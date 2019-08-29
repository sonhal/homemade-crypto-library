import unittest
from homemade_crypto.__main__ import cli

class CLITest(unittest.TestCase):

    def test_ceasar_cli(self):
        cipher, action, key, target = cli(["caesar", "encrypt", "-k", "2", "-i", "LISAGIKKTILSKOLEN"])
        self.assertEqual("caesar", cipher)
        self.assertEqual("encrypt", action)
        self.assertEqual("2", key)
        self.assertEqual("LISAGIKKTILSKOLEN", target)
