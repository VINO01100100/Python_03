# class Queue:
#     def __init__(self,size):
#         self.__capacity = size
#         self.__arr = []
#         self.__front = -1
#         self.__rear = -1

#     def isFull(self):
#         if self.__front == 0 and self.__rear == self.__capacity -1:
#             return True
#         return False

#     def get_queue(self):
#         print(self.__arr)


#     def enqueue(self, value):
#         if(self.isFull()):
#             print("enqueue is full")
#         else:
#             if len(self.__arr) == 0:
#                 self.__arr.append(value)
#                 self.__front += 1
#                 self.__rear += 1
#             else:
#                 self.__arr.append(value)
#                 self.__rear += 1
#             print(str(value) + " is enqueued is succesfully...")
#     def isEmpty(self):
#         if self.__front == -1 and self.__rear == -1:
#             return True
#         else:
#             return False
#     def dequeue(self):
#         if(self.isEmpty()):
#             print("Queue is Empty")
#         elif(self.__front == self.__rear):
#             self.__rear.pop()
#             self.__front = -1
#             self.__rear = -1
#         else:
#             self.__arr.pop(0)
#             self.__front += 1
            
# queue = Queue(5)

# queue.enqueue(10)
# queue.enqueue(20)
# queue.enqueue(30)
# queue.enqueue(40)


#stack
class Stack:
    def __init__(self,size):
       self.size = size
       self.list = []
    def is_full(self):
        if len(self.list)<(self.size):
            return True
        else:
            return False

    def is_empty(self):
        if len(self.list)== 0:
            return True
        else:
            return False
    def push(self,value):
        if self.is_full():
            self.list.append(value)
            print("Element insert succesfully")
        else:
            print("stack is full")
    def pop(self):
        if self.is_empty():
            self.list.pop()
        else:
            print("stack is empty")
    def print_stack(self):
        return self.list
s1 = Stack(int(input("Enter a stack size")))
while True:
    print("1.Add element in stack")
    print("2.Delete element in stack")
    print("3.print element in stack")
    print("4.exit")
    





            


        

        