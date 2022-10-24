# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

# For example, given the following Node class

# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# The following test should pass:

# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'

##Aproach: maybe have the root look like this: thought process: maybe we first start doing ((r)) and use parenthesis to determine left and right nodes, but that will not work
## Now i thought perhaps using "01r02" where the number on the left represents the vertical level away from root and the number to the right represents which slot horizontally, but
##Thats not an elegan solution.
##Now the one I think ill implement is getting only the tip of the branching nodes (in this case, root.left.left and root.right) and build a node tree based on that.

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(node):
    strToReturn = ""
    path=[node]
    for x in path:
        if(x.left != None):
            path.append(x.left)
        if(x.right!= None):
            path.append(x.right)
        if(x.right == None and x.left == None):
            strToReturn+= x.val+","

    print(strToReturn)
        
    return strToReturn

def deserialize(strng):
    nodeToReturn = Node("root")
    strCheck = ""
    nodesToAdd=[]
    for x in strng:
        if(x=="l" or x =="r" or x=="."):##we only care for these symbols
            strCheck+=x
        elif(x==","): 
            strCheck+=" "
            nodesToAdd.append(strCheck) 
            strCheck = ""

    print(str(nodesToAdd))
    cNode = nodeToReturn
    cstr=""
    for x in nodesToAdd:
        for y in range(len(x)):
            if(x[y]=="r"):
                if(cNode.right == None):
                    cNode.right = Node(cstr+"right")
                if(x[y+1]=="."):
                    cstr+="right."
                    cNode= cNode.right
            elif(x[y]=="l"):
                if(cNode.left == None):
                    cNode.left = Node(cstr+"left")
                if(x[y+1]=="."):
                    cstr+="left."
                    cNode= cNode.left
            elif(x[y]==" "): ##If theres no more then return to root.
                print("Node ended at "+ cNode.val)
                if(cNode.left!= None):
                    print(" with l = " + cNode.left.val)
                if(cNode.right!= None):
                    print(" with r = " + cNode.right.val)
                cNode=nodeToReturn
    return nodeToReturn

def main():
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'

if __name__ == "__main__":
    main()
    