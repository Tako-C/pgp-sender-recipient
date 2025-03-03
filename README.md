# PGP Encryption and Decryption

## Introduction

Pretty Good Privacy (PGP) is an encryption program that provides cryptographic privacy and authentication. It is used to secure communications, ensure the integrity of data, and authenticate the sender through digital signatures.

## Key Concepts

1. **Public Key Encryption**: 
   - Each user has a public key (for encryption) and a private key (for decryption).
   - The sender uses the recipient's public key to encrypt the message, ensuring only the recipient can decrypt it with their private key.

2. **Private Key Signing**:
   - The sender can sign the message using their private key. This signature ensures the authenticity of the message and verifies that it hasn’t been altered.
   - The recipient uses the sender's public key to verify the signature.

3. **Hashing**:
   - A cryptographic hash algorithm, such as SHA256, is used to create a unique hash of the message.
   - This hash is signed by the sender to ensure the integrity of the message.

## How PGP Works

### Step 1: Key Pair Generation
- The sender and recipient generate their own public and private key pairs. The private key is kept secret, while the public key is shared with others.

### Step 2: Signing the Message
- The sender signs the message using their private key and a hashing algorithm (e.g., SHA256). The signature is appended to the message.

### Step 3: Encrypting the Message
- The sender encrypts the signed message using the recipient's public key. This ensures that only the recipient can decrypt the message with their private key.

### Step 4: Decryption and Signature Verification
- The recipient uses their private key to decrypt the message.
- The recipient then verifies the sender’s signature using the sender’s public key to ensure the message’s authenticity and integrity.

## Usage

1. **Signing a Message**:
   - The sender signs the message using their private key and a hashing algorithm (e.g., SHA256).
   
2. **Encrypting a Message**:
   - The sender encrypts the signed message using the recipient's public key.

3. **Decrypting a Message**:
   - The recipient decrypts the message using their private key.

4. **Verifying the Signature**:
   - The recipient verifies the signature using the sender’s public key.

## Example Code

```python
import gnupg

gpg = gnupg.GPG()

# Import keys
public_key_file = './keys/recipient_public.asc'
private_key_file = './keys/sender_private.asc'

# Import recipient's public key
with open(public_key_file, 'rb') as key_file:
    gpg.import_keys(key_file.read())

# Import sender's private key
with open(private_key_file, 'rb') as key_file:
    gpg.import_keys(key_file.read())

# Sign the file
with open('input_file.txt', 'rb') as file:
    signed_data = gpg.sign_file(file, keyid='sender_key_id', passphrase='your_passphrase')

# Encrypt the file
with open('signed_file.txt', 'rb') as file:
    encrypted_data = gpg.encrypt_file(file, recipients=['recipient_key_id'], output='encrypted_file.txt')
