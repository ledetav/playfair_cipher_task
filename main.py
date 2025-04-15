from playfair import encrypt_playfair, decrypt_playfair

def main():
    text = "IDIOCY OFTEN LOOKS LIKE INTELLIGENCE"
    key = "WHEATSON"

    encrypted = encrypt_playfair(text, key)
    decrypted = decrypt_playfair(encrypted, key)

    print("🔐 Playfair Cipher")
    print(f"Plaintext : {text}")
    print(f"Key       : {key}")
    print(f"Encrypted : {encrypted}")
    print(f"Decrypted : {decrypted}")

if __name__ == "__main__":
    main()
