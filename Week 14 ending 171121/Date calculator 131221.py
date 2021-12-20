from datetime import date
DatePuppyWasReceived = date(input('Enter the date that you received your pet(yyyy/mm/dd): '))
#DatePuppyWasReceived = date(2014, 11, 2)
DateNow = date(input('What date is it today?(yyyy/mm/dd): '))
#DateNow = date(2014, 12, 3)
Length = DateNow - DatePuppyWasReceived
print('You got your pet',Length.days,'days ago')