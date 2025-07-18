import os
from powerdnsadmin.security import encryption, token


def test_encrypt_decrypt():
    key = os.urandom(16)
    secret = "sensitive data"
    enc = encryption.encrypt(secret, key)
    dec = encryption.decrypt(enc, key)
    assert dec == secret


def test_generate_token_length():
    tok = token.generate_token(16)
    assert len(tok) >= 16
