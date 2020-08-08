# Assignment 3
# Name: Winston Lu
# Block: 1-4
# 
# Task A: Create a function called sqrt(x) that
# returns the square root of x if x is non-negative;
# otherwise, return None. Assume x is a number. [2]

def sqrt(x):
    if(type(x)==int or type(x)==float):
        if(x<0):
            return(None)
        else:
            ans = x**0.5
            return(ans)
    else:
        return(None)

# Test Cases:
print(sqrt(25))		# 5.0
print(sqrt(0))		# 0.0
print(sqrt(2.0))	# 1.414...
print(sqrt(-4))		# None
    
# Task B: Create a function called linear(b,c) that
# solves bx + c = 0 for x and returns the answer x
# rounded to 3 decimal places (i.e. thousandths).
# Include exceptions such as the case when b = 0
# and when b or c is not numeric. [3]

def linear(b,c):
    numberB = type(b) == int or type(b) == float
    numberC = type(c) == int or type(c) == float
    if (numberB and numberC == True):
        if(b!=0):         
            ans = -c/b
            x = round(ans,3)
            return(x)
        else:
            return(None)
    else:
        return(None)

# Test Cases:
print(linear(2,5))	# -2.5
print(linear(3,-1))	# 0.333
print(linear(0,1))	# None
print(linear(1,"pi"))	# None

# Task C: Create a function called quad(a,b,c) that
# solves ax^2 + bx + c = 0 for x using the quadratic 
# equation and return x to 3 decimal places. The
# function should call the other functions from Task
# A and B. Include exceptions. [10]

def quad(a,b,c):
    numberA = type(a) == int or type(a) == float
    numberB = type(b) == int or type(b) == float
    numberC = type(c) == int or type(c) == float
    if(a==0):
        x = linear(b,c)
        return(x)
    if(numberA == True and numberB == True and numberC == True):
        discrim = b**2-(4*a*c)
        if (discrim < 0):
            return(None)
        if (discrim == 0):
            ans1 = linear(2*a,b)
            return(ans1)
        if (discrim > 0):
            ans2 = linear(2*a , b + sqrt(discrim))
            ans3 = linear(2*a , b - sqrt(discrim))
            return(ans2,ans3)                     
    else:
        return(None)



# Test Cases:
print(quad(4,-5,1))	# 0.25, 1.0
print(quad(6,-9,1))	# 0.121, 1.379
print(quad(1,2,1))	# -1.0
print(quad(1,1,1))	# None
print(quad(0,5,2))	# -0.4
print(quad(0,0,2))	# None
print(quad("a",2,3))	# None


