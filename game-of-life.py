import numpy as np
import random
import itertools
import os


def initialize_board(x,y):
	board = np.zeros([x,y])

	for i in range(1, x-1):
		for j in range(1, y-1):
			board[i,j] = random.randint(0,1)

	return board


def next_gen(board):
	next_board = np.zeros(board.shape)

	for i in range(1, next_board.shape[0]-1):
		for j in range(1, next_board.shape[1]-1):
			total_sum = check_sum(i, j, board)
			next_board[i, j] = new_value(total_sum, current_value=board[i,j])

	return next_board


def check_sum(i, j, board):
	total_sum = 0

	for comb in itertools.product([0,1,-1], repeat=2):
		total_sum += board[i+comb[0], j+comb[1]]

	total_sum -= board[i,j]

	return total_sum


def new_value(n, current_value):
	if n < 2:
		return 0
	elif n == 2:
		return current_value
	elif n == 3:
		return 1
	else:
		return 0


if __name__ == '__main__':
	board = initialize_board(6,6)

	for x in range(5):
		board = next_gen(board)
		print board
		print "\n"
