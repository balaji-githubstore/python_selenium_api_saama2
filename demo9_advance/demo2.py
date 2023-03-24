def hello1():
    return 'hi'


def hello2():
    print("browser launch")
    yield 'start'
    print("end browser")
    yield 'done'


print(hello1())
print(hello2())

for val in hello2():
    print(val)

#complete the feedback in chat window
#Finish the final assessment  - link in chat