import random
wining_number = random.randint(0,100)
Guessing_number = int(input("Enter your gussing number: "))
guess = 0
game_over = False
while not game_over:
    if Guessing_number == wining_number:
        print("You are win!!!!")
        print(f"you are guess {guess} times")
        game_over = True
    else:
        print("Guess Wrog!!!!")
        if Guessing_number < wining_number:
            print("To low Guess!!!!")
            # guess += 1#dry code
            # Guessing_number = int(input("Guess Again: "))
        else:
            print("To High Guess!!!!")
    guess += 1
    Guessing_number = int(input("Guess Again: "))#Dry code optimize your code line
