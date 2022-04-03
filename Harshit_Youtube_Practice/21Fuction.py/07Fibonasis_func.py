#print fibonasis serias using def fuction

num = int(input("Enter a last number you want: "))
def fibonasis(num):
    a = 0
    b = 1
    if num == 1:
        print(a)
    elif num == 2:
        print(a, b)
    else:
        print(a, b, end=" ")
        for i in range(num - 2):
            c = a + b
            a = b
            b = c
            print(b, end=" ")
fibonasis(num)
