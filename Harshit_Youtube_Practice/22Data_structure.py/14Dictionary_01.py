#dictionary is key value pair of data
#unorderform data callection

#1syntax

user = {'name': 'vinod', 'age': 21}
print(user)

#2syntax
user1 = dict(name =  'nakul',  age =  20)
print(user1)

#Data Access in dictionary
#Access data in dictionary is key and value not indexing
print(user1['name'])
#output: nakul

#add data to dictionary

user2 = {}
user2['name'] = 'kiran'
user2['age'] = 21
print(user2)
#output : {'name': 'kiran', 'age': 21}