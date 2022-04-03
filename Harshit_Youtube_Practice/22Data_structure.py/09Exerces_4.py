#Filter Even or Odd

def even_odd(lst):
    # lst =int(lst)
    even = []
    odd = []
    for i in lst:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return odd, even
numbers= [1,2,3,4,5]
print(even_odd(numbers))