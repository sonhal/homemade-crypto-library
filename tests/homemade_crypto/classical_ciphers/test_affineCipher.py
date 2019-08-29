from unittest import TestCase

from homemade_crypto.classical_ciphers.affine_cipher import AffineCipher

VALID_A_VALUES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
VALID_B_VALUES = list(range(0, 37))


class TestAffineCipher(TestCase):

    def test_gen_key(self):
        affine = AffineCipher.ascii_affine()
        key = affine.gen_key()
        self.assertIn(key[0], VALID_A_VALUES)
        self.assertIn(key[1], VALID_B_VALUES)

    def test_encrypt(self):
        affine = AffineCipher.ascii_affine()
        key = (5, 8)
        plain_text = "LISEGIKKTILSKOLEN"
        expected = " LY1BLVV2L YVE 19"
        cipher_text = affine.encrypt(key, plain_text)
        self.assertEqual(expected, cipher_text)

    def test_decrypt(self):
        affine = AffineCipher.ascii_affine()
        key = (5, 8)
        plain_text = "LISEGIKKTILSKOLEN"
        cipher_text = affine.encrypt(key, plain_text)
        result = affine.decrypt(key, cipher_text)
        self.assertEqual(plain_text, result)
