import gnupg

# สร้าง instance ของ GPG
gpg = gnupg.GPG()

recipient_private_key_file = './keys/recipient_0x1FA6885B_private.asc'
input_enc_file = './scc/encrypt/enc_doc.txt'
output_dec_file = './scc/decrypt/dec_doc.txt'
passphrase = '2recipient2'


with open(recipient_private_key_file, 'rb') as private_key_file:
    private_key_data = private_key_file.read()

gpg.import_keys(private_key_data)


with open(input_enc_file, 'rb') as enc_file:
    decrypted_data = gpg.decrypt_file(enc_file, passphrase=passphrase)
# print(" decrypted_data :",decrypted_data)
if decrypted_data.ok:
    with open(output_dec_file, 'w') as dec_file:
        dec_file.write(str(decrypted_data))  # บันทึกไฟล์ที่ถอดรหัสแล้ว
    print("✅ File decrypted successfully. Saved to:", output_dec_file)
else:
    print("❌ Error during decryption:", decrypted_data.status)

verified = gpg.verify(decrypted_data.data)

if verified:
    print("✅ Signature is valid and the file has not been altered.")
else:
    print("❌ Signature is invalid or the file has been altered.")
