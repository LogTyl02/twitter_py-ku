# PHONEME COUNTER!!

import os
import sys


unconj = None
ambiguated_compound = None

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
                pdic.seek(0)

def disambiguate(word):
    unconj = None
    ambiguated_compound = None
    print "Is", word, "a word you recognize?"
    answer = raw_input()
    if answer == 'yes':
        answer = ''
        print "Is", word, "a conjugation of another word?"
        answer = raw_input()
        if answer == 'yes':
            answer = ''
            print "Please enter the un-conjugated word"
            unconj = raw_input().upper()
            print unconj
        else:
            answer = ''
            print "Is", word, "a compound?"
            answer = raw_input()
            if answer == 'yes':
                print "First word:"
                first_word = raw_input().upper()
                print "Second word:"
                second_word = raw_input().upper()
                answer = ''
                ambiguated_compound = [first_word, second_word]
                print ambiguated_compound
    else:
        print 'Ignoring...'

    if unconj: 
        return unconj
    
    if ambiguated_compound:
        return ambiguated_compound


        
                
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