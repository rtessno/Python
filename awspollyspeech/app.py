from chalice import Chalice, Response
from contextlib import closing
import os
import uuid
from tempfile import gettempdir
import boto3
import subprocess
from io import BytesIO
from PIL import Image


app = Chalice(app_name='AWSPollyIMGSpeech')

BUCKET_NAME = 'roberts-speech'


def text_to_speech(text, voice):
    '''
    Uses AWS Polly to convert the given text to speech
    :param text: the text to convert
    :param voice: the voice to use
    :return: the url of where to access the converted file.
    '''
    # code taken from/based on
    # https://aws.amazon.com/blogs/ai/build-your-own-text-to-speech-applications-with-amazon-polly/,
    # last access 10/29/2017
    rest = text

    # Because single invocation of the polly synthesize_speech api can
    # transform text with about 1,500 characters, we are dividing the
    # post into blocks of approximately 1,000 characters.
    print('Setting up textBlocks')
    textBlocks = []
    while (len(rest) > 1100):
        begin = 0
        end = rest.find(".", 1000)

        if (end == -1):
            end = rest.find(" ", 1000)

        textBlock = rest[begin:end]
        rest = rest[end:]
        textBlocks.append(textBlock)
    textBlocks.append(rest)
    print('textBlocks:', textBlocks)

    # For each block, invoke Polly API, which will transform text into audio
    print('Creating polly client')
    polly = boto3.client('polly')
    filename = '{}.mp3'.format(uuid.uuid4())
    print('filename:', filename)
    for textBlock in textBlocks:
        response = polly.synthesize_speech(
            OutputFormat='mp3',
            Text=textBlock,
            VoiceId=voice
        )

        # Save the audio stream returned by Amazon Polly on Lambda's temp
        # directory. If there are multiple text blocks, the audio stream
        # will be combined into a single file.
        if "AudioStream" in response:
            with closing(response["AudioStream"]) as stream:
                output = os.path.join(gettempdir(), filename)
                print('Outputting to', output)
                with open(output, "ab") as file:
                    file.write(stream.read())

    s3 = boto3.client('s3')
    print('Uploading {} to S3'.format(filename))
    s3.upload_file(os.path.join(gettempdir(), filename),
                   BUCKET_NAME,
                   filename)
    print('Setting ACL')
    s3.put_object_acl(ACL='public-read',
                      Bucket=BUCKET_NAME,
                      Key=filename)
    print('Returning URL')
    return 'https://s3.amazonaws.com/{}/{}'.format(BUCKET_NAME, filename)


def get_image_from_file(filename):
    """
    Loads and returns the bytes of the image from the specified file
    :param filename: the name of the file
    Based on
       https://docs.aws.amazon.com/rekognition/latest/dg/example4.html,
       last access 10/3/2017
    """
    with open(filename, 'rb') as imgfile:
        return imgfile.read()



def get_labels(img, confidence=50):
    client = boto3.client('rekognition')
    # imgbytes = get_image_from_file(img)
    rekresp = client.detect_labels(Image={'Bytes': img},
                                   MinConfidence=confidence)
    text = ''
    count = 0
    while count < len(rekresp['Labels']):
        # print(rekresp['Labels'][count]['Name'], end=', ')
        text += rekresp['Labels'][count]['Name'] + ' '
        count = count + 1
    return text



@app.route('/AWSPollyIMGSpeech/{voice}', content_types=['image/png'], methods=['GET','POST','PUT'], cors=True)
def AWSPollyIMGSpeech(voice):
    im = Image.open(BytesIO(app.current_request.raw_body))
    out = BytesIO()
    # receives raw image byes from upload and sends to get_labels function
    text = get_labels(app.current_request.raw_body)
    print('new text ', text)
    im.save(out, 'PNG')
    if im is None or voice is None:
        return {"Error": "text and/or voice not set"}
    return Response(status_code=200,
                    headers={
                        'Content-Type': 'image/png',
                        # 'voice': voice,s
                        # 'labels': text,
                        # 'url': text_to_speech(text, voice)
                    },
                    body={'voice': voice,
                          'labels': text,
                          'url': text_to_speech(text, voice)})

