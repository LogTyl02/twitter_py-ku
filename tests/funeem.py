# Phoneme Counter

pdic = open('CMelonphonemeEN.txt', 'r')

def search_dictionary(word):
    for line in pdic:
        if line.split()[0] == word.upper():
            return line.strip()
            

balloon = search_dictionary('balloon')

def count_phonemes(line):
    phoneme_count = 0
    for phoneme in line.split():
        if len(phoneme) == 2:
            phoneme_count += 1
            
    return phoneme_count
    
print count_phonemes(search_dictionary('scarecrow'))