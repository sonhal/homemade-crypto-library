import random

ASCII = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
NOR = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÆÅ'


class VigenereCipher:

    def __init__(self, key_space):
        self._key_space = key_space

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