import random

f = open('paz.txt', 'r')

class Grist(object):
	def __init__(self, file):
		self.raw_data = [i.strip('.,;"\n') for i in file]
		for line in self.raw_data:
			if line == '' or line == '\n':
				del self.raw_data[self.raw_data.index(line)]
		self.prime_lines = []
		self.primer()

	def get_raw(self):
		if self.raw_data:
			return self.raw_data

	def primer(self):
		for line in self.raw_data:
			count = 0
			for char in line:
				if char != ' ':
					count += 1
			if count >= 2:
				for i in range(2, count):
					if count % i == 0:
						break
					else:
						continue
				else:
					self.prime_lines.append(line)


	def build_poem(self, lines=3):
		for i in range(lines):
			print self.build_complex_line()

        def build_complex_line(self):
            seed = random.choice(self.raw_data)
            flower = random.choice(self.raw_data)
            seed = seed.split()
            seed[-1] = flower.split()[-1]
            return ' '.join(seed)

        def rend_fluff(self):
            fluffy_line = random.choice(self.raw_data).split()
            strong_line = []
            for word in fluffy_line:
                if word == 'the' or word == 'The':
                    fluffy_line.remove(word)
            return fluffy_line
                
        def clean_singleton(self, line):
            pass

        def last_three(self, line):
            if len(line) >=3:
                phrase = [line[-1], line[-2], line[-3]]
            else:
                phrase = line
            return phrase
                

	def prime_poem(self, lines=3):
		self.pp = []
		for i in range(lines):
			if i not in self.pp:
				self.pp.append(random.choice(self.prime_lines))

		for line in self.pp:
			print line.capitalize()

class Codex(object):
	def __init__(self, source):
		self.source = source

	def get(self):
		print self.source

	def make_dict(self):
		self.word_count = {}
		for line in self.source:
			for word in line.split():
				if word not in self.word_count:
					self.word_count.update({word:1})
				elif word in self.word_count:
					self.word_count[word] += 1
		return self.word_count

	def dict_tuple(self):
		for i in self.make_dict().iteritems():
			print i
			

octavio = Grist(f)

test = [word.strip(',.:;-!').upper() for line in octavio.raw_data for word in line.split() if len(word) > 3]
from phoneme_counter import *

def count_em_all():
	for word in test:
		print word, "has", count_phonemes(search_dictionary(word)), "syllables!"
		pdic.seek(0)

#octavio.build_poem(3)


#print octavio.rend_fluff()
#print octavio.last_three(octavio.rend_fluff())

octavio.prime_poem(5)	# Builds a poem using only lines that have a prime number of chars

# count_em_all()			# Returns syllable counts for every word
