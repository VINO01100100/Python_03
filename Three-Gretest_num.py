num1=int(input("enter first number\n"))
num2=int(input("enter secound number\n"))
num3=int(input("enter theered number\n"))

if num1>num2 and num1>num3:
    print("Firset number  greter:")
elif num2>num1 and num2>num3:
    print("secound number  greter:")
elif num3>num2 and num3>num1:
    print("Thired number is greter:")
else:
    print("number are same:")