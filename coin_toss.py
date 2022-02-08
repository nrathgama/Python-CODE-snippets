import random 

def coin_flip():
	return random.choice(['heads', 'tails'])

if coin_flip() == 'tails':
	print('Heads - You win!')
else:
	print('Tails - You lose!')
