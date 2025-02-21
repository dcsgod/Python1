# Here we are Trying to Take input Level wise
from common import Treenode, print_tree
from collections import deque

def take_input_level_wise():
    data=int(input("Enter the root Data"))
    root= Treenode(data)
    queue=deque([root])
    while queue:
        current_node=queue.popleft()
        num_child=int(input("Enter the number of child of " + str(current_node.data)))

        for i in range(num_child):
            childdata=int(input(f"Enter the Data for child {i+1} of Node {current_node.data}"))
            childnode=Treenode(childdata)
            current_node.children.append(childnode)
            queue.append(childnode)

    return root

root=take_input_level_wise()
print_tree(root)

