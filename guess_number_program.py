#this is a python guess-a-number computer program
#using the random module to help the computer pick
# any random number by the help of randint(a,b) function

from random import randint

num = randint(1,20)
guess = eval(input('Enter your Guess:'))
if guess == num:
    print('Congrats,You got it!')
else:
    print('Sorry,the number is', num)
    
#Results
#Enter your Guess:13
#Sorry,the number is 7  
#Enter your Guess:8
#Congrats,You got it!