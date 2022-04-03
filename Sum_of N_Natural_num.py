#Formula: Sum =num1(num1+1)/2 (n Natural number)
num1 = int(input("Enter the last number sum:-"))
sum = int(num1*(num1+1)/2)
print(sum)

#using while

num1 = int(input("Enter the number you want upto sum\n"))
i = 1
sum = 0
while (i<=num1):
    sum = sum +i
    i = i+1
print("your sum is",sum)