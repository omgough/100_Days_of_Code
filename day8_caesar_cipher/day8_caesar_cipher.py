# from art import logo # ASCII art in course material 
# print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1 # if decoding we change direction by multiplying by -1
  for char in start_text: # to handle characters that aren't letters in alphabet (i.e. symbols and numbers)
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char    
  print(f"Here's the {cipher_direction}d result: {end_text}")

should_cont = True # statement to determine whether the program should run again or stop, based on user input
while should_cont:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26 # means the program can handle any number above 26, modulo gives remainder
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction) # calling function with user inputs
  result = input("Type 'yes' if you'd like to run the program again. Type 'no' to finish. \n")
  if result == 'no':
    should_cont = False 
    print("Thanks for using - goodbye!")