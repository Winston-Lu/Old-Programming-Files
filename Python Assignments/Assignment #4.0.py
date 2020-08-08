# Assignment 4
# Name:
# Block:
#
# Task A:
# Write a function called repeatString(myString, n) that prints myString
# a total of n times. The default value of n is 1, meaning that calling
# the function repeatString(myString) will print out my string once.
# The function must use at least one while loop and handle three exceptions
# without using try-except statements:
#   1. prints ‘n is invalid’ when n is a non-integer 
#   2. prints ‘n is invalid’ when n is a negative number
#   3. prints nothing when n = 0.
#  
# Note: Create your own test cases based on scenario.

def repeatString(myString,n):
    if (type(n)!=int or n<0):
        print("n is invalid")
    elif (n > 0):
        print(myString)
        repeatString(myString,n - 1)
    else:
        return(None)
    

#repeatString("Hello", 2)
repeatString("Hello", 0)
#repeatString("Hello", -2)
#repeatString("Hello", "two")

# Hello
# Hello




# Task B:
# Write a function called triangle(n = 1) that visually prints the sum
# of the first n consecutive integers and returns the actual sum. n must
# be a positive integer.
#


def triangle(n):
    counter = 0
    num = 1
    if (n == 1):
        print("triangle(1) = 1 = 1")
        return
    if(not n<=0):
        if(n==1):
            return(1)
        else:
            print("triangle(" + str(n) + ") =", end=" ")
            while (counter<n):
                print(num, end=" + ")
                counter = counter+1
                num = num+1
                if(counter==n - 1):
                    ans = n/2 * (2 + (n-1))         # formula for arithmetic series
                    print(counter + 1, "=", int(ans))
                    return
    else:
        return(None)



# Test Case
triangle(5)
triangle(6)
triangle(10)
#triangle(5) = 1 + 2 + 3 + 4 + 5 = 15


