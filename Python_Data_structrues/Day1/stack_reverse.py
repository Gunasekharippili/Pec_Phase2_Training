#implement stack and reverse it but the o/p should be in same input order

class stack:
    def __init__(self):
        self.arr = []
        self.size = 3
    def stack_push(self, element):
        if len(self.arr) == self.size:
            print("stack is full")
        else: 
             return self.arr.append(element)
    def stack_pop(self):
        if len(self.arr) == 0:
            print("stack is underflow") 
        else:
            return self.arr.pop()
    def stack_peek(self):
        if len(self.arr) == 0:
            print("underflow")
        else:    
            return self.arr[-1]
    def isEmpty(self):
        if len(self.arr) == 0:
            return True
        else:
            return False 
# obj1= stack() 
# obj2= stack() 
# for i in range(obj1.size):
#     obj1.stack_push(i)
# print(obj1.arr) 
# for j in  obj1.arr:
#     obj2.stack_push(obj1.stack_pop())
# print(obj2.arr) 
s1=stack() 
s1.stack_push(10)
s1.stack_push(20)
s1.stack_push(30)
print(s1.arr)

s2=stack()
s2.stack_push(s1.stack_pop())
s2.stack_push(s1.stack_pop())
s2.stack_push(s1.stack_pop()) 
print(s2.arr)

