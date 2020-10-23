from reserved_word import ReservedWords

class Classifier():

	def __init__(self):
		self.list_of_words = []
		

	def classificate_list(self, list_of_words):
		reserved_word = ReservedWords()
		for word in list_of_words:

			# Para a parte de verificação de reservada, olhar em ["className"] == "reserved"
			# fiz assim para facilitar caso fossemos usar em uma lista
			# retorno facilmente trocável
			print(reserved_word.is_reserved_word(word))
		
		