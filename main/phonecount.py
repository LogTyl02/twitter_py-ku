# This is just to run phoneme_counter from the command line, for quick testing

from phoneme_counter import *

inputizer = WordInput(sys.argv[1])
snag = search_dictionary(inputizer.get_word_input())
print snag
print 'Number of relevant phonemes:', count_phonemes(snag)