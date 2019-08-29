import random

ASCII = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789'


class AffineCipher:
    VALID_A_VALUES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

    def __init__(self, key_space):
        self._key_space = list(key_space)
        self._valid_b_values = list(range(0, len(key_space)))
        self._m = len(self._key_space)

    @classmethod
    def ascii_affine(cls) -> "AffineCipher":
        return cls(ASCII)

    def gen_key(self):
        a = self.VALID_A_VALUES[random.randint(0, len(self.VALID_A_VALUES) - 1)]
        b = self._valid_b_values[random.randint(0, len(self._key_space) - 1)]
        return a, b

    def encrypt(self, key, plain_text: str):
        letters = list(plain_text.upper())
        a = key[0]
        b = key[1]
        cipher_list = []
        for letter in letters:
            new_index = (a * self._index_of_letter(letter) + b) % self._m
            cipher_list.append(self._key_space[new_index])
        return "".join(cipher_list)

    def _index_of_letter(self, letter):
        return self._key_space.index(letter)

    def decrypt(self, key, cipher_text):
        letters = list(cipher_text.upper())
        a = key[0]
        b = key[1]
        inverse = self._find_inverse(a)
        cipher_list = []
        for letter in letters:
            new_index = (inverse * (self._index_of_letter(letter) - b)) % self._m
            cipher_list.append(self._key_space[new_index])
        return "".join(cipher_list)

    def _find_inverse(self, a):
        """ 1 = aa^-1 mod m """
        for value in self._valid_b_values:
            if (a * value) % self._m == 1:
                return value
        raise AttributeError(f"a={a} is not a valid value")


