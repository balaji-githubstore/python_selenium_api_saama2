def greeting(name):
    def hello():
        return "Hello, " + name + "!"
    return hello

greet = greeting("Atlantis")
print(greet())  # prints "Hello, Atlantis!"


def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return  0.2

        return func(a, b)
    return inner


def divide(a, b):
    return a/b


div=smart_divide(divide)
print(div)

print(div(4,4))
# div
