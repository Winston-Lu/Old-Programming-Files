# Assignment 5
# Name: Winston Lu
# Block: 1-4
#
# Task A: Create a function called binary(n) that returns the binary string of n,
# where n is a non-negative integer. Do not use bin(n) function. Include exceptions.

def binary(n):
    if (type(n) == int or type(n) == float): 
        if (n==0):
            return(0)
        elif(n<0):
            print('The variable can not be a negative number.')
            return
        elif (n%2 == 1):
            binary((n-1)/2)
            print('1'[::-1], end='')
        elif (n%2 == 0):
            binary(n/2) 
            print('0'[::-1], end='')


# Task B: Create a function called isPalindrome(x) that returns True if x is a
# palindrome and False otherwise. The data type can either be a number or a string.
# Make your code efficient. Include exceptions.

def isPalindrome(x):
    return(str(x)[::-1] == str(x))


# Task C: Create a function called sqrt(x, g = 1, n = 10000) that returns the
# square root of x using the Babylonian method (only +, -, x , /), where g is
# your intial guess and n is the *maximum* number of times the guess is refined.
# Make your code efficient. Include exceptions.

def sqrt(x, g=1, n=1000, count=1): # Made max guesses 1,000 , 10,000 seems too much and runs too long for non-perfect squares
    if (type(x)!=int and type(x)!=float or type(g)!=int and type(g)!=float or type(n)!=int and type(n)!=float):
        print('There was an error when reassigning variables.')
        return
    elif (x==0 or g==0):
            return(0)
    elif(x<0):
        print('Negative numbers can not be square rooted.')
        return
    while (count <= n and g*g != x):
        guess = (x + g*g) / (2*g)
        error = guess - g
        g = guess
        print('Guess #' + str(count) , ':', str(guess) + ', guess may be off by up to:', str(error) + '.')
        count+=1
    else:
        print('The Answer is:', str(g) + '.') 



