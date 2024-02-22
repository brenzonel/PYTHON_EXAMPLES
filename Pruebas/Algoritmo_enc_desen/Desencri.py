import string

def desencrypt (text, shift):
    
    desencrypted_text = list(range(len(text)))

    alphabet = string.ascii_lowercase

    first_half = alphabet[:shift:]
    second_half = alphabet[shift:]

    shifted_alphabet = second_half+first_half

    for i, letter in enumerate(text.lower()):
        if letter in alphabet:
            index = shifted_alphabet.index(letter)
            original_letter = shifted_alphabet[index]
            desencrypted_text[i] = original_letter
        else:
            desencrypted_text[i] = letter

    return ''.join(desencrypted_text)

texto = 'hola'
print(texto)
print(desencrypt(texto,2))