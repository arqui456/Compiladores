
from automaton import Automaton
from grammar import Grammar
from classifier import Classifier

def main():
	file_path = "arquivo_test2.c"
	grammar = Grammar()
	classifier = Classifier()
	automaton = Automaton(file_path, grammar, classifier)
	print(automaton.splitter.list_of_words)
if __name__ == '__main__':
	main()