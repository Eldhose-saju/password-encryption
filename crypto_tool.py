from cryptography.fernet import Fernet

# ✅ Load the fixed key from file
with open("key.key", "rb") as file:
    key = file.read()

cipher = Fernet(key)

def encrypt_password(password):
    return cipher.encrypt(password.encode()).decode()

def decrypt_password(encrypted_password):
    return cipher.decrypt(encrypted_password.encode()).decode()
