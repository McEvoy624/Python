#String Concatenation
#word1 = '4'
#word2 = '3'


#subject = word1 + word2
#print(subject)
#the result will be 43 as python sees 4 and 3 as string not numbers

#How to make python see that as numbers

#word1 = 4
#word2 = 3

#Answer = word1 + word2
#print(Answer)
#if you take away the quotation marks it automatically sees the numbers not string
#another technique is called casting (see below)

word1 = float(4)
word2 = float(3)

subject = word1 + word2
print(subject)