#!/usr/bin/python3

import random

elem = ['paper', 'rock', 'scissors']

print('Enter paper, rock or scissors ')

player_choice = input()
bot_choice = elem[random.randint(0,2)]

if player_choice == bot_choice:
	print('Enemy choice was ' + bot_choice + ' ,it`s a draw')
elif player_choice == 'paper' and bot_choice == 'rock':
	print('Enemy choice was ' + bot_choice + ' ,you win!')
elif player_choice == 'paper' and bot_choice == 'scissors':
	print('Enemy choice was ' + bot_choice + ' ,you loos!')
elif player_choice == 'rock' and bot_choice == 'paper':
	print('Enemy choice was ' + bot_choice + ' ,you loos!')
elif player_choice == 'rock' and bot_choice == 'scissors':
	print('Enemy choice was ' + bot_choice + ' ,you win!')
elif player_choice == 'scissors' and bot_choice == 'paper':
	print('Enemy choice was ' + bot_choice + ' ,you win!')
elif player_choice == 'scissors' and bot_choice == 'rock':
	print('Enemy choice was ' + bot_choice + ' ,you loos!')
else:
	print('you enter incorrect value')