class stack:
    arr=[] 
    size=5 
    def stack_push(self, element):
        if len(self.arr) == self.size:
            print("stack is full")
        else: 
            self.arr.append(element)
    def stack_pop(self) :
        if len(self.arr) == 0:
            print("stack is underflow") 
        else:
            self.arr.pop()
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

s=stack()
s.stack_push(10)
s.stack_push(20)
s.stack_push(30)
s.stack_push(40)
print(s.arr)
print(s.stack_peek())
s.stack_pop()
s.stack_pop()
s.stack_pop()
print(s.stack_peek())
print(s.isEmpty())