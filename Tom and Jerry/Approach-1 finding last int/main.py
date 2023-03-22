# Tom and Jerry were playing a game. Jarvis had to enter a number for them, but Jarvis can only generate machine language. Soon after Jarvis generate a number, he performed an operation which was as follows:
# He would convert the generated number to decimal and perform an operation in which he checks whether the decimals are multiples of 2, If so Tom wins else Jerry wins.
# The game was successful so they decided to create a program but all of them were weak in programming. Their code had a lot of errors. Help Tom and Jerry to rectify the errors.
# Input
# First line must contain T (how many times there are playing the game)
# Followed by the numbers Jarvis inserted (n)
# Constraints
# 0<=T<=10^5
# 0<=n<=10^5
# Output
# Print tom if Tom wins and jerry if jerry wins.
# Sample input:
# 3
# 1111
# 011000
# 100
# Sample output:
# jerry
# tom
# tom

n=int(input()) #no of cases
for _ in range(n):
    num=input()
    if num[-1]=='0':print('tom')
    else:print('jerry')

