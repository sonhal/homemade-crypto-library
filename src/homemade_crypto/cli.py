import typing
import argparse
from homemade_crypto.classical_ciphers import CaesarCipher, VigenereCipher

CIPHERS = {
    "caesar": CaesarCipher.norwegian_caesar(),
    "vigenere": VigenereCipher.norwegian_vigenere()
}


def cli(arguments: typing.Sequence = None) -> typing.Tuple:
    """
    Handles CLI for homemade_crypto
    :param arguments:
    :return: None
    """
    parser = argparse.ArgumentParser(description='Access and use cryptographic algorithms and functions')
    parser.add_argument('cipher', type=str, choices=CIPHERS.keys(),
                        help='The cipher to use')
    parser.add_argument('action',
                        choices=["encrypt", "decrypt", "gen-key"],
                        help='Action to complete using the chosen cipher')
    parser.add_argument('-i', "--in", dest="target",
                        help='Input to encrypt or decrypt command')
    parser.add_argument("-k", "--key",
                        help='Action to complete using the chosen cipher')

    args = parser.parse_args(arguments)
    return args.cipher, args.action, args.key, args.target


def run_commands(cipher, action, key, target):
    cipher = CIPHERS[cipher]
    if action == "encrypt":
        return cipher.encrypt(key, target)
    elif action == "decrypt":
        return cipher.decrypt(key, target)
    elif action == "gen-key":
        return cipher.gen_key()

