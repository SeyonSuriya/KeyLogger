from cryptography.fernet import Fernet

class FileDecryptor:
    def __init__(self, encryption_key):
        self.fernet = Fernet(encryption_key)

    def decrypt_file(self, input_filename, output_filename):
        with open(input_filename, 'rb') as file:
            encrypted_data = file.read()

        decrypted_data = self.fernet.decrypt(encrypted_data)

        with open(output_filename, 'wb') as file:
            file.write(decrypted_data)

# if __name__ == "__main__":
#     # Replace with the same encryption key used for encryption
#     encryption_key = b'YOUR_ENCRYPTION_KEY_HERE'
#
#     # Paths to encrypted input and decrypted output files
#     input_encrypted_filename = 'encrypted.zip'
#     output_decrypted_filename = 'decrypted.zip'
#
#     decryptor = FileDecryptor(encryption_key)
#     decryptor.decrypt_file(input_encrypted_filename, output_decrypted_filename)
#
#     print(f'File "{input_encrypted_filename}" decrypted and saved as "{output_decrypted_filename}".')
