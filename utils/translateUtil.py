import re
from .fileUtil import create_translate_file

alphabet = {
    0: "A",
    1: "B",
    2: "C",
    3: "D",
    4: "E",
    5: "F",
    6: "G",
    7: "H",
    8: "I",
    9: "J",
    10: "K",
    11: "L",
    12: "M",
    13: "N",
    14: "O",
    15: "P",
    16: "Q",
    17: "R",  
    18: "S",
    19: "T",
    20: "U",
    21: "V",
    22: "W",
    23: "X",
    24: "Y",
    25: "Z"
}

alphabet_inv = {v: k for k, v in alphabet.items()}

def caesar_encrypt(key: int, alphabet: dict, letter: str) -> str:
    letter_index = alphabet_inv[letter]
    new_index = (letter_index - key) % 26
    return alphabet[new_index]

def append_translate_to_text(translate_text: str, key: int, alphabet: dict, letter: str) -> str:
    translate_text += caesar_encrypt(key, alphabet, letter)
    return translate_text    

def translate(encrypted_text: str, alphabet: dict, key: int) -> str:
    text = ""
    for char in encrypted_text:
        if re.search(r'\.|\s|\n|,|-', char):
            text += char  # Corrected 'new_text' to 'text'
        else:
            text = append_translate_to_text(text, key, alphabet, char)  # Added 'char' argument and assigned the return value
    return text

def translate_with_diffrent_keys(encrypted_text: str):
    for key in range(1, 26):
        text = translate(encrypted_text, alphabet, key)
        create_translate_file(key, text)
