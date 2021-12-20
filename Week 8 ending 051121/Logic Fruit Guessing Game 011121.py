import random

fruit = ['apple', 'banana', 'strawberry', 'orange', 'pineapple']
answer = random.choice(fruit)
#print(answer)

guess = str(input('Enter a random fruit: '))
print(answer)

if guess == answer:
    print('Your guess was correct')
    print('Well Done')
    
elif guess != answer:
        print('Your guess was wrong')
        print('Unlucky')
    
print('Goodbye')