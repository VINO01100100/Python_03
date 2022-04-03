num = input("Enter a number more than one digit: ")
i=0
sum = 0
while i<len(num):
    sum += int(num[i])
    i += 1
print(sum)
