# class Studant:
#     def __init__(self, name, roll, hight):
#         self.name = name
#         self.roll = roll
#         self.hight = hight
#     def Print_details(self):
#         return self.name, self.roll, self.hight
# s = Studant("vinod", 57, 5.9)

# print(s.Print_details())

# class car:
#     def __init__(self,color, model_name):
#         self.color = color
#         self.model_name = model_name
#     def Print_details(self):
#         print(self.color, self.model_name)
# c1 = car("black", "Jeep_Campus")
# c1.Print_details()




# class Trangle:
#     pass
# t1 = Trangle()
# t1.a=2
# t1.b=3
# t1.c=4
# def prameter(t1):
#     p = t1.a + t1.b + t1.c
#     print(p)
# prameter(t1)

#Inharitance
#Single Inharitance
# class A:

#     def DisA(self):
#         print("Print Im a A")
# class B(A):
#     def DisB():
#         print("Im in B")    
# obj1 = B
# A.DisA(obj1)

#Method Overriding
# class parent:
#     def Dis(self):
#         print("Im parent class")
# class Child:
#     def DisA(self):
#         print("Im in child class")
# obj1 = Child
# parent.Dis(obj1)

#Insecapsulation
class ABC:
    def __init__(self,X,Y,Z):
        self.var1 = X
        self._var2 = Y
        self.__var3 = Z
obj1 = ABC(2, 3, 4)
print(obj1.var1)
print(obj1._var2)
print(obj1.__var3)