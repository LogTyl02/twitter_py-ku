class FileHandler():
	def __init__(self, filename):
		self.contents = open(filename, 'r+')

	def dump(self):
		for line in self.contents:
			print line

poem = FileHandler('poem.txt')

poem.dump()
