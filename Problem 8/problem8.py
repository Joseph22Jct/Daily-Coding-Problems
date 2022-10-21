# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

# Given the root to a binary tree, count the number of unival subtrees.

# For example, the following tree has 5 unival subtrees:

#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1

#    0
#   / \
#  1   1
#     / \
#    1   1
#   / \
#  1   1

count = 0

def rec(Node):
    global count
    if(Node.left == None and Node.right == None):
        count+=1
        return True
    left = True
    right = True
    if(Node.left !=None):
        left = rec(Node.left) and Node.val == Node.left.val
    if(Node.right!=None):
        right = rec(Node.right) and Node.val == Node.right.val
    if(left==True and right == True):
        count+=1
        return True
    else:
        return False



def solve(NodeTree):
    global count
    count = 0
    rec(NodeTree)
    print(count)
    
    pass

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


def main():
    test1 = Node(0,Node(1), Node(0, Node(1,Node(1), Node(1)), Node(0))) ##Example node
    test2 = Node(0,Node(1), Node(1, Node(1,Node(1), Node(1)), Node(1)))
    test3 = Node(0,Node(1), Node(1, Node(1,Node(1), Node(1)), Node(1,Node(1), Node(1))))
    solve(test1)
    solve(test2)
    solve(test3)
    pass


if __name__ == "__main__":
    main()

# def CountTree(NodeTree, currentString):
#     global trees
#     if(NodeTree.left!= None):
#         newString = currentString + str(NodeTree.val)
#         CountTree(NodeTree.left, newString)
#     if(NodeTree.right!= None):
#         newString = currentString + str(NodeTree.val)
#         CountTree(NodeTree.right, newString)
#     if(NodeTree.left == None and NodeTree.right == None):
#         print(NodeTree.val)
#         trees.append(currentString+ str(NodeTree.val))
#         return
    
# def CountTree(Node):
# if(Node.left==None and Node.right ==None):
#     trees.append(str(Node.val))
# elif(Node.left!=None and Node.right == None):
#     if(Node.left.val == Node.val):
#         trees.append(str(Node.val))
#     CountTree(Node.left)
# elif(Node.right!=None and Node.left == None):
#     if(Node.right.val == Node.val):
#         trees.append(str(Node.val))
#     CountTree(Node.right)
# elif(Node.right!=None and Node.left !=None):
#     if(Node.right.val == Node.val and Node.left.val == Node.val):
#         trees.append(str(Node.val))
#     CountTree(Node.right)
#     CountTree(Node.left)
