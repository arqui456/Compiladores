import string

list_of_spaces = [" ", "\n", "\t"]
list_of_compound = ["<=", "<>", ">=", "=="]
list_of_simple = ["<", ">", "=", "+", "-", "*",
                  "/", "(", ")", ":", ",", ";", ".", "{", "}"]
list_of_characters = list(string.ascii_lowercase)
list_of_digits = list(string.digits)

file_path = "arquivo_test2.c"

file = open(file_path, 'r')
file_lines = file.readlines()

list_of_words = []

for line in file_lines:
    word = ""
    i = 0
  
    while i < (len(line)):
        
        # se leu um espaço
        if line[i] in list_of_spaces and word != "":
            list_of_words.append(word)
            word = ""
        # se leu um delimitador composto
        elif i != len(line) - 1 and (line[i] + line[i+1]) in list_of_compound:
            if word == "":
               list_of_words.append(line[i] + line[i+1])
            else: 
               list_of_words.append(word)
               word = ""
               list_of_words.append(line[i] + line[i+1])
            i = i + 1
        # se leu um delimitador simples
        elif line[i] in list_of_simple:
           
            if word == "":
               list_of_words.append(line[i])
            else: 
               list_of_words.append(word)
               word = ""
               list_of_words.append(line[i])
        # se leu uma letra
        elif line[i] in list_of_characters:
            word = word + line[i]
        # se leu um número
        elif line[i] in list_of_digits:
            word = word + line[i]
        
        i = i + 1
    
            
print(list_of_words)
        

file.close()


