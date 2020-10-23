import string

class ReservedWords():
  def __init__(self):
    self.last_word = ""
    self.double_reserved = ["end main", "prompt for", "end for", "end while", "end if"]
    self.reserved_word = ["while", "if", "then", "let", "call", "else", "display", "for", "to", "main", "end", "define", "integer", "function"]
  
  def is_reserved_word(self, word):
    if not self.last_word == "":

      # Verificações para o caso de ser uma palavra reservada composta

      if self.last_word == "end":
        if word == "main" or word == "for" or word == "while" or word == "if":
          self.last_word = ""
          return [{"word": "end " + word, "className": "reserved"}]
        else:
          rtrn = [{"word": self.last_word, "className": "reserved"}]
          self.last_word = word
          return rtrn
      elif self.last_word == "prompt":
        if word == "for":
          self.last_word = ""
          return [{"word": "prompt " + word, "className": "reserved"}]
        else:
          rtrn = [{"word": self.last_word, "className": "notReserved"}]
          self.last_word = word
          return rtrn
      else:
        # Caso não caia em um dos ifs, então teremos que precessar a atual palavra (word)
        # e limpar a ultima palavra lida
        self.last_word = ""
        return self.is_reserved_word(word)
        

    if word == "end" or word == "prompt":
      # Verificando se é o começo de uma palavra reservada composta

      self.last_word = word

      # Retorno uma palavra não reservada e vazia, para não ser incluída na lista
      # Será necessário receber a próxima palavra para verificar se é uma composição
      return {"word": "", "className": "notReserved"}
    
    for rw in self.reserved_word:
      if rw == word:
        return [{"word": word, "className": "reserved"}]
    
    return [{"word": word, "className": "notReserved"}]

    

