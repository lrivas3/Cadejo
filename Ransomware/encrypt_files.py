from Crypto.PublicKey import ECC
import subprocess
import os

public_key = "./generated_keys/public_key.pem"

files = []

to_encript_folder = "Archivos_a_encriptar"

for file in os.listdir(to_encript_folder):
     file_path = os.path.join(to_encript_folder, file)
     if os.path.isfile(file_path):
        files.append(file_path)

def encrypt_file(file_path, public_key_path):
    # Generate an ECC public key from a PEM file
    with open(public_key_path, 'rb') as f:
        ecc_key = ECC.import_key(f.read())

    # Read the file contents
    with open(file_path, 'rb') as f:
        plaintext = f.read()

    # Encrypt the file with the ECC public key
    ciphertext = ecc_key.encrypt(plaintext)

    # Write the encrypted file to the output file
    with open(file_path, 'wb') as f:
        f.write(ciphertext)

# Run the script that generates the keys
subprocess.call(['python', 'keygen.py'])


# Encrypting the files

# for f in files:
#    encrypt_file(f, public_key)


print(files)