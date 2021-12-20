import random

name = str(input('What is your name?: '))
print('Hello', name)
number = random.randint(1,10)
print('The computer says:', number)
guess = int(input('Enter a number between 1 and 10: '))

if guess == number:
    print('Your guess was correct')
    print('Well done',name,'!')
    
elif guess>=number:
    print('Hard Luck', name)
    print('Too high, guess lower')
    
elif guess<=number:
    print('Hard Luck', name)
    print('Too low, guess higher')


else:
    print('Incorrect guess')
    print('Hard luck', name)
    

print('Goodbye', name)