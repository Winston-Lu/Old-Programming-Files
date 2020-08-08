# Assignment 5 Part D:
# Write a function called searchList(myList, myCriteria) which searches
# through all the elements of myList and returns the first index number that matches myCriteria
# If none of the elements match myCriteria, then return None

def searchList(myList, myCriteria):
    num = 0
    try:
        while (True):
            if (myList[num] == myCriteria):
                print(num)
                break
            else:
                num += 1
    except:
        return(None)
        
# Test cases:

searchList(['hello','bye'],'hello') #= 0
searchList([3,4,6,1,1], 6)          #= 2
searchList([3,4,6,1,1], 1)          #= 3
searchList([3,4,6,1,1], 7)          #= None
