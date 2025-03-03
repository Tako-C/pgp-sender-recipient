import gnupg

# Create a GPG instance
gpg = gnupg.GPG()

# Define paths for the recipient's private key file and the encrypted file
recipient_private_key_file = '[path of recipient_private_key.asc]'
input_enc_file = '[path of input_enc_file.txt]'
output_dec_file = '[path of output_dec_file.txt]'
passphrase = 'yourpassphrase'

# Import the recipient's private key
with open(recipient_private_key_file, 'rb') as private_key_file:
    private_key_data = private_key_file.read()

gpg.import_keys(private_key_data)

# Decrypt the encrypted file
with open(input_enc_file, 'rb') as enc_file:
    decrypted_data = gpg.decrypt_file(enc_file, passphrase=passphrase)

if decrypted_data.ok:
    # Save the decrypted file
    with open(output_dec_file, 'w') as dec_file:
        dec_file.write(str(decrypted_data))  # Save the decrypted content as a string
    print("✅ File decrypted successfully. Saved to:", output_dec_file)
else:
    print("❌ Error during decryption:", decrypted_data.status)

# Verify the signature
verified = gpg.verify(decrypted_data.data)

if verified:
    print("✅ Signature is valid and the file has not been altered.")
else:
    print("❌ Signature is invalid or the file has been altered.")
