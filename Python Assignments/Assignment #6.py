# Assignment #6
# Name: Winston Lu
# Block: 1-4
# Date: Jan 19 2017
#
# Part A: Write a function called fib(n, f1 = 1, f2 = 1) such that it returns a list containing
# the first n terms in the Fibonacci sequence. The first and second term of the Fibonacco
# sequence is given by the values of f1 and f2 respectively. The next term is determined by
# the sum of the last two terms

def fib(n, f1 = 1, f2 = 1):
    fibList = []
    switch = False
    try:
        if (n <= 0):        #exceptions
            return(None)
        elif (n >= 1):      #test for the exception when n=1,2
            fibList.append(f1)
            if (n >= 2):
                fibList.append(f2)
        while (n > 2):      
            fibList.append(f1 + f2)
            if (switch == False):   #Switches between reassigning f1 and f2
                f1 = f1+f2
                switch = True
            else:
                f2 = f1+f2
                switch = False    
            n -= 1
        return(fibList)
    except:
        print('There was an error when assigning variables.')
        




# Test Cases:
fib(8, 1, 1)    # returns the list (1, 1, 2, 3, 5, 8, 13, 21)
fib(10, 0, 2)   # returns the list (0, 2, 2, 4, 6, 10, 16, 26, 42, 68)
fib(1, -1, 0)   # returns (-1)


# Part B: Write a function called product() that asks the user to enter a number and stores the value
# into a list. The function continues to ask the user to enter a number until a non-number is entered.
# The function then prints the list of numbers followed by its product (i.e. multiply all the numbers
# in the list).
#
# ~ Sample Output ~
# Enter a number: 5
# Enter a number: 2
# Enter a number: -3
# Enter a number: anyString
# The list is [5, 2, -3] and its product is -30.

def product():
    numDB = []
    x = 0
    leng = 0
    ans = 1
    while (type(x) == float or type(x) == int):
        try:
            x = float(input('Enter a number: '))
            numDB.append(x)
        except:
            break
    while(len(numDB) > leng):   #Checks length of list
        if (numDB[leng] == 0):  #Checks if there is a 0 in the list
            print('The list is', str(numDB) , 'and its product is 0.' )
            return
        else:
            ans *= int(numDB[leng]) #Normal multiplying operations
            leng += 1
    print('The list is', str(numDB) , 'and its product is' , str(ans) + '.' )
        



# Part C: Write a function called gcf(m,n) which finds the greatest common factor (GCF) between
# two integers m and n. The GCF is the largest number that m and n can be divided by. Hint: A number
# is divisible if its remainder is zero.

def gcf(m,n):
    gcf = 1
    mult = 1
    x = True
    try:
        if(m == 1 or n==1):     # exception when m or n = 1
            print('The GCF between',m,'and',n,'is: 1.')
            return
        elif(m==0 or n==0):     # exception when m or n = 0
            print('The GCF between',m,'and',n,'is: undefined.')
            return
        else:
            while (mult <= m and mult <= n):    #checks weither the multiplier is equal or less than m or n
                if (m % mult == 0 and n % mult == 0):   #checks weither it is a perfect factor
                    gcf = mult
                mult += 1
        print('The GCF between',m,'and',n,'is:',str(gcf) + '.')
    except:
        None





# ~ Test Cases ~
#gcf(5, 2)     # 1
#gcf(50, 20)   # 10
#gcf(5, 10)    # 5
#gcf(1,2)      # 1
#gcf(0,5)      # undefined
