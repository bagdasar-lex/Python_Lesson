# name = input("Введите Имя: ")
# for i in range(0, 3):
#    print(name)

# name = input("Enter a name: ")
# num = int(input("Enter number: "))
#  for i in range(0, num):
#    print(name)

# num = int(input("Enter a number"))
# name = input("Enter a name!: ")
# for x in range(0, num):
#    for i in name:
#        print(i)


# num = int(input("Enter a number between 1 - 12 : "))
# for i in range(1, 13):
#    answer = num * i
#    print(i, "x", num, "=", answer)

# num = int(input("Enter a number less that 50: "))
# num2 = num - 1
# for i in range(50, num2, -1):  # или тут прос num-1
#    print(i)

# name = input("Enter a name: ")
# num = int(input("Enter number: "))
# if num < 10:
#    for i in range(0, num):
#        print(name)
# else:
#    print("Number too hight")


# total = 0
# print("Enter a number 5 times ")
# for i in range(0, 5):
#   num = int(input("Enter a number: "))
#    ans = input("Do you want include this to sum (y/n): ")
#    if ans == "y":
#        total = total + num
# print(total)

# ans = input("Wich direction count? (< or >): ")
# if ans == "<":
#    num = int(input("Enter a number less 20: "))
#    for i in range(20, num-1, -1):
#        print(i)
# elif ans == ">":
#    num = int(input("Enter a number: "))
#    for i in range(1, num+1):
#        print(i)
# else:
#    print("I dont understand!!")

peopleCount = int(input("How many person you want to invite?:"))
if peopleCount < 10:
    for i in range(0, peopleCount):
        name = input("Enter name to invite: ")
        print(name, "Has been invite! ")
else:
    print("To many person!!!")
