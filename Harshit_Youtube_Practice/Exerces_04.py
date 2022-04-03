import random
wining_number = random.randint(0,100)
Gussing_number = int(input("Enter your gussing number: "))

if wining_number == Gussing_number:
    print("WIN!!!!!!!")
else:
    if Gussing_number < wining_number:#It is called nested if else
        print("To low !!!!\n")
    else:
        print("To high!!!!")