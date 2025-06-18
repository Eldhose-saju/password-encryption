from cryptography.fernet import Fernet

# Load the previously generated key
def load_key():
    with open("key.key", "rb") as file:
        return file.read()

# Encrypt the password
def encrypt_password(password):
    key = load_key()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(password.encode())
    return encrypted

# Decrypt the password
def decrypt_password(encrypted_password):
    key = load_key()
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_password)
    return decrypted.decode()
