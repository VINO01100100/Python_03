#practice Function 
#return a last char in name
#Ex)

# def last_char(name):#definig fuction and  argument
#     return name[-1]
# print(last_char("vinod"))#passing parameter and calling function


#que.1) even odd using fuction
#Type 1
# num = int(input("Enter number: "))
# def even_odd(num):
#     if num%2 == 0:
#         return "even"
#     else:
#         return "odd"
# print(even_odd(num))

#Type 2 but is return True Or False
num = int(input("Enter number: "))
def even_odd(num):
    return num%2 == 0
print(even_odd(num))
