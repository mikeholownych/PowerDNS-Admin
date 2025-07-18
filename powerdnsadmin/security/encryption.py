"""AES encryption utilities for sensitive data."""

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode

BLOCK_SIZE = 16


def pad(data: bytes) -> bytes:
    padding_len = BLOCK_SIZE - len(data) % BLOCK_SIZE
    return data + bytes([padding_len]) * padding_len


def unpad(data: bytes) -> bytes:
    padding_len = data[-1]
    return data[:-padding_len]


def encrypt(plaintext: str, key: bytes) -> str:
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(plaintext.encode()))
    return b64encode(cipher.iv + ct_bytes).decode()


def decrypt(ciphertext: str, key: bytes) -> str:
    raw = b64decode(ciphertext)
    iv = raw[:BLOCK_SIZE]
    ct = raw[BLOCK_SIZE:]
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    return unpad(cipher.decrypt(ct)).decode()
