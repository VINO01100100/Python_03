#Update maethod is use to udate data in dictionary

user_info = {
    'name' : 'vinod',
    'age' : 21,
    'fav_movie' : 'lion_king'
}

more_info = {'state' : 'colardro', 'country'  : 'US'}

user_info.update(more_info)#you can passing same key in more info they can change the
#origanlal key
print (user_info)