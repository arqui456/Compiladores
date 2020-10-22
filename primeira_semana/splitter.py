import string

class Splitter():

    def __init__(self, file_path, grammar):
        self.list_of_characters = list(string.ascii_lowercase)
        self.list_of_digits = list(string.digits)
        self.file_path = file_path
        self.grammar = grammar
        self.list_of_words = []

    def split(self):
        with open(self.file_path, 'r') as file:
            file_lines = file.readlines()
            list_of_words = []
            for line in file_lines:
                word = ""
                i = 0
                while i < (len(line)):
                    # se leu um espaço
                    if line[i] in self.grammar.LIST_OF_SPACES and word != "":
                        list_of_words.append(word)
                        word = ""
                        # se leu um delimitador composto
                    elif i != len(line) - 1 and (line[i] + line[i+1]) in self.grammar.LIST_OF_COMPOUND:
                        if word == "":
                            list_of_words.append(line[i] + line[i+1])
                        else:
                            list_of_words.append(word)
                            word = ""
                            list_of_words.append(line[i] + line[i+1])
                        i += 1
                    # se leu um delimitador simples
                    elif line[i] in self.grammar.LIST_OF_SIMPLES:
                        if word == "":
                            list_of_words.append(line[i])
                        else:
                            list_of_words.append(word)
                            word = ""
                            list_of_words.append(line[i])
                    # se leu uma letra
                    elif line[i] in self.list_of_characters:
                        word = word + line[i]
                    # se leu um número
                    elif line[i] in self.list_of_digits:
                        word = word + line[i]
                    i += 1
            self.list_of_words = list_of_words
