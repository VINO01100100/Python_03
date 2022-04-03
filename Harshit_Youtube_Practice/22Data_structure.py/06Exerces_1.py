def squre_func (l):
    sqr = []
    for i in l:
        sqr.append(i**2)
    return sqr
number = list(range(1, 11))
print(squre_func(number))
