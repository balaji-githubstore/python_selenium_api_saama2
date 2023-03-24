name = 'balaji dinakaran'
colors = ['red', 'green', 'yellow', 'orange']

print(type(name))
print(type(name))

print(name[0])

print(colors[0])

print(len(name))
print(len(colors))

print(name.title())
print(name.capitalize())
print(name.upper())
print(name.lower())

new_name = name.replace("dinakaran", "D")

print(new_name)

sal1 = '$200,000'
sal2 = '$300,890,233'
sal1=sal1.replace("$","").replace(",","")
sal2=sal2.replace("$","").replace(",","")

print(int(sal1)+int(sal2))

print(float(sal1)+float(sal2))

#sub string
name="hello world"

#final index will be excluded
print(len(name))
print(name[0:5])
print(name[6:11])

print(name[1:])
print(name[6:])
print(name[name.index("world"):])
data="Hellow is a form of greeting used by a hyper-active person in The Netherlands."
print(data.index("Netherlands"))

print(data[data.index("greet"):])

email_id='balaji_d01@gmail.com'

print(email_id.replace('@gmail.com',''))
print(email_id.index("@"))

print(email_id[0:email_id.index("@")])

output=email_id.split("@")
print(output)
print(len(output))

print(output[0])

print(email_id.split('@')[0])
