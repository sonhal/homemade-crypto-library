from unittest import TestCase

from homemade_crypto.classical_ciphers.vigenere_cipher import VigenereCipher


class TestVigenereCipher(TestCase):

    def test_gen_key(self):
        vigenere = VigenereCipher.norwegian_vigenere()
        key = vigenere.gen_key()
        self.assertIsInstance(key, str)
        self.assertTrue(len(key) > 0)

    def test_encrypt(self):
        vigenere = VigenereCipher.norwegian_vigenere()
        key = "ABBA"
        plain_text = "LISAGÅRTILSKOLEN"
        cipher_text = vigenere.encrypt(key, plain_text)
        self.assertEqual("LJTAGASTIMTKOMFN", cipher_text)

    def test_decrypt(self):
        vigenere = VigenereCipher.norwegian_vigenere()
        key = "ABBA"
        plain_text = "LISAGÅRTILSKOLEN"
        cipher_text = vigenere.encrypt(key, plain_text)
        decrypted_text = vigenere.decrypt(key, cipher_text)
        self.assertEqual("LISAGÅRTILSKOLEN", decrypted_text)
