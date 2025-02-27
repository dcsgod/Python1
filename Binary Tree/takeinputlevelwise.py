from collections import deque
from binarytree import BinaryTreeNode

def takeinput_levelwise():
    data=int(input("Enter the Data for the Root: "))
    if data==-1:
        return
    
    root = BinaryTreeNode(data)
    queue=deque([root])
    while len(queue) !=0:
        currentnode= queue.popleft()

        lcdata=int(input(f"enter the left child for {currentnode.data}: "))
        if lcdata !=-1:
            leftnode=BinaryTreeNode(lcdata)
            currentnode.left=leftnode
            queue.append(leftnode)

        rcdata=int(input(f"enter the right child for {currentnode.data}: "))
        if rcdata !=-1:
            rightnode=BinaryTreeNode(rcdata)
            currentnode.right=rightnode
            queue.append(rightnode)
        
    return root



root= takeinput_levelwise()
from binarytree import print_binary_tree
print_binary_tree(root)
