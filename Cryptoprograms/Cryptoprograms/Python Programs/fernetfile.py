from cryptography.fernet import Fernet
key=Fernet.generate_key()
mykey=open('mykey.key','wb')
mykey.write(key)
mykey=open('mykey.key','rb')
key=mykey.read()
print(key)

f=Fernet(key)
original_file=open('grades.csv','rb')
original=original_file.read()
encrypted=f.encrypt(original)
encrypted_file=open('enc_grades.csv','wb')
encrypted_file.write(encrypted)
encrypted_file.close()

f=Fernet(key)
print(f)
encrypted_file=open('enc_grades.csv','rb')
encrypted=encrypted_file.read()
decrypted=f.decrypt(encrypted)
decrypted_file=open('dec_grades.csv','wb')
decrypted_file.write(decrypted)
decrypted_file.close()
print(decrypted)
