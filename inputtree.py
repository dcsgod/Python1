from common import Treenode, print_tree

def take_input():
    data=int(input("Enter the data for the node"))
    node=Treenode(data)
    num_child=int(input(f"Enter the number of the child for {data}"))
    for child in range(num_child):
        child=take_input()
        node.children.append(child)

    return node

root=take_input()
print_tree(root)