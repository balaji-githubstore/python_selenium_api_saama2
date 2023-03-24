# 1 to 10

# for i in range(1, 11):
#     print(i)

numbers = [78, 65, 45, 12, 4, 5, 88, 42, 68, 41, 21, 28, 54]

# print(len(numbers))

# 0 to 12

# print only value that are less than or equal to 50

for i in range(0, len(numbers)):
    if numbers[i] == 12:
        print(numbers[i])
        break

for i in range(0, len(numbers)):
    if numbers[i] == 12:
        continue
    print(numbers[i])
