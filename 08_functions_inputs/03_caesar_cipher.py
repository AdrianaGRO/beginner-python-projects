"""
Caesar Cipher (Capstone)

Task:
Create a function that encodes and decodes messages using the Caesar Cipher technique.
- The function should accept a message, shift amount, and direction (encode/decode) as arguments.
- Shift each letter forward (encode) or backward (decode) by the shift amount, handling wrap-around for letters.
- Print the encoded or decoded message in the format:
  Here is the encoded/decoded result: X
  (where X is the result)

Example:
If you call the function with ('hello', 3, 'encode'), the output should be:
Here is the encoded result: khoor

Note:
For testing, use hard-coded values instead of input().
"""
from art_caesar_cipher import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar_cipher(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
            shift_amount *= -1
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")

cipher_loop = True

while cipher_loop:
    cipher_on = input("Do you want to use the program to encode/decode? Press 'y' for yes or 'n' for no: ")
    if cipher_on == 'y':
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar_cipher(original_text=text, shift_amount=shift, encode_or_decode=direction)

    if cipher_on == 'n':
        print("Have a nice day!")
        break
