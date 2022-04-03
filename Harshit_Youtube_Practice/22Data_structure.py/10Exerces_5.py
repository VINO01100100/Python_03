#comman element in two lists
def cooman_list(lst1, lst2):
    comman = []
    for i in lst1:
        if i in lst2:
            comman.append(i)
    return comman
print(cooman_list([1,2,3,4,5], [1,5,2,3,9]))