import random
import itertools

ASCII = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
NOR = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÆÅ'


class VigenereCipher:

    def __init__(self, key_space):
        self._key_space = list(key_space)
        self._m = len(key_space)

    @classmethod
    def norwegian_vigenere(cls) -> "VigenereCipher":
        return cls(NOR)

    @classmethod
    def ascii_vigenere(cls) -> "VigenereCipher":
        return cls(ASCII)

    def gen_key(self):
        key_length = random.randint(1, len(self._key_space) - 1)
        pick_space = list(self._key_space)
        random.shuffle(pick_space)
        return "".join(pick_space[:key_length])

    def encrypt(self, key, plain_text: str) -> str:
        key = key.upper()  # make sure key does not contain lower case
        letters = list(plain_text.upper())
        key_letter_pair = list(zip(letters, itertools.cycle(key)))
        cipher_list = []
        for letter, key_letter in key_letter_pair:
            letter_index = self._key_space.index(letter)
            key_letter_index = self._key_space.index(key_letter)
            cipher_letter_index = (letter_index + key_letter_index) % self._m
            cipher_list.append(self._key_space[cipher_letter_index])
        return "".join(cipher_list)

    def decrypt(self, key, cipher_text):
        key = key.upper()  # make sure key does not contain lower case
        letters = list(cipher_text.upper())
        key_letter_pair = list(zip(letters, itertools.cycle(key)))
        cipher_list = []
        for letter, key_letter in key_letter_pair:
            letter_index = self._key_space.index(letter)
            key_letter_index = self._key_space.index(key_letter)
            cipher_letter_index = (letter_index - key_letter_index) % self._m
            cipher_list.append(self._key_space[cipher_letter_index])
        return "".join(cipher_list)
