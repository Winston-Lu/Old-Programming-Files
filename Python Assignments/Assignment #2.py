# Assignment 2
# Name: Winston Lu
# Block: 2-4
#
# Task: Write a function called pythag(a,b) that
# takes in two parameters, a and b, which represent
# the length of the legs of a right triangle and
# returns the length of the hypotenuse c by using
# the Pythagorus Theorem. c is rounded to the
# nearest hundredths (two decimal places)

def pythag(a,b):
    if (type(a)==str or type(b)==str):
        return 0
    elif (a<=0 or b<=0):
        return 0
    elif (a>0 and b>0):
        aSqrd = float(a**2)
        bSqrd = float(b**2)
        cSqrd = aSqrd + bSqrd
        c = cSqrd ** 0.5
        cRound = round(c,2)
        return(cRound)

# Test Cases - Passing
print(pythag(3, 4))		# 5.0	(float)
print(pythag(6, 8.0))		# 10.0
print(pythag(5.0, 12))		# 13.0
print(pythag(1, 1))		# 1.41

# Test Cases - Mostly Meeting
print(pythag(-3, 4))		# 0 	(int)
print(pythag(3, -4))		# 0
print(pythag(-3, -4))		# 0


# Test Cases - Fully Meeting
print(pythag(3, "one"))	        # 0
print(pythag("one", "hello"))	# 0


# Criteria
# +5 marks: solves for hypotenuse c
# +1 mark: accepts integers
# +1 mark: accepts floats
# +1 mark: rounds to two decimal places (i.e. hundredths)
# +1 mark: rejects negatives
# +1 mark: rejects non-real numbers (e.g. strings)
# -1 mark: poorly named variables. :(
# -1 mark: printed (not returned)















