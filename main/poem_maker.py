# This is the main script for the creation of poems
# Handles dictionaries, syllables, disambiguation, construction and desconstruction of beautiful and terrible things.

import os
import sys

class FileHandler(object):
	def __init__(self, lookupFile, newPoemFile, gristFile):		# gristFile is the raw data we will process into beautiful poem things
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
	pass

class Grist(object):


f = FileHandler('tyler_syllable.txt', 'output.txt')


