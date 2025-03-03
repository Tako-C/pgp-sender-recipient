import gnupg

gpg = gnupg.GPG()

recipient_key_file = './keys/recipient_0x1FA6885B_public.asc'
sender_key_file = './keys/sender_0xA5005D65_private.asc'
input_doc_file = './doc.txt'
signed_doc_file = './scc/encrypt/signed_doc.txt'
output_enc_file = './scc/encrypt/enc_doc.txt'
passphrase = '2sender2'

# นำเข้า public key ของผู้รับ
with open(recipient_key_file, 'rb') as public_key_file:
    public_key_data = public_key_file.read()

# นำเข้า private key ของผู้ส่ง
with open(sender_key_file, 'rb') as private_key_file:
    private_key_data = private_key_file.read()

# นำเข้าคีย์
import_result = gpg.import_keys(public_key_data)
if import_result.count == 0:
    print("Error: No keys imported. Make sure the public key file is correct.")
    exit()

recipient_key_id = import_result.results[0]['fingerprint']

import_result = gpg.import_keys(private_key_data)
if import_result.count == 0:
    print("Error: No keys imported. Make sure the private key file is correct.")
    exit()

sender_key_id = import_result.results[0]['fingerprint']
print("recipient_key_id :",recipient_key_id)
print("sender_key_id :",sender_key_id)

extra_args = ['--digest-algo', 'SHA256']
with open(input_doc_file, 'rb') as doc_file:
    signed_data = gpg.sign_file(doc_file, keyid=sender_key_id, passphrase=passphrase, extra_args=extra_args)

if signed_data:
    with open(signed_doc_file, 'w') as signed_file:
        signed_file.write(str(signed_data))
    print("File signed successfully.")
else:
    print("Error during signing:", signed_data.status)

with open(signed_doc_file, 'rb') as enc_doc_file:
    encrypted_data = gpg.encrypt_file(enc_doc_file, recipients=[recipient_key_id])

if encrypted_data.ok:
    with open(output_enc_file, 'w') as enc_signed_file:
        enc_signed_file.write(str(encrypted_data))
    print("File encrypted successfully.")
else:
    print("Error during encryption:", encrypted_data.status)
