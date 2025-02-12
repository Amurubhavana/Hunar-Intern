def caesar_cipher(text, shift, mode="encrypt"):
    result = ""
    
    if mode == "decrypt":
        shift = -shift  # Reverse the shift for decryption

    for char in text:
        if char.isalpha():  # Only encrypt/decrypt letters
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  # Keep other characters unchanged

    return result

# User input
mode = input("Do you want to encrypt or decrypt? ").strip().lower()
text = input("Enter the text: ")
shift = int(input("Enter shift value (1-25): "))

if mode == "encrypt":
    encrypted_text = caesar_cipher(text, shift, "encrypt")
    print(f"Encrypted: {encrypted_text}")
elif mode == "decrypt":
    decrypted_text = caesar_cipher(text, shift, "decrypt")
    print(f"Decrypted: {decrypted_text}")
else:
    print("Invalid mode. Choose 'encrypt' or 'decrypt'.")
