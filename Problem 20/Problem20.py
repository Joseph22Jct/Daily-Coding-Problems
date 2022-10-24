# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

# For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

# In this example, assume nodes with the same value are the exact same node objects.

# Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.

class Node(object):
    def __init__(self, value, Node=None) -> None:
        self.val = value
        self.next = Node
        

def FindLink(A, B):
    while(A.next != None and B.next!=None):
        print ("A = "+ str(A.val) + " B = "+ str(B.val))
        if(A.val == B.val):
            return A.val
        else:
            A = A.next
            B = B.next
    return None ##No value found
    pass


def main():
    LLA = Node(3, Node(7, Node(8, Node(10))))
    LLB = Node(99, Node(1, Node(8, Node(10))))
    print(FindLink(LLA, LLB))
    pass

if __name__ == "__main__":
    main()
    