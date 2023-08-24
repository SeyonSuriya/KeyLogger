from cryptography.fernet import Fernet


class KeyGenerator:
    def generate_Key(self):
        key = Fernet.generate_key()
        return key
