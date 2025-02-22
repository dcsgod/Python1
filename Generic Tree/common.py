class Treenode:
    def __init__(self, data):
        self.data=data
        self.children=[]

def print_tree(root):
    if root==None:
        return
    print(root.data,end=":")

    for x in root.children:
        print(x.data,end=',')
    print()
    for x in root.children:
        print_tree(x)