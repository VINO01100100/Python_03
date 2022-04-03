#Min Max Function
# min max use to find minimun or maximu number in list 
 
# numbers = [50,60,70,20]
# print(min(numbers))
# print(max(numbers))

def dist_func(lst):
    num = max(lst) - min(lst)
    return num
numbers = [50,60,70,20]
print(dist_func(numbers))