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

    def searching(self, root, key):
        if root.data == key:
            print("found")
            return
        elif root.data > key:
            if root.left != None:
                if root.left != key:
                    self.searching(root.left, key)
                else:
                    print("found")
            else:
                print("not found")

    def search(self, root, key):
        if root.data == key:
            return root
        if key < root.data and root.left != None:
            return self.search(root.left, key)
        if key > root.data and root.right != None:
            return self.search(root.right, key)


        elif root.data < key:
            if root.right != None:
                if root.right != key:
                    self.searching(root.right, key)
                else:
                    print("found")
            else:
                print("not found")

    def sum_of_left_right_subtree(self, root):
        sum = root.data
        if root.left != None:
            sum += self.sum_of_left_right_subtree(root.left)

        if root.right != None:
            sum += self.sum_of_left_right_subtree(root.right)
        return sum

    def tree_height(self, root):
        if root == None:
            return -1
        left_height = self.tree_height(root.left)
        right_height = self.tree_height(root.right)

        return 1 + max(left_height, right_height)





obj = bs_tree()
root = Node(10)
obj.add(root, 7)
obj.add(root, 40)
obj.add(root, 5)
obj.add(root, 9)
obj.add(root, 15)
obj.add(root, 60)
# obj.searching(root, 1000)

# print(obj.sum_of_left_right_subtree(root))
# print(obj.sum_of_left_right_subtree(root.left))
# print(obj.sum_of_left_right_subtree(root.right))

# print(obj.search(root, 69))
# if obj.search(root, 9):
#     print("found")
# else:
#     print("Not found")


print(obj.tree_height(root))