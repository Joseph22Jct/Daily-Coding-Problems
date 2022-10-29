# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be smaller than the length of the list.

# The list is very long, so making more than one pass is prohibitively expensive.

# Do this in constant space and in one pass.





def solve(LL):
    pass

class LinkedList(object):
    def __init__(self, next = None) -> None:
        self.previous = None
        self.next = next
        if(next!=None):
            next.previous = self


def main():
    LL = LinkedList(LinkedList(LinkedList()))
    solve(LL)

if __name__ == "__main__":
    main()