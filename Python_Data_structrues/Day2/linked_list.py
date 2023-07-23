class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:

    def add_ele_at_start(self, head, value):
        newNode = Node(value)
        newNode.next = head
        head = newNode
        return head

    def add_element(self, head, value):
        newNode = Node(value)
        temp = head
        while temp.next != None:
            temp = temp.next
        temp.next = newNode

    def remove_element(self):
        temp = head
        while temp.next.next != None:
            temp = temp.next
        temp.next = None

    def print_list(self):
        temp = head
        while temp != None:
            print(temp.data, end='->')
            temp = temp.next

    def search_element(self):
        pass

    def insert(self, head, value, pos):
        newNode = Node(value)
        curr = head
        prev = None
        while pos != 0:
            prev = curr
            curr = curr.next
            pos = pos-1
        prev.next = newNode
        newNode.next = curr

    def reverse(self, head):
        cur = head
        prev = None
        while cur != None:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev

obj = LinkedList()
head = Node(10)
obj.add_element(head, 20)
obj.add_element(head, 30)
obj.add_element(head, 40)
obj.add_element(head, 50)
obj.add_element(head, 60)
# obj.print_list()
#head = obj.add_ele_at_start(head, 69)
#obj.print_list()
head = obj.reverse(head)
obj.print_list()