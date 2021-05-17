import sys
from random import randint



start = int(sys.argv[1])
stop = int(sys.argv[2])
lol = int(sys.argv[3])
x = randint(start,stop)
print(f'guess the number in range from {start}, to {stop}')
if lol==x: 
	print('Good job u guessed rigt')
else: print(f'try again it was {x}')
