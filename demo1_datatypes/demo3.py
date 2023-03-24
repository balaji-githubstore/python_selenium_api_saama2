colors = ['red', 'green', 'yellow', 'orange']

print(type(colors))

print(colors)

print(colors[2])

print(colors[1:4])
print(colors[1:])

colors.append("blue")

print(colors)

colors.append("black")
print(colors)

colors.insert(0,"pink")

print(colors)

print(colors.index("orange"))

colors.remove("green")

print(colors)

colors.append("green")
colors.append("green")

print(colors)

print(colors.count("red"))
print(colors.count("green"))

print(len(colors))

print('-' * 50)

print(colors)
value=colors.pop()
print(value)
print(colors)

value=colors.pop()
print(value)
print(colors)

print(colors[1])
colors.remove(colors[1])
print(colors)