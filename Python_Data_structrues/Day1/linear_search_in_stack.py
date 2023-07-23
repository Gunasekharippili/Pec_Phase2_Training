class stack:
    def __init__(self):
        self.size=5
        self.arr=[]
    def push(self,element):
        self.arr.append(element)
    def stack_pop(self):
        self.arr.pop()
    def lineary_search(self,key):
        for i in range(len(self.arr)):
            if key == self.arr[i]:
                print("found at :", i)
        else:
            print("Element not found")


obj=stack()
obj.push(10)
obj.push(20)
obj.push(30)
obj.push(40)
obj.push(50)
obj.push(60)
print(obj.arr)
obj.arr.sort()
obj.lineary_search(60)