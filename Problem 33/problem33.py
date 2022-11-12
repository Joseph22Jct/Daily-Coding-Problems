# Good morning! Here's your coding interview problem for today.

# This problem was asked by Microsoft.

# Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.

# Recall that the median of an even-numbered list is the average of the two middle numbers.

# For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

# 2
# 1.5
# 2
# 3.5
# 2
# 2
# 2
def solve(ls):
    if(len(ls)>0):
        currentList = []
        currentList.append(ls[0])
        print(ls[0])
    if(len(ls)>1):
        for x in range(len(ls))[1:]:
            #print("current X: "+ str(x))
            currentList.append(ls[x])
            currentList.sort()
            if(x%2 == 1):
                print((currentList[int(x/2)]+currentList[int(x/2)+1])/2)  
            else:
                print(currentList[int(x/2)]) 
            
        
        

def main():
    list1 = [2, 1, 5, 7, 2, 0, 5]
    solve(list1)
    pass

if __name__ == "__main__":
    main()
