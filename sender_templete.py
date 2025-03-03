import gnupg

# Initialize GPG instance
gpg = gnupg.GPG()

# Paths to your key files and document files
recipient_key_file = '[path of recipient_public_key.asc]'
sender_key_file = '[path of sender_private_key.asc]'
input_doc_file = '[path of input_doc_file.txt]'
signed_doc_file = '[path of signed_doc_file.txt]'
output_enc_file = '[path of output_enc_file.txt]'
passphrase = 'yourpassphrase'

# Import recipient's public key
with open(recipient_key_file, 'rb') as public_key_file:
    public_key_data = public_key_file.read()

import_result = gpg.import_keys(public_key_data)
if import_result.count == 0:
    print("Error: No keys imported. Make sure the public key file is correct.")
    exit()

recipient_key_id = import_result.results[0]['fingerprint']

# Import sender's private key
with open(sender_key_file, 'rb') as private_key_file:
    private_key_data = private_key_file.read()

import_result = gpg.import_keys(private_key_data)
if import_result.count == 0:
    print("Error: No keys imported. Make sure the private key file is correct.")
    exit()

sender_key_id = import_result.results[0]['fingerprint']
print("recipient_key_id:", recipient_key_id)
print("sender_key_id:", sender_key_id)

# Sign the document
extra_args = ['--digest-algo', 'SHA256']
with open(input_doc_file, 'rb') as doc_file:
    signed_data = gpg.sign_file(doc_file, keyid=sender_key_id, passphrase=passphrase, extra_args=extra_args)

if signed_data:
    # Save the signed document
    with open(signed_doc_file, 'wb') as signed_file:  # Use 'wb' for binary output
        signed_file.write(signed_data.data)
    print("File signed successfully.")
else:
    print("Error during signing:", signed_data.status)

# Encrypt the signed document
with open(signed_doc_file, 'rb') as enc_doc_file:
    encrypted_data = gpg.encrypt_file(enc_doc_file, recipients=[recipient_key_id])

if encrypted_data.ok:
    # Save the encrypted document
    with open(output_enc_file, 'wb') as enc_signed_file:  # Use 'wb' for binary output
        enc_signed_file.write(encrypted_data.data)
    print("File encrypted successfully.")
else:
    print("Error during encryption:", encrypted_data.status)
