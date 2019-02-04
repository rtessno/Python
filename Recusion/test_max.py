import timeit
print('recursion_max results')
t = timeit.Timer("import recursion_max")
results = t.repeat(5, 1000000)
for i, item in enumerate(results):
    print(i, "\t", item)
print('python built in max results')
t = timeit.Timer("import Python_builtin_max")
results = t.repeat(5, 1000000)
for i, item in enumerate(results):
    print(i, "\t", item)
print()
