#reverse method
def rever_lst(l):
    l.reverse()
    return l
numbers= [1,2,3,4,5]
print(rever_lst(numbers))

#slicing

def slicing_list(l):
    return l[::-1]
numbers= [1,2,3,4,5]
print(slicing_list(numbers))

#pop and uppend
def reverse_list(lst):
    r_list = []
    for i in range(len(lst)):
        poped_list = lst.pop()
        r_list.append(poped_list)
    return r_list
numbers= [1,2,3,4,5]
print(rever_lst(numbers))
