#define function and check how many list pass in list

def check_list(lst):
    for i in lst:
        countr = 0
        if type(i) == list:
            countr += 1

    return countr
mixed = [[1,2,3],[2,3,4],[5,6,7]]
print(check_list(mixed))