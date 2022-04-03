num = input("Enter a number more than one digit: ")
sum = 0
for i in range(0, len(num)):
    sum += int(num[i])
print(sum)