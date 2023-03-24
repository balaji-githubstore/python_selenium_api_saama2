def my_prop(func):
    return func()


def get_method():
    return "Balaji Dinakaran"


my_prop = my_prop(get_method)
print(my_prop)

