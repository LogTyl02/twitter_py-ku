# Just testing to see if I can make random poems from lines.

import random

line_list = []

poem_lines = open('basho.txt', 'r')

for line in poem_lines:
	if not '#' in line and line != '\n':
		line_list.append(line.rstrip('\n').rstrip(',').rstrip(':').rstrip('.'))

for i in range(3):
	print random.choice(line_list)