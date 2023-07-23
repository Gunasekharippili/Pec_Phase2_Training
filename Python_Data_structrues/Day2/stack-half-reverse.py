
class stack:
    arr = []
    arr1 = []
    size = 10

    def stack_push(self, element):
        if len(self.arr) == self.size:
            print("stack is full")
        else:
            self.arr.append(element)

    def stack_pop(self):
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

    def half_reverse(self):
        low = 0
        high = len(self.arr)-1
        half = (low+high)//2
        while half < high:
            pop = self.arr.pop(high)
            self.arr.insert(half+1, pop)
            half += 1
        print(self.arr)

    def first_half_reverse(self):
        low = 0
        high = len(self.arr)-1
        half = (low+high)//2
        while half > low:
            pop = self.arr.pop(low)
            self.arr.insert(half, pop)
            half -= 1
        print(self.arr)



s = stack()
s.stack_push(10)
s.stack_push(20)
s.stack_push(30)
s.stack_push(40)
s.stack_push(50)
s.stack_push(60)
# s.stack_push(70)
# s.stack_push(80)


print(s.arr)
s.half_reverse()
#print(s.arr)

s.first_half_reverse()
