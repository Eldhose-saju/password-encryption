from crypto_tool import encrypt_password, decrypt_password

def main():
    print("==== Password Encryption Tool ====")
    print("1. Encrypt a password")
    print("2. Decrypt a password")

    choice = input("Enter your choice (1/2): ").strip()

    if choice == "1":
        password = input("Enter the password to encrypt: ").strip()
        encrypted = encrypt_password(password)
        print("Encrypted password:", encrypted.decode())

    elif choice == "2":
        encrypted_input = input("Enter the encrypted password: ").strip().encode()
        try:
            decrypted = decrypt_password(encrypted_input)
            print("Decrypted password:", decrypted)
        except Exception as e:
            print("Error: Decryption failed. Make sure the key and input are correct.")

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
