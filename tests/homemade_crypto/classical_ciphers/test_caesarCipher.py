import unittest

from homemade_crypto.classical_ciphers.ceasar_cipher import CaesarCipher, ASCII, NOR


class CaesarCipherTest(unittest.TestCase):

    def test_gen_key(self):
        caesar = CaesarCipher(ASCII)
        self.assertIsInstance(caesar.gen_key(), int)
        self.assertTrue(caesar.gen_key() < 29)
        self.assertTrue(caesar.gen_key() > 0)

    def test_encrypt(self):
        plain_text = "LISAGÅRTILSKOLEN"
        caesar = CaesarCipher.norwegian_caesar()
        key = 2
        cipher_text = caesar.encrypt(key, plain_text)
        self.assertEqual("NKUCIBTVKNUMQNGP", cipher_text)

        plain_text = "MARKWALKSTOSCHOOL"
        caesar = CaesarCipher.ascii_caesar()
        key = 26 + 2
        cipher_text = caesar.encrypt(key, plain_text)
        self.assertEqual("OCTMYCNMUVQUEJQQN", cipher_text)

    def test_decrypt(self):
        plain_text = "LISAGÅRTILSKOLEN"
        caesar = CaesarCipher.norwegian_caesar()
        key = 2
        cipher_text = caesar.encrypt(key, plain_text)
        self.assertEqual(plain_text, caesar.decrypt(key, cipher_text))


if __name__ == '__main__':
    unittest.main()
