def encrypt(text, shift):
    for char in text:
        if char in alphabet:
            original_index = alphabet.index(char)
            new_index = (original_index + shift) % len(alphabet)
            print(alphabet[new_index], end="")
        else:
            print(char, end="")
encrypt(text, shift)