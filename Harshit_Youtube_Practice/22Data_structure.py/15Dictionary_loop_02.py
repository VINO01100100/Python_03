
user_info = {
    'name' : 'vinod',
    'age' : 21,
    'fav_movoe' : 'lion_king'
}
#codition
if 'name' in user_info:#in keyword only check key
#if 'name' in user_info.value(): 
    print ('present')
else:
    print('not present')

#Iteam method

for key , value in user_info.items():
    print (f'key is {key} : value {value}')