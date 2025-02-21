from generictree import predefined_generic_tree_inputs

def count_nodes(root):
    if root == None:
        return
    
    count=1
    for x in root.children:
        count += count_nodes(x)
    return count

root1,root2, root3=predefined_generic_tree_inputs()
print(count_nodes(root1))
print(count_nodes(root2))
print(count_nodes(root3))