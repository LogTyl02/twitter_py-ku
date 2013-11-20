from syllable_test import *

sentence = 'This poor grass-roofed hut of old brushwood may sound miserable, but I very quickly found it altogether suiting my taste.'

def obliterate(line):
	words = line.split()
	obliteration = [{'Word: ':w.upper(), 'Length: ':len(w), 'Syllables: ':CountSyllables(w)} for w in words]

	return obliteration

# Test

shiva = obliterate(sentence)

for i in shiva:
	print i
