"""
Home made crypto lib. Main module to execute crypto algorithms from the CLI
"""

from homemade_crypto.cli import cli, run_commands


if __name__ == '__main__':
    cipher, action, key, target = cli()
    result = run_commands(cipher, action, key, target)
    print(result)
