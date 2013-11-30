
phoneme_dictionary = open('CMelonphonemeEN.txt', 'r')

syllable_dictionary = open('tyler_syllable.txt', 'r+')

def count_phonemes(line):
	vowels = ['A', 'E', 'I', 'O', 'U']
	phoneme_count = 0
	for phoneme in line.split():
		if len(phoneme) == 2 and phoneme[0] in vowels:
			phoneme_count += 1
	return phoneme_count


for line in phoneme_dictionary:
	if line.split()[0][-1] != ')':
		syllable_dictionary.write(line.split()[0] + ' ' + str(count_phonemes(line)) + '\n')



