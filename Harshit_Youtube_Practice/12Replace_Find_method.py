#replace()
#replace method replace the character with passing another charcter

string = "she is betiful and she is very good dancer"

print(string.replace("is","was",1))#passing how many char replace
#output: she was betiful and she was very good dancer

#find()
#find method is use to find the position of charcter in a string

print(string.find("is"))
#output: 4

#find the next is postion
pos1= string.find("is")
pos2= string.find("is",pos1+1)#pos1 + 1 work to first is skip then find next is
print(pos2)