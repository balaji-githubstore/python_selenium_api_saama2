def my_prop(func):
    return func()


@my_prop
def get_method():
    return "Balaji Dinakaran"



print(get_method)
