#Check a Multipal condition to use elif
#ex):-
#Movie Ticket Pricing
# 1 to  3  (Free)
# 4 to  10 (150)
# 11 to 60 (250)
# above 60 (200)


age = int(input("Enter your age:"))
if age== 0 or age<0:
    print("You cannot watch movie:-")
elif  0<age<=3:
    print("You Watch movie Free:-")
elif  3<age<=10:
    print("Movie Ticket 150:-")
elif  11<age<60:
    print("Movie Ticket 250:-")
else:
    print("Movie Ticket 200:-")