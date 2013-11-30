# PHONEME COUNTER!!

import os
import sys

class WordInput():
    def __init__(self, word_input):
        self.word_input = word_input
        
    def get_word_input(self):
        return str(self.word_input)

pdic = open('CMelonphonemeEN.txt', 'r')

def search_dictionary(word):
        for line in pdic:
            if line.split()[0] == word.upper():
                return line.strip()
                
def count_phonemes(line):
    vowels = ['A','E','I','O','U']
    phoneme_count = 0
    for phoneme in line.split():
        if len(phoneme) == 2 and phoneme[0] in vowels:
            phoneme_count += 1
            
    return phoneme_count
                

#inputizer = WordInput(sys.argv[1])
#snag = search_dictionary(inputizer.get_word_input())
#print snag
#print 'Number of relevant phonemes:', count_phonemes(snag)
