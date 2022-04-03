def revese_element(lst):
    element = []
    for i in lst:
        element.append(i[::-1])
    return element
numbers= ['a,b,c', 't,u,v', 'x,y,z']
print(revese_element(numbers))


#slicing
def slicing_list(l):
    return l[0][::-1], l[1][::-1], l[2][::-1]
numbers= ['a,b,c', 't,u,v', 'x,y,z']
print(slicing_list(numbers))
