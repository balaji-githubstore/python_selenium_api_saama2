def my_prop(func):
    return str(func()).upper()


@my_prop
def get_name():
    return "hello world"


# register the decorator to your function
# get_name = my_prop(get_name)

# instead of above code - we can @my_prop to the existing method

print(get_name)
