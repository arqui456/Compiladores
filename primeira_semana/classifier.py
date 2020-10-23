from reservedWords import ReservedWords

class Classifier():

	def __init__(self):
		self.list_of_words = []
		pass

	def classificateList(self, list_of_words):
		reservedWord = ReservedWords()
		for word in list_of_words:

			# Para a parte de verificação de reservada, olhar em ["className"] == "reserved"
			# fiz assim para facilitar caso fossemos usar em uma lista
			# retorno facilmente trocável
			print(reservedWord.isReservedWords(word))
		
		