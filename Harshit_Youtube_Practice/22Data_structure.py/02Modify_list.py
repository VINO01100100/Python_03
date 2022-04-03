##append method
#append is method to add element in last position list

lst1 = ["apple", "orange",]
lst1.append("graph")
print(lst1)


##insert method
#insert is add in element in specific index
 
lst2 = ["cherry", "watermelon"]
lst2.insert(1,"banana")
print(lst2)

##Add two list elements

lst3 = lst1 + lst2
print(lst3) 

##Extend method 
#Extend is use to add two list elment in single list

lst1.extend(lst2)
lst1.append(lst2)#its methos to list inside in list
print(lst1)


##count method
#count method is use to count element in list

lst4 =["apple", "orange","apple", "kivi"]
print(lst4.count("apple"))

##sort method
#sort method is used to sort elements in list
lst4.sort()
print(lst4)

##Delete element in list
#pop method always delete element in last 

fruits = ["kivi", "pear", "papaya", "chiku"]
fruits.pop()
#fruits.pop(3) you can also delete specific index
print(fruits)

