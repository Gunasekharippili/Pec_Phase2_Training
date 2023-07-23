class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        self.prev = None

class double_linked_List():
    def add(self, value):
        newNode = Node(value)
        temp = head
        while temp.next != None:
            temp = temp.next
        temp.next = newNode
        newNode.prev = temp
    def print(self):
        temp = head
        while temp != None:
            print(temp.data)
            temp = temp.next
        print()
    def revese(self):
        temp = head
        while temp.next != None:
            temp = temp.next
        while temp:
            print("<-", temp.data,end="")
            temp = temp.prev
        print()

    def remove(self):
        temp = head
        while temp.next.next != None:
            temp = temp.next
        temp.next.prev = None
        temp.next = None


obj = double_linked_List()
head = Node(10)
obj.add(20)
obj.add(30)
obj.add(40)
obj.remove()
obj.print()