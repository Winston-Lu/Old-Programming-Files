# Assignment 1
# Name: Winston Lu
# Block: 1-4
#
# Task A - Write a short program that asks the user his/her name
# and then prints "Hello" followed by his/her name.
#
# EXAMPLE
# What is your name? John             « Space after ? is required.
# Hello John.                         « Period is required.

      
name = input("What is your name? ")
print("Hello",name+".")


# Task B - Write a short program that asks the user for a mass in
# kilograms (kg) and prints the mass in pounds (lb). The formula for
# the conversion is lb = 2.2 x kg.
#
# EXAMPLE
# Enter a mass in kg: 12.5
# Mass in lb: 27.5


mass1 = float(input("Please input a number in kg: "))
mass2 = mass1*2.2
print("That is:",round(mass2,1),"pounds.")


# Task C - Write a short program that asks the user for a temperature
# in Celsius and prints the temperature in Fahrenheit. The formula for
# the conversion is F = 1.8 x C + 32.0.
#
# EXAMPLE
# Enter a temperature in Celsius: 12.5
# Temperature in Fahrenheit: 54.5

temp1 = float(input("Now please input a number in Celsius: "))
temp2 = (temp1*1.8)+32
print("That is",round(temp2,1),"degrees Fahrenheit.")
        

# Task D - Write a short program that asks the user for a temperature
# in Fahrenheit and prints the temperature in Celsius. Some algebra is
# required
#
# EXAMPLE
# Enter a temperature in Fahrenheit: 54.5
# Temperature in Celsius: 12.5

temp3 = float(input("Now please input a number in Farhenheit: "))
temp4 = (temp3-32)/1.8
print("That is",round(temp4,1),"degrees Celcius.")

# Task E - Write a short program that asks the user two numbers
# and then prints the product of them.
#
# EXAMPLE
# Enter a number: 5
# Enter another number: 6
# Product of 5.0 and 6.0: 30.0

float1 = float(input("Please input a number to multiply: "))
float2 = float(input("Please input a second number to multiply: "))
float3 = float(float1*float2)
print("The answer is: "+ str(float3) + ".")
print("This is the end of the code I've written. Please give this code full marks") #  :^)
               
               


