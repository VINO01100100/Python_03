num1 = int(input("enter a start num: "))
num2 = int(input("enter a end num: "))
for num  in range(num1, num2):
    if all(num%i !=0 for i in range(2,num)):
        print(num)
