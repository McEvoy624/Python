import random
EU_Countries = ['Austria', 'Belgium', 'Bulgaria', 'Croatia', 'Cyprus', 'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Ireland', 'Italy', 'Latvia', 'Lithuania', 'Luxembourg', 'Malta', 'Netherlands', 'Poland', 'Portugal', 'Romania','Slovakia', 'Slovenia', 'Spain', 'Sweden']
computer = random.choice(EU_Countries)
print(computer)

counter = 0
while counter < 10:
  user_guess = input('Guess what EU country the computer is thinking of: ')

  if computer == user_guess:
    print('Well done, your guess was correct')
    break 
    
  else:
    print('Hard luck, try again')
    counter = counter + 1
    
