def xor_cipher(text_or_bytes: list[int] | str, key: str) -> list[int] | str:
    """Universal function: encrypts string to bytes OR decrypts bytes to string."""
    key_bytes = [ord(char) for char in key]
    key_len = len(key_bytes)
    
    # Determine the mode: if input is a string, we encrypt (convert to ASCII codes)
    if isinstance(text_or_bytes, str):
        input_bytes = [ord(char) for char in text_or_bytes]
        is_encrypting = True
    else:
        input_bytes = text_or_bytes
        is_encrypting = False
        
    result_bytes = []
    # Core cryptographic loop with repeating key pattern (idx % key_len)
    for idx, item in enumerate(input_bytes):
        resulting_value = item ^ key_bytes[idx % key_len]
        result_bytes.append(resulting_value)
        
    # If encrypting, return list of numbers. If decrypting, join codes into a string.
    if is_encrypting:
        return result_bytes
    else:
        return "".join(chr(_) for _ in result_bytes)


if __name__ == "__main__":
    print("--- 🔐 INTERACTIVE XOR CIPHER / DECIPHER ---")
    print("Select an option:")
    print("1. Encrypt plaintext string")
    print("2. Decrypt comma-separated integer byte array")
    
    choice = input("Enter choice (1 or 2): ").strip()
    
    if choice == "1":
        # Prompt user for encryption keys and text
        user_key = input("🔑 Enter encryption key: ")
        user_text = input("📝 Enter plaintext to encrypt: ")
        
        # Execute encryption routine
        encrypted = xor_cipher(user_text, user_key)
        
        print("\n📦 ENCRYPTED INT BYTE ARRAY:")
        print(", ".join(map(str, encrypted)))
        
    elif choice == "2":
        # Prompt user for decryption keys and ciphertext array
        user_key = input("🔑 Enter encryption key: ")
        raw_numbers = input("📦 Enter comma-separated numbers: ")
        
        try:
            # Parse raw text input string into integer array dump
            user_bytes = [int(num.strip()) for num in raw_numbers.split(",")]
            
            # Execute decryption routine
            decrypted = xor_cipher(user_bytes, user_key)
            
            print("\n📝 DECRYPTED PLAINTEXT:")
            print(decrypted)
        except ValueError:
            print("\n❌ Error: Invalid numbers format. Make sure they are separated by commas.")
            
    else:
        print("\n❌ Error: Invalid selection choice.")
