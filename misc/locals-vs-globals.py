def f(x):
    y = 2
    print(locals())
    return y
y = f(1)
print(globals())


