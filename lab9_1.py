#!/usr/bin/env python3

import random

card_dict = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':10,'Q':10,'K':10,'A':[1,11]}

def generate_start_game() -> list:
	#function generate start score from 2 random card and return list with score first and second players
	i=0
	j=0
	score = [0,0]
	while i < 4:
		random_key = random.choice(list(card_dict.keys()))
		if random_key == 'A':
			if score[j] <= 10:
				score[j] += card_dict.get(random_key)[1]
			else:
				score[j] += card_dict.get(random_key)[0]
		else:
			score[j] += card_dict.get(random_key)
		if i == 1:
			j += 1
		i+=1
	return score

def add_card(player_score:int) -> int:
	#function accepts plater score, add point from 1 random card and return this result
	random_key = random.choice(list(card_dict.keys()))
	if random_key == 'A':
		if player_score <= 10:
			player_score += card_dict.get(random_key)[1]
		else:
			player_score += card_dict.get(random_key)[0]
	else:
		player_score += card_dict.get(random_key)

	return player_score




def game_process() -> str:
	player1_score,player2_score = generate_start_game() #generate start score

	first_player = True
	second_player = True
	#loop for question add card or stop for 1 player
	while first_player:
		print('player 1 score is - {}'.format(player1_score))
		print('player 2 score is - {}'.format(player2_score))
		state = input('player 1 write stop or add - ')
		#check what player chose
		if state == 'add':
			player1_score = add_card(player1_score)
		elif state == 'stop':
			first_player = False
		else:
			print('unknown state, try again')
		if player1_score > 21:
			player1_score = 'BUST'
			first_player = False
			second_player = False
	#loop for question add card or stop for 2 player
	while second_player:
		print('player 1 score is - {}'.format(player1_score))
		print('player 2 score is - {}'.format(player2_score))
		state = input('player 2 write stop or add - ')
		#checks what player chose
		if state == 'add':
			player2_score = add_card(player2_score)
		elif state == 'stop':
			second_player = False
		else:
			print('unknown state, try again')
		if player2_score > 21:
			player2_score = 'BUST'
			second_player = False

	print('player 1 score is - {}'.format(player1_score))
	print('player 2 score is - {}'.format(player2_score))
	#checks players score and return result according to got results
	if player1_score == 'BUST':
		return 'player 2 - WIN'
	elif player2_score == 'BUST':
		return 'player 1 - WIN'

	if player1_score < player2_score:
		return 'player 2 - WIN'
	elif player1_score == player2_score:
		return 'it`s a draw'
	else:
		return 'player 1 - WIN'


print(game_process())