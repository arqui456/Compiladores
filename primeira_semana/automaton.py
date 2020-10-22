from splitter import Splitter

class Automaton():

	def __init__(self, input, grammar, classifier):
		self.splitter = Splitter(input, grammar)
		self.splitter.split()
