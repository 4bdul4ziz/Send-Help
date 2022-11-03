# Let T be a given Binary Tree (not necessarily complete  Full / Perfect) with k elements.
# The elements are arranged in T such that an In-Order traversal will print the questions in Non-decreasing order of the value of the elements.
# Write a Program that will Re-arrange the elements in the tree such that, upon performing a Post-Order Traversal, the elements should be output in Non-decreasing order.
# Also, print the root node of the tree before and after re-arrangement.
# Your program should work for any input and be generic. You should not perform sorting on the elements.


class BinaryTree:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def insert_left(self, key):
        if self.left:
            node = BinaryTree(key)
            node.left = self.left
            self.left = node
        else:
            self.left = BinaryTree(key)

    def insert_right(self, key):
        if self.right:
            node = BinaryTree(key)
            node.right = self.right
            self.right = node
        else:
            self.right = BinaryTree(key)


def preorder(tree):
    if not tree:
        return
    print(tree.key)
    [preorder(tree.left)]
    [preorder(tree.right)]


def inorder(tree):
    if not tree:
        return
    [inorder(tree.left)]
    print(tree.key)
    [inorder(tree.right)]


def postorder(tree):
    if not tree:
        return
    postorder(tree.left)
    postorder(tree.right)
    print(tree.key)


tree = BinaryTree(1)
tree.insert_left(2)
tree.insert_right(3)
tree.left.insert_left(4)
tree.left.insert_right(5)
tree.right.insert_left(6)
tree.right.insert_right(7)

print("The root node is: ", tree)
print("Pre-Order Traversal")
preorder(tree)
print("\nIn-Order Traversal")
inorder(tree)
print("\nPost-Order Traversal")
postorder(tree)
