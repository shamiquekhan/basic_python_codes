class treeNode:
    def __init__(self,keys):
        self.key=keys
        self.left=None
        self.right=None
node0=treeNode(3)    
node1=treeNode(4) 
node2=treeNode(5) 
node0.left=node1
node0.right=node2
tree=node0
print(tree.key)
print(tree.left.key)
print(tree.right.key)
