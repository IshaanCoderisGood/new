def check(num1, num2):
    if (num1 ^ num2) != 0:
        print("they are not equal")
    else:
        print("they are equal")

num1=int(input("What is the first number: "))
num2=int(input("What is the second number: "))

check(num1, num2)

#Ab