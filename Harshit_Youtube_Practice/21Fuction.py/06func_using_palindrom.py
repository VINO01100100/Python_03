def palindrome(name):
    name1 = name[::-1]
    return name == name1
    
print(palindrome("madam"))

#using user input: 

# name = input("Enter name to check palindrome or not: ")
# def palindrome(name):
#     name1 = name[::-1]
#     return name == name1
# print(palindrome(name))