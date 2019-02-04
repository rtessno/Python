from sorting import bubble_string_list
import timeit

alist = ['Victor','Zulu','Charlie','Mike','Whiskey','Quebec', 'Golf','Papa',
          'Juliet', 'Kilo','Yankee','Delta','November',
          'Oscar','India', 'Foxtrot','Romeo','Alpha',
          'Tango','Uniform','Sierra', 'Echo', 'X-ray',
          'Lima', 'Bravo']


for i in alist:
    bubble_string_list.BubbleStringList.add(i)


print("timeit test, testing bubble_string_list.BubbleStringList.sort_obj()")
t = timeit.Timer("bubble_string_list.BubbleStringList.sort_obj(bubble_string_list.obj_list)", "import bubble_string_list")
results = t.repeat(5, 1000000)
for i, item in enumerate(results):
    print(i, "\t", item)


