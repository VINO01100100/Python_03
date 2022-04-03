#Eroor resolve
num1 = int(input("Enter first number: "))
num2 = int(input("Enter secound number: "))
num3 = int(input("Enter third number: ")) 

def two_gretest(num1,num2):
    if num1>num2:
        return "num 1 is greter"

    return"num 2 is greter"
print(two_gretest(num1, num2))

def new_gretest(num1, num2, num3):
    bigger = two_gretest(num1, num2)
    return two_gretest(bigger,num3)
print(new_gretest(num1, num2, num3))

