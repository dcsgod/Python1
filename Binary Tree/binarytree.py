class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

root= BinaryTreeNode(1)
root.left=BinaryTreeNode(2)
root.right=BinaryTreeNode(3)

#printing Binary Tree Using Recursion

def print_binary_tree(root):

    if root is None:
        return

    print(root.data,end=":")

    if root.left is not None:
        print(f"L-> {root.left.data}",end=",")
    else:
        print("L-> NONE", end=",")

    if root.right is not None:
        print(f"R-> {root.right.data}")
    else:
        print("R-> NONE",)

    #Recursion for Left and Right child

    print_binary_tree(root.left)
    print_binary_tree(root.right)

#from predefinedbinarytree import predefined_binary_tree_inputs

#root1, root2, root3 = predefined_binary_tree_inputs()

#print_binary_tree(root1)