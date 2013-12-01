# This is the main script for the creation of poems
# Handles dictionaries, syllables, disambiguation, construction and desconstruction of beautiful and terrible things.

import os
import sys
from phoneme_counter import *

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

	def countSyllables(self, pack):               # THIS DOES NOTHING YET. 
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

for i in a:
	if i != None:		# Testing
		print i, count_phonemes(search_dictionary(i.strip()))	# These functions are part of the phoneme_counter file.
		pdic.seek(0)	# This trick sets the pointer back at the beginning of the file so it can search through it again.
	else:
		pdic.seek(0)
		continue






