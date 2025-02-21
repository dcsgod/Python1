from generictree import predefined_generic_tree_inputs


# preorderTraversal: In this kind of traversal Root is Printed First then its child got Printed
def preordertraversal(root):

    if root is None:
        return

    print (root.data,sep="",end=',')
    for x in root.children:
        preordertraversal(x)

#postorder traversal: First child got printed then root is printed
def postordertraversal(root):
    if root is None:
        return
    for x in root.children:
        postordertraversal(x)
    print(root.data,end=" ,")

root1,root2,root3= predefined_generic_tree_inputs()
print("Preorder Traversal:")
preordertraversal(root1)
print()
print("Postorder Traversal:")
postordertraversal(root1)
