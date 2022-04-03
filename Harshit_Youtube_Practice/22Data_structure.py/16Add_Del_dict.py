user_info = {
    'name' : 'vinod',
    'age' : 21,
    'fav_movie' : 'lion_king'
}

#Add data in Dictionary
user_info['fav_song'] = ['song1', 'song2']
print (user_info)

#delete data in Dict (pop)

poped_iteam = user_info.pop('fav_song')#pop iteam stored in variable
print (f"your poped item is{poped_iteam}")
print (user_info)

#pop iteam 
pop_item = user_info.popitem()#popiteam remove randamly key pair element
print (pop_item)#tuole return
print (user_info)