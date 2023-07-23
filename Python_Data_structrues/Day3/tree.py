class Node:
    def __init__(self,value):
        self.data = value
        self.left = None
        self.right = None

class bs_tree:
    def add(self, root, value):
        new_node = Node(value)
        if new_node.data < root.data:
            if root.left != None:
                self.add(root.left, value)
            else:
                root.left = new_node
        else:
            if root.right != None:
                self.add(root.right, value)
            else:
                root.right = new_node

    def inorder(self,root):
        if root.left != None:
            self.inorder(root.left)
        print(root.data, end=" ")
        if root.right != None:
            self.inorder(root.right)

    def preorder(self, root):
        print(root.data, end=" ")

        if root.left != None:
            self.preorder(root.left)

        if root.right != None:
            self.preorder(root.right)

    def postorder(self, root):

        if root.left != None:
            self.postorder(root.left)

        if root.right != None:
            self.postorder(root.right)

        print(root.data, end=" ")
    def levelorder(self, root):
        q = []
        q.append(root)
        while len(q) != 0:
            ele = q.pop(0)
            print(ele.data, end=" ")
            if ele.left:
                q.append(ele.left)
            if ele.right:
                q.append(ele.right)





obj = bs_tree()
root = Node(10)
obj.add(root, 7)
obj.add(root, 40)
obj.add(root, 5)
obj.add(root, 9)
obj.add(root, 15)
obj.add(root, 60)
obj.inorder(root)
print("\nInoder complete")
obj.preorder(root)
print("\npreoder complete")
obj.postorder(root)
print("\npostorder complete")
obj.levelorder(root)
print("\nlevelorder complete")