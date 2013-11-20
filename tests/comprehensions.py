sentence = 'This poor grass-roofed hut of old brushwood may sound miserable, but I very quickly found it altogether suiting my taste.'

def obliterate(line):
	words = line.split()
	obliteration = [[w.upper(), w.lower(), len(w)] for w in words]

	return obliteration

# Test

out = obliterate(sentence)
print out