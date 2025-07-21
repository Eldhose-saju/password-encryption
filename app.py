import streamlit as st
from crypto_tool import encrypt_password, decrypt_password

st.set_page_config(page_title="Password Encryptor", layout="centered")

st.title("🔐 Password Encryption Tool")

st.markdown("This tool lets you encrypt and decrypt passwords securely.")

# Choose mode
mode = st.radio("Select an option:", ["Encrypt", "Decrypt"])

if mode == "Encrypt":
    password = st.text_input("Enter password to encrypt:", type="password")
    if st.button("Encrypt"):
        if password:
            encrypted = encrypt_password(password)
            st.success("Encrypted Password:")
            st.code(encrypted)
        else:
            st.warning("Please enter a password to encrypt.")

elif mode == "Decrypt":
    encrypted_input = st.text_input("Enter encrypted password:")
    if st.button("Decrypt"):
        if encrypted_input:
            try:
                decrypted = decrypt_password(encrypted_input)
                st.success("Decrypted Password:")
                st.code(decrypted)
            except Exception as e:
                st.error("Decryption failed. Check your input or key.")
        else:
            st.warning("Please enter an encrypted string.")
