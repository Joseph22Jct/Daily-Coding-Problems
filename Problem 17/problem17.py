# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Suppose we represent our file system by a string in the following manner:

# The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

# dir
#     subdir1
#     subdir2
#         file.ext
# The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

# The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

# dir
#     subdir1
#         file1.ext
#         subsubdir1
#     subdir2
#         subsubdir2
#             file2.ext
# The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. 
# subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

# We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, 
# the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).

# Given a string representing the file system in the above format, return the length of the longest absolute path to a file in the abstracted file system. 
# If there is no file in the system, return 0.

# Note:

# The name of a file contains at least a period and an extension.

# The name of a directory or sub-directory will not contain a period.

##Approach: Turn these directories into nodes, then gather the leaves and just count recursively the parents and return the longest? no... because this takes 
# itno account directory NAMES
##I SHOULD be getting all leaves though, because extra info just adds to the count, theres no case a leave would subtract from a total count.
##So rather, every node should have a parent, name, and child node.
##The first challenge is reading the string.
##OOOHHH /n is new line and /t is tab im a moron.

def readString(s,prevNode = None, rootNode = None, listOfLeaves = []):
    newNodeName = ""
    def readNextLevel(st):
        level = 0
        for x in st:
            if(x=="\t"):
                level+=1
            else:
                return level


    for x in range(len(s)):
        if(s[x] == "\n"):
            newNode = Node(prevNode, newNodeName)
            if(rootNode==None):
                newNode.level = 0
                rootNode = newNode
            if(prevNode != None):
                prevNode.child.append(newNode)
                
            nextLevel = readNextLevel(s[x+1:])
            
            if(nextLevel == newNode.level+1):
                readString(s[x+1:], newNode,rootNode, listOfLeaves)
            elif( nextLevel <= newNode.level):
                listOfLeaves.append(newNode)
                cNode = newNode
                #if(newNode.level == nextLevel):
                cNode = newNode.parent
                for x in range(newNode.level-nextLevel):
                    cNode = cNode.parent
                readString(s[x+1:], cNode,rootNode, listOfLeaves)
            break
            
        elif(s[x] == "\t"):
            pass
        else:
            newNodeName+=s[x]
            
    newNode = Node(prevNode, newNodeName)
    if(rootNode==None):
        newNode.level = 0
        rootNode = newNode
    if(prevNode != None):
        prevNode.child.append(newNode)
        
    listOfLeaves.append(newNode)
  
    return listOfLeaves
            
def TurnToString(Nodes):
    stringList = []
    for x in Nodes:
        currentString = ""
        cNode = x
        currentString+= cNode.nodeName
        while(cNode.parent != None):
            cNode = cNode.parent
            currentString = cNode.nodeName+"/"+currentString
        stringList.append(currentString)
    return stringList


class Node(object):
    def __init__(self, parent = None, name = None):
        self.parent = parent
        self.nodeName = name
        self.child = []
        if (parent==None):
            self.level = 0
        else:
            self.level = parent.level+1

def solve(string):
    leaves = readString(string)
    #print(str(leaves))
    leavesString = TurnToString(leaves)
    print(str(leavesString))
    return max(leavesString, key=len)

def main():
    print(solve("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"))
    print(solve("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))
    

if __name__=="__main__":
    main()