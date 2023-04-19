# Cadejo

![Cadejo](./img/cadejo.png)

This Python project allows you to encrypt and decrypt files using elliptic curve cryptography.
It simulates a Ransomware attack at its basics by using the Python Libraries cryptography and pycryptodome in order to generate keys and then encrypt and decrypt files.

## Installation

1. Clone this repository

```git
git clone https://github.com/lrivas3/Cadejo.git
```

2. Alternatively you can use a virtual environment to install python packages there
```python3
python3 -m venv venv

# Linux - bash zsh
source ./venv/bin/activate

# Windows - Powershell 
.\venv\bin\Activate.ps1

# Windows - Cmd
.\venv\Scripts\activate.bat

```

3. Install required packages listed on 'requirements.txt'

```python3
pip install -r requirements.txt
```

## Usage

Run the corresponding script for the action you want to perform (encrypt or decrypt) with python3

```python3
# encrypt
python3 encrypt.py

# decrypt
python3 decrypt.py
```
