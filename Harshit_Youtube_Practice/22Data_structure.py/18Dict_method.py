#fromkey is use to set default value in dict
D1 = dict.fromkeys(['name', 'age', 'hight'],'unkhown')
print (D1)
#output : {'name': 'unkhown', 'age': 'unkhown', 'hight': 'unkhown'}

#get method (imp)
#get method is to access perticular key

user = {'name' : 'vinod' , 'age' : 21}
print(user.get('name'))#only keys acess

if user.get('names'):# if can evalute none is not present
    print("present")
else:
    print("not present")
