# Good morning! Here's your coding interview problem for today.

# This problem was asked by Snapchat.

# Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

# For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

##Could have optimized by sorting the arrays first.....

def solve(array):
    arrayOfTimeSlots = [[]]
    arrayOfTimeSlots[0].append(array[0])
    for x in array[1:]:
        dontAddTime = True
        for z in arrayOfTimeSlots:
            print("Comparing "+str(x)+ " with " + str(z))
            for y in z:
                print(str(x[0])+">"+ str(y[0])+ " "+ str(x[0])+"<"+ str(y[1]) + " and "+str(x[1])+">"+ str(y[0])+ " "+str(x[1])+"<"+ str(y[1]) + " ")
                if(not (x[0]>y[0] and x[0]<y[1]) and not (x[1]>y[0] and x[1]<y[1])):
                    dontAddTime = False
                    pass
            if (not dontAddTime):
                
                z.append(x)
                break
        if(not dontAddTime):
            break
        if(dontAddTime):
            arrayOfTimeSlots.append([])
            arrayOfTimeSlots[-1].append(x)
            
    for x in arrayOfTimeSlots:
        print(str(x))
    
    print ("There's " + str(len(arrayOfTimeSlots))+ " TimeSlots")
    return arrayOfTimeSlots
    pass

def main():
    solve([(30, 75), (0, 50), (60, 150)])
    pass

if __name__ == "__main__":
    main()