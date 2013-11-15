from syllable_test import *

strip_list = [',', '.', '-', '!']

line_list = []
line = ''
word_list = []
word = ''

parse_fodder = open('basho.txt', 'r')

for line in parse_fodder:
    if line != '\n':
        words = line.split()
        for i in words:
            if i != '\n':
                print i.rstrip(str(strip_list)) + ' ' + str(CountSyllables(i))
                
        
        