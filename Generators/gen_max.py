def g(x):
    if not x:
        return

    m = x[0]
    for i in x:
        if i > m:
            m = i
        yield m

v = [3, 1, 4, 2]
print(list(g(v)))  # Output: [3, 3, 4, 4]
