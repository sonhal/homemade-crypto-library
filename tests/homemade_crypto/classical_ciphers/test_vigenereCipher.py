from unittest import TestCase

from homemade_crypto.classical_ciphers.vigenere_cipher import VigenereCipher


class TestVigenereCipher(TestCase):

    def test_gen_key(self):
        vigenere = VigenereCipher.norwegian_vigenere()
        key = vigenere.gen_key()
        self.assertIsInstance(key, str)
        self.assertTrue(len(key) > 0)




