from phoneme_counter import *

sentence = 'This poor grass-roofed hut of old brushwood may sound miserable, but I very quickly found it altogether suiting my taste.'

def cleanup(sentence):
	return [i.strip(',.') for i in sentence.split()]

a = cleanup(sentence)

#for line in pdic:
#	for i in a:
#		if line.split()[0] == i.upper():
#			print line.strip()

def is_in(entry, dictionary):
	if entry in dictionary:
		print 'True'
		return True
	else:
		print 'False'
		return False


for line in pdic:
	for i in a:
		if line.split()[0] == i.upper():
			print i, 'True'
		else:
			print i, 'False'