import gnupg

gpg = gnupg.GPG()

private_key_file = './keys/recipient_0x1FA6885B_private.asc'
passphrase = '2recipient2'

with open(private_key_file, 'rb') as key_file:
    gpg.import_keys(key_file.read())

encrypted_message_file = './scc/enc_doc.txt'

with open(encrypted_message_file, 'rb') as enc_file:
    decrypted_data = gpg.decrypt_file(enc_file, passphrase=passphrase)

if decrypted_data.ok:
    print("Decrypted message:")
    print(decrypted_data.data.decode())
else:
    print("Error during decryption:", decrypted_data.status)
