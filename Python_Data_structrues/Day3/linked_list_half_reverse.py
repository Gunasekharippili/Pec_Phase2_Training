class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class linked_list:
    def add_ele(self,head,value):
        new_node = Node(value)
        temp = head
        while temp.next != None:
            temp = temp.next
        temp.next = new_node

    def print(self):
        temp = head
        while temp != None:
            print(temp.data, end = '->')
            temp = temp.next

    def half_reverse(self):
        first = head
        cur = head
        prev = None
        n = 3
        while n != 0:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            n -= 1
        first.next = cur
        return prev

obj = linked_list()
head = Node(10)
obj.add_ele(head,20)
obj.add_ele(head,30)
obj.add_ele(head,40)
obj.add_ele(head,50)
obj.add_ele(head,60)
obj.print()
print("/n")
head = obj.half_reverse()
obj.print()