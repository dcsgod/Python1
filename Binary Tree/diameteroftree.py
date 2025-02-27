#Diameter of tree = Maximum Distance between two nodes
# diameter of tree = leftheight+rightheight
# we find diameter of all subtree and take maximum of all

def height(root):

    if root is None:
        return 0

    leftheight = height(root.left)
    rightheight= height(root.right)
    heightoftree= 1+max(leftheight,rightheight)

    return heightoftree


def diameteroftree(root):

    if root is None:
        return 0

    leftheight=height(root.left)
    rightheight=height(root.right)

    leftdiameter= diameteroftree(root.left)
    rightdiameter=diameteroftree(root.right)
    ans= max(leftdiameter,rightdiameter,leftheight+rightheight)

    return ans


from predefinedbinarytree import predefined_binary_tree_inputs

root1, root2, root3= predefined_binary_tree_inputs()

print("Diameter of given tree is : ", diameteroftree(root3))

