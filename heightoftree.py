from generictree import predefined_generic_tree_inputs
#from common import print_tree
def height_of_tree(root):
    if root == None:
        return
    
    height=1
    max_height=0
    for x in root.children:
        max_height= max(max_height,height_of_tree(x))
    
    height+=max_height
    return height

root1,root2, root3=predefined_generic_tree_inputs()
print(height_of_tree(root1))
print(height_of_tree(root2))
print(height_of_tree(root3))
#print_tree(root2)