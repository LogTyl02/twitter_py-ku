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
        for line in pdic.readlines():
            if line.split()[0] == word.upper():
                return line.strip()
                
def count_phonemes(line):
    vowels = ['A','E','I','O','U']
    phoneme_count = 0
    if line != None:
        if len(line.split()[0]) == 2:
            phoneme_count -= 1
        for phoneme in line.split():
            if len(phoneme) == 2 and phoneme[0] in vowels: #OMFG... Of course it counts the first thing in the list. So two letter words, like 'of', will count itself, making the count go up
                phoneme_count += 1

                # Apparently it won't find 'squints', but it finds 'squint'. Yet another stupid thing to account for.


    return phoneme_count