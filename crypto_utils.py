from cryptography.fernet import Fernet
import os
import base64

# Use a consistent key for encryption/decryption
CRYPTO_KEY = os.getenv("CRYPTO_KEY", "YOUR_SECRET_KEY_HERE").encode()
fernet = Fernet(base64.b64encode(CRYPTO_KEY.ljust(32)[:32]))


def encrypt_text(text: str) -> str:
    """Encrypt a text string."""
    return fernet.encrypt(text.encode()).decode()


def decrypt_text(encrypted_text: str) -> str:
    """Decrypt an encrypted text string."""
    return fernet.decrypt(encrypted_text.encode()).decode()
