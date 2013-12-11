import os
import sys

source = open('CMelonphonemeEN.txt', 'r')

class Counter(object):
	def __init__(self, words):
		self.words = words

		if type(self.words) == list:
			self.input_is_list = True
		else:
			if type(self.words) == str:
				self.input_is_string = True

	def search(self, word):
		source.seek(0)
		for line in source.readlines():
			if line.split()[0] == self.words.upper():
				return line.strip()
				source.seek(0)
			else:
				source.seek(0)
				ambi = self.words.upper()
				fix_me = Ambiguous(ambi)

				fix_me.disambiguate()
				if fix_me.is_compound:
					for compound in fix_me.compound_list:
						print self.search(compound)
				else:
					pass

class Ambiguous(object):
	def __init__(self, word):
		self.word = word
		self.is_compound = False
		self.is_conjugation = False

		self.compound_list = None

	def disambiguate(self):
		print "Is", self.word, "a compound?"
		self.answer = raw_input()

		if self.answer == 'yes':
			#self.is_compound = True
			return self.split_compound(self.word)

		else:
			return None


	def split_compound(self, word):
		print "Splitting", word
		self.first_word = raw_input('First Word: ')
		self.second_word = raw_input('Second Word: ')

		self.compound_list = [self.first_word, self.second_word]
		return self.first_word

s = Counter('hatterfolly')
s.search('hatterfolly')