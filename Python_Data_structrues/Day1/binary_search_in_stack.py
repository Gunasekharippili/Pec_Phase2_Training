class stack:
    def __init__(self):
        self.size = 5
        self.arr = []

    def push(self, element):
        self.arr.append(element)

    def stack_pop(self):
        self.arr.pop()

    def binary_search(self, key):
        low = 0
        high = len(self.arr)-1
        while low <= high:
            mid = (low+high)//2
            if self.arr[mid] == key:
                print('found at', mid)
                break
            elif key < self.arr[mid]:
                high = mid-1
            elif key > self.arr[mid]:
                low = mid+1
        else:
            print('not found')


obj = stack()
obj.push(10)
obj.push(20)
obj.push(30)
obj.push(40)
obj.push(50)
obj.push(60)
print(obj.arr)
obj.binary_search(50)
