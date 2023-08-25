import os
from cryptography.fernet import Fernet

class ZipFileEncryptor:
    def __init__(self, encryption_key):
        self.fernet = Fernet(encryption_key)

    def encrypt_file(self, input_filename, output_filename):
        with open(input_filename, 'rb') as file:
            file_data = file.read()

        encrypted_data = self.fernet.encrypt(file_data)

        with open(output_filename, 'wb') as file:
            file.write(encrypted_data)

# if __name__ == "__main__":
#     # Replace with your desired key (use Fernet.generate_key() to generate a key)
#     encryption_key = b'YOUR_ENCRYPTION_KEY_HERE'
#
#     # Paths to input and output files
#     input_zip_filename = 'input.zip'
#     output_encrypted_filename = 'encrypted.zip'
#
#     encryptor = ZipFileEncryptor(encryption_key)
#     encryptor.encrypt_file(input_zip_filename, output_encrypted_filename)
#
#     print(f'File "{input_zip_filename}" encrypted and saved as "{output_encrypted_filename}".')
