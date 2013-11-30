# Is an unrecognized word a compound word?
# Valid compound forms are: hyphenated, as in 'Grass-roofed', in which case we should split at the hyphen and treat as two words, or 'Brushwood', which also can be split,
# but in some cases may be harder to disambiguate.


class Ambiguous(object):
	is_hyphenated = None

	def __init__(self, word):
		self.word = word
		if '-' in self.word:
			print self.word, 'is hyphenated'
			print 'Attempting to split hyphenated word...'
			self.hyphen_two(self.word)
			# Now stick that back into the line
		else:
			print self.word, 'is not hyphenated'
			self.is_hyphenated = False

	def hyphen_two(self, word):		# Takes a hyphenated word and makes it into two separate words
		print word.split('-')
	

grass = Ambiguous('grass-roofed')
wood  = Ambiguous('brushwood')
