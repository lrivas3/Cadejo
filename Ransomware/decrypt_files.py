from Crypto.PublicKey import ECC
import os

public_key = "publi_key.pem"

files = []

for file in os.listdir():
     if file == "encrypt.py" or file == "decrypt.py":
         continue
     if os.path.isfile(file):
        files.append(file)
os.listdir()


def decrypt_file(file_path, private_key_path, output_file_path):
    # Generate an ECC private key from a PEM file
    with open(private_key_path, 'rb') as f:
        ecc_key = ECC.import_key(f.read())

    # Read the encrypted file contents
    with open(file_path, 'rb') as f:
        ciphertext = f.read()

    # Decrypt the file with the ECC private key
    plaintext = ecc_key.decrypt(ciphertext)

    # Write the decrypted file to the output file
    with open(output_file_path, 'wb') as f:
        f.write(plaintext)