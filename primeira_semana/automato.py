import string

list_of_spaces = [" ", "\n", "\t"]
list_of_compound = ["<=", "<>", ">=", "=="]
list_of_simple = ["<", ">", "=", "+", "-", "*",
                  "/", "(", ")", ":", ",", ";", "."]
list_of_characters = list(string.ascii_lowercase)
list_of_digits = list(string.digits)

#file_path = input("Digite o caminho absoluto do arquivo:")

file_path = "/home/john/Desktop/Compiladores/atividades/arquivo_test.c"

file = open(file_path, 'r')
file_lines = file.readlines()

list_of_words = []

for line in file_lines:
    word = ""
    i = 0
  
    while i < (len(line)):
        
        if line[i] in list_of_spaces and word != "":
            list_of_words.append(word)
            word = ""
        elif i != len(line) - 1 and (line[i] + line[i+1]) in list_of_compound:
            if word == "":
               list_of_words.append(line[i] + line[i+1])
            else: 
               list_of_words.append(word)
               word = ""
               list_of_words.append(line[i] + line[i+1])
            i = i + 1
        elif line[i] in list_of_simple:
           
            if word == "":
               list_of_words.append(line[i])
            else: 
               list_of_words.append(word)
               word = ""
               list_of_words.append(line[i])
               
        elif line[i] in list_of_characters:
            word = word + line[i]
        elif line[i] in list_of_digits:
            word = word + line[i]
        
        i = i + 1
    
            
print(list_of_words)
        

file.close()


