# Symmetric Encryption Application
A Python application for securely encrypting and decrypting text using AES-256-GCM

## Installation
```
pip install cryptography
```

## Usage
Start the application:
```
python cli.py
```

## Menu Options
1. Generate new key - Creates a secure 256-bit key
2. Encrypt text - Encrypt your message with a key
3. Decrypt text - Decrypt a message with the correct key
4. Exit - Close the application

## Technical Details
* Algorithm: AES-256-GCM (Authenticated encryption)
* Key length: 256 bits (32 bytes)
* Mode: Galois/Counter Mode with authentication
* Library: Python cryptography

## Files
* `cli.py` - Command line interface
* `crypto_utils.py` - Encryption functionalities
* `test_crypto.py` - Unit tests
* `README.md` - This file

## Kerckhoffs's Principle
This application follows Kerckhoffs's principle: security lies entirely in the secret key, not in the algorithm. All code is public, only the key must remain secret.

## Security
Important:
* Store keys securely
* Share keys only through secure channels
* Without the correct key, decryption is impossible

## Tests
Run the tests:
```
python test_crypto.py
```

## Author
Caner Kümür
