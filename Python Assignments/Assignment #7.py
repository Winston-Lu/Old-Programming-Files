# Assignment 7
# Name: Winston Lu
# Block: 1-4
# Date: Jan 27 2017

# Write a program called guessGame(n = 10). It will ask the user
# to guess a number between 1 and n. If the user enters a number
# less than the correct number, it will tell the user to guess a
# larger number. If the number is larger than the correct number,
# it will tell the user to guess a smaller number. If the number
# is correct, the game ends with a congratulations message and
# the total number of guesses. Any non-numeric input does not
# count as a guess byt ab errir message is displayed.





def guessGame(n=10):
    import random
    random.seed(random.random())
    num = random.randint(1,n)
    guesses = 1
    grammar = ''
    while True:
        try:
            guess = int(input('Guess a number between 1 to ' + str(n) +': '))
            if (guess > num):
                print('My number is lower, try a smaller number.')
                guesses += 1
            elif(guess < num):
                print('My number is higher, try a larger number.')
                guesses += 1
            elif(guess == num):
                if (guesses > 1):
                    grammar = 's'
                print('You guessed my number "'+ str(num) +'" in', guesses, 'attempt' + grammar + '!')
                return
        except:
            print('Please enter a number')


guessGame()
