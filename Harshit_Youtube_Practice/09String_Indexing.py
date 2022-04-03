prg = "Python"
print(prg[2])#alwas string inndexing in [] bracket

#STRING SLICING
#SYNTAX:[Start Argument : End Argument]

print(prg[2:4])#you can print specific length

print(prg[:2])#only print the py 0 or 1 indexing element

print(prg[2:])#first two char not and print remaning string

#SAME AS NEGATIVE INDEXING

print(prg[-1])#print the last char of string

#STEP ARGUMENT
#SYNTAX:[Start Argument : End Argument, Step]

print(prg[1:6:2])
#output: yhn is count is two step

#Reverse string using slicing
svkm = "organazation"
# print(svkm[::-1])
print(svkm[10:5:-1])