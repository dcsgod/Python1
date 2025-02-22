class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def takeinput():
    data=int(input("Enter the Data for the Node"))

    if data==-1:
        return None

    node= BinaryTreeNode(data)
    print(f"Enter the Left Child of {data}")
    node.left=takeinput()

    print(f"Enter the Right Child of {data}")
    node.right=takeinput()

    return node


print("Enter the Binary Tree Data (-1) for No node")

root= takeinput()
from binarytree import print_binary_tree
print_binary_tree(root)