from searching import binary_string_list
import timeit
a_list =['florida','beautifully','gradual','station','sour','apple','safety', 'simple','skilled','core',
         'transport','pick','anxiously','practically','profession', 'courage','Sunday','funeral','inside','generously']
for i in a_list:
    binary_string_list.list_object.append(i)
print(binary_string_list.list_object)
print("timeit test using one of the words in the list looking for the word 'simple'")
t = timeit.Timer("binary_string_list.BinaryStringList.binary_search('pick')", "import binary_string_list")
results = t.repeat(5, 1000000)
for i, item in enumerate(results):
    print(i, "\t", item)
print("timeit test using one of the words NOT in the list looking for the word 'dimple'")
t = timeit.Timer("binary_string_list.BinaryStringList.binary_search('dimple')", "import binary_string_list")
results = t.repeat(5, 1000000)
for i, item in enumerate(results):
    print(i, "\t", item)
