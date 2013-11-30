from syllable_test import *
from phoneme_counter import *

class FileHandler():
	def __init__(self, input_file, input_mode, output_file, output_mode):
		self.input_file = input_file
		self.input_mode = input_mode
		self.output_file= output_file
		self.output_mode= output_mode

		self.input_contents = open(str(self.input_file), str(self.input_mode))
		self.output_contents= open(str(self.output_file), str(self.output_mode))

	def dump_input_contents(self):
		if self.output_mode == 'r' or 'r+':
			print self.input_contents.readlines()
		else:
			print 'File not open in reading mode!'

	def dump_output_contents(self):
		if self.output_mode == 'r' or 'r+':
			print self.output_contents.readlines()
		else:
			print 'File not open in reading mode!'

	def write_out(self, raw_lines):
		for i in raw_lines:
			if i != '\n':
				self.output_contents.write(i)
				
	def lines_to_list(self, raw_lines):
	    self.line_list = []
	    for i in raw_lines:
	        if i!= '\n':
	            self.line_list.append(i.strip())
	    return self.line_list


class Poemerizer(object):
    def __init__(self, raw_data):
        self.data = raw_data
        
    def data_to_lines(self, data):
       for i in data:
           return i
        
    def obliterate(self, line_list):
	self.words = str(line_list[0]).split()
	obliteration = [{'Word: ':w.upper(), 'Length: ':len(w), 'Syllables: ':count_phonemes(w)} for w in self.words]

	return obliteration

f_handler = FileHandler('basho.txt', 'r', 'output.txt', 'w')
basho_list = f_handler.lines_to_list(f_handler.input_contents)

bashorizer = Poemerizer(basho_list)

print bashorizer.obliterate(bashorizer.data)
