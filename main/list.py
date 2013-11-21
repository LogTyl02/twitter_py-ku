apple = [{'mambo':'101010','text':"I'm small! I have adventures!"}]

class ListWizard():	

	def on_data(self, data):
		print data['text']
		return False

chunk = ListWizard()

chunk.on_data(apple)