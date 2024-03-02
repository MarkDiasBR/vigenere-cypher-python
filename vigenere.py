def vigenere(message, key, direction=1):
  key_index = 0 #índice que vai percorrer a chave
  alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
  final_message = '' #string que será retornada

  for char in message:

      # Se o caractere não for uma letra, ele é adicionado "as is" na string
      if not char.isalpha() and not char.isnumeric():
          final_message += char
      else:        
          # Encontrar a posição 
          key_char = key[key_index % len(key)] 
          key_index += 1

          # Define the offset and the encrypted/decrypted letter
          offset = alphabet.index(key_char) #entra a letra da key, sai o seu index
          index = alphabet.find(char) #entra a letra do text, sai seu índice
          new_index = (index + offset*direction) % len(alphabet)
          final_message += alphabet[new_index]

  print('Vigenère Cypher\n\nAlphabet: ' + alphabet + '\n\nKey: ' + key)
  operation = ''
  if direction == 1:
    operation += 'encryption'
  else:
    operation += 'decryption'
  print('\n\nOperation: ' + operation + '\nInput message: ' + message + '\nOutput message: ' + final_message)


  return final_message

def encrypt(message, key):
  return vigenere(message, key)

def decrypt(message, key):
  return vigenere(message, key, -1)

vigenere('Secret Message #01', 'a143fFfFffgf4664gG')
#output: 'S56kjY RJxxgl8 #WX'

vigenere('S56kjY RJxxgl8 #WX', 'a143fFfFffgf4664gG', -1) 
#should output: 'Secret Message #01' and it does!
