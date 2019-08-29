import random

ASCII = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
NOR = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÆÅ'


class CaesarCipher:
    """ Implementation of the Caeser Cipher"""

    def __init__(self, key_space):
        self._key_space = list(key_space)
        self._m = len(self._key_space)

    @classmethod
    def norwegian_caesar(cls) -> "CaesarCipher":
        return CaesarCipher(NOR)

    @classmethod
    def ascii_caesar(cls) -> "CaesarCipher":
        return CaesarCipher(ASCII)

    def gen_key(self):
        return random.randint(1, self._m)

    def encrypt(self, key, plain_text: str):
        letter_list = list(plain_text.upper())
        cipher_letter_list = []
        for letter in letter_list:
            letter_index = self._key_space.index(letter)
            new_letter_index = (letter_index + key) % self._m
            cipher_letter_list.append(self._key_space[new_letter_index])
        return "".join(cipher_letter_list)

    def decrypt(self, key, cipher_text):
        return self.encrypt(-key, cipher_text)


