# Good morning! Here's your coding interview problem for today.

# This problem was asked by Airbnb.

# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

# Follow-up: Can you do this in O(N) time and constant space?

def solve(array):

    if(len(array)<=2):
        return max(array)
    else:
        storedvals = [0 for i in array] ##Set every position to 0 so we dont have to check every number being positve or not
        storedvals[0] = max(0,array[0])
        storedvals[1] = max(storedvals[0], array[1]) #set up

        for i in range(2, len(array)):
            storedvals[i] = max(array[i]+ storedvals[i-2], storedvals[i-1]) #Check backwards, rather than forwards
        return storedvals[-1] ##Last element
            




def main():
    test1 = [2,4,6,2,5]
    test2= [5,1,1,5]
    test3= [-1,0,0,-2,-3]
    print(solve(test1))
    print(solve(test2))
    print(solve(test3))
    pass

if __name__ == "__main__":
    main()

    #  while(ongoing):
    #         if(currentIndex==0):
    #             if(array[currentIndex]>array[currentIndex+1]):
    #                 if(array[currentIndex]>0):
    #                     summ+=array[currentIndex]
    #                 currentIndex+=2
    #             else:
    #                 if(array[currentIndex]>0)
    #                     summ+=array[currentIndex+1]
    #                 currentIndex+=3
    #         elif(currentIndex==len(array)-1):
    #             pass
    #         else:
    #             if(array[currentIndex]>array[currentIndex+1] and array[currentIndex]>array[currentIndex+2]):
    #                 if(array[currentIndex]>0):
    #                     summ+=array[currentIndex]
    #                 currentIndex+=2
                    
    #             elif(array[currentIndex+1]>array[currentIndex] and array[currentIndex+1]>array[currentIndex+2]):
    #                 if(array[currentIndex]>0):
    #                     summ+=array[currentIndex]
    #                 currentIndex+=2

    #         pass

    #  summ = 0
    #     currentIndex = 0
    #     while(True):
    #         print("current array["+str(currentIndex)+"] is: "+str(array[currentIndex]))
    #         if(currentIndex+2<len(array)-1):
    #             if(array[currentIndex]>array[currentIndex+1] and array[currentIndex]>array[currentIndex+2]):
    #                 if(array[currentIndex]>0):
    #                     summ+=array[currentIndex]
    #                 currentIndex+=2
    #             else:
    #                 currentIndex+=1
    #         elif(currentIndex+1<len(array)-1):
    #             if(array[currentIndex]>array[currentIndex+1]):
    #                 if(array[currentIndex]>0):
    #                     summ+=array[currentIndex]
    #                 return summ
    #             else:
    #                 if(array[currentIndex+1]>0):
    #                     summ+=array[currentIndex]
    #                 return summ
    #         else:
    #             if(array[currentIndex]>0):
    #                     summ+=array[currentIndex]
    #             return summ