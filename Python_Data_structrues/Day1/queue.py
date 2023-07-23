class queue:
    arr=[] 
    size=5 
    def enqueue(self, element):
        if len(self.arr) == self.size:
            print("Queue is full")
        else: 
            self.arr.append(element)
    def dequeue(self):
        if len(self.arr) == 0:
            print("queue is underflow")
        else:
            self.arr.pop(0)
    def queue_peek(self):
        if len(self.arr) == 0:
            print("underflow")
        else:    
            return self.arr[0]
    def isEmpty(self):
        if len(self.arr)==0:
            return True
        else:
            return False 

s=queue() 
s.enqueue(10)
s.enqueue(20)
s.enqueue(30)
print(s.arr)
s.dequeue()
print(s.arr)
print(s.queue_peek())