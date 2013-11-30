# This is the main script for the creation of poems
# Handles dictionaries, syllables, disambiguation, construction and desconstruction of beautiful and terrible things.

import os
import sys

class FileHandler( object ):
	def __init__(self, lookupFile, gristFile, newPoemFile ):		# gristFile is the raw data we will process into beautiful poem things
		self.grist = open( os.path.join( 'data', gristFile), 'r' )
		self.syllable_dictionary = open( os.path.join( 'dictionaries', lookupFile ), 'r' )
		self.newPoem = open( os.path.join( 'output', newPoemFile ), 'r+' )

class NewPoem(object):
	def __init__(self):
		self.lineOne   = ''
		self.lineTwo   = ''
		self.lineThree = ''

	def checkSyllables(self):
		pass

class GruntWork(object):
	def __init__(self, data):
		self.data = data

	def makeNaked(self):
		self.lines = [i.strip("',.!?\n") for i in self.data]
		self.naked = [i.split() for i in self.lines]
		return self.naked

	def process(self):
		self.processed = [line.split()]

	def packLines(self):
		self.packedLines = [x.strip(',.!').lower() for word in self.makeNaked() for x in word]		# This is some serious list comprehension shenanigans, and I love it.
		return self.packedLines

	def countSyllables(self, pack):
		self.pack = pack
		for line in f.syllable_dictionary:
			for i in self.packLines():
				if i.upper() in line:
					print line

class Grist(object):
	pass

f = FileHandler('tyler_syllable.txt', 'basho.txt', 'output.txt')

grunt = GruntWork(f.grist)

a = grunt.packLines()

#for line in f.syllable_dictionary:
#	for word in a:
#		if word.upper() in line:
#			print line

b = f.syllable_dictionary

for line in b:
	for word in line.split():
		print word[0]