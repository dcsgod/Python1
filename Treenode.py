class Treenode:
    def __init__(self, data):
        self.data=data
        self.children=[]


root=Treenode(1)
ch1=Treenode(2)
ch2=Treenode(3)
ch3=Treenode(4)
root.children.append(ch1)
root.children.append(ch2)
ch1.children.append(ch3)

def print_tree(root):
    if root==None:
        return
    print(root.data,end=":")
    
    for x in root.children:
        print(x.data,end=',')
    print()
    for x in root.children:
        print_tree(x)


print_tree(root)