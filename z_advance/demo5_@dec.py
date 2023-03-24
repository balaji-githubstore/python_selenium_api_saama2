class MyProp:
    def __init__(self, func):
        self.get_me(func)

    def get_me(self, func):
        return func()


@MyProp
def get_method():
    return "Balaji Dinakaran"


print(get_method)



