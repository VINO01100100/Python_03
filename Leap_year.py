year = int(input("Enter which year check leap or not:- "))
if ((year%4 == 0) and ( year%100 != 0 ) or (year%400 == 0 ) ):
    print(year,"this year is leap year")
else:
    print(year,"This year not leap year")