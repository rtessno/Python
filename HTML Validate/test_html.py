import timeit

t = timeit.Timer("import check_html")
results = t.repeat(5, 1000000)
for i, item in enumerate(results):
    print(i, "\t", item)





