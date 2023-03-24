def gen_func(x):
    for i in range(x):
        yield i


r = gen_func(5)
print(r)
print(type(r))

print(next(r))
print(next(r))


def simpleGeneratorFun():
    yield
    yield 2
    yield 3


# Driver code to check above generator function
for value in simpleGeneratorFun():
    print(value)


def config():
    print("browser launch")
    yield
    print("browser close")



config()

