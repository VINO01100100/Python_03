num1 = int(input("Enter first number: "))
num2 = int(input("Enter secound number: "))
num3 = int(input("Enter third number: "))
def greter(num1,num2,num3):
    if num1>num2 and num1>num3:
        return "num1 is greter"
    elif num2>num1 and num2>num3:
        return "num2 is greter"
    else:
        return "num3 is greter"
print(greter(num1,num2,num3))
