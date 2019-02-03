# Using one of the testing frameworks we discussed write a Encryption class
# that has an encrypt method and a decrypt method. The encrypt method takes
# a string that is encrypts and returns the decrypted text and vice-versa.
# For the encryption key use the Ceaser Cipher.
# https://en.wikipedia.org/wiki/Caesar_cipher Write unit tests that cover the
# encrypt method and the decrypt method.


# The encrypt method takes a string that is encrypted
# and returns the decrypted text and vice-versa.
class Encryption:
    #Encrypt the string and return the ciphertext#
    def encrypt(self):
        result = ''
        for l in self.lower():
            try:
                i = (key.index(l) + 3) % 26
                result += key[i]
            except ValueError:
                result += l
            if l.isdigit():
                 raise ValueError('Numbers Are Not Allowed')
        return result.lower()

    def decrypt(self):

        result = ''

        ciphertext = self

        for l in ciphertext:
            try:
                i = (key.index(l) - 3) % 26
                result += key[i]
            except ValueError:
                result += l
        if ciphertext == '':
            raise ValueError('String is Empty')
        for l in ciphertext:
            if l.isdigit():
                raise ValueError('Numbers Are Not Allowed')

        return result

###Decrypt the string and return the plaintext###
key = 'abcdefghijklmnopqrstuvwxyz'
#################### Your Message to Encrypt ####################
string = 'attack at dawn'
############################################################
print('The string to encrypt and decrypt: ', '"',string,'"',sep='')
print('The string is now encrypted: ','"',Encryption.encrypt(string),'"',sep='')
print('The string is now decrypted: ','"',Encryption.decrypt(Encryption.encrypt(string)),'"',sep='')



###raises ValueError for empty string for decrypt
# print(Encryption.decrypt(''))

###raises ValueError becuase numbers are not allowed encrypt
# print(Encryption.encrypt('attack at 3 pm'))

###raises ValueError because numvers are bot allowed to decrypt
# print(Encryption.decrypt('dwwdfn1'))
