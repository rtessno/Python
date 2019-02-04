# Create a test program called sequential_test.py.
# Create an instance of your SequentialStringList and add 20 strings to it.
# Create a timeit test using one of the words in the list and the find method and another timeit test using a word not in the list and the find method.
# Create another test program called binary_test.py and perform the same tests. Compare the
# results and write a brief discussion of your findings. In your discussion, include an analysis of the time complexity, i.e Big O.
from searching import sequential_search
import timeit

a_list =['florida','beautifully','gradual','station','sour','apple','safety', 'simple','skilled','core',
         'transport','pick','anxiously','practically','profession', 'courage','Sunday','funeral','inside','generously']


for i in a_list:
    sequential_search.SequentialStringList.add(i)

print(sequential_search.list_objects)
print("timeit test using one of the words in the list looking for the word 'simple'")
t = timeit.Timer("sequential_search.SequentialStringList.find('simple')", "import sequential_search")
results = t.repeat(5, 1000000)
for i, item in enumerate(results):
    print(i, "\t", item)
print("timeit test using one of the words NOT in the list looking for the word 'dimple'")
t = timeit.Timer("sequential_search.SequentialStringList.find('dimple')", "import sequential_search")
results = t.repeat(5, 1000000)
for i, item in enumerate(results):
    print(i, "\t", item)

