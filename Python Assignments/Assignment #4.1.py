def decimal(n):
    if (type(n) != int or type(n) != float): 
        if (n==0):
            return(0)
        elif (n%2 == 1):
            decimal((n-1)/2)
            print('1'[::-1], end='')
        elif (n%2 == 0):
            decimal(n/2) 
            print('0'[::-1], end='')
    else:
        return(None)



