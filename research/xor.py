from itertools import product

def xor_decrypt(key: list[int], encrypted_text: list[int]) -> list[int]:
    """
    Decrypts the encrypted integer byte array using the provided multi-byte XOR key.
    Applies early-exit pruning if any character falls outside printable ASCII bounds.
    """
    text = []
    key_len = len(key)
    
    for idx, item in enumerate(encrypted_text):
        # Apply bitwise XOR operation with the repeating key pattern
        resulting_value = item ^ key[idx % key_len]
        
        # Heuristic Pruning: Exit early if the character is not within standard printable ASCII range (32 to 126)
        if resulting_value < 32 or resulting_value > 126:
            break
        text.append(resulting_value)

    return text

def guess_key(encrypted_text: list[int], key_size: int) -> list[list[str]]:
    """
    Breaks the XOR encryption using optimized product space brute-force.
    Returns a list of pairings containing the structural key string and the derived plaintext string.
    """
    possible_text_and_key_list = []
    
    # Generate all possible key permutations for lowercase alphabetic space [a-z]
    for k in product(range(ord("a"), ord("z") + 1), repeat=key_size):
        decrypted_text = xor_decrypt(list(k), encrypted_text)
        
        # Verify if the full payload successfully bypassed the printable ASCII constraint filters
        if len(decrypted_text) == len(encrypted_text):
            key_str = ''.join(chr(_) for _ in k)
            plaintext_str = ''.join(chr(_) for _ in decrypted_text)
            possible_text_and_key_list.append([key_str, plaintext_str])

    return possible_text_and_key_list


if __name__ == '__main__':
    # Load the comma-separated integer byte array dump from the encrypted data file
    with open('encrypted.txt') as file:
        encrypted_text = [int(_) for _ in next(file).split(',')]
    
    # Execute the heuristic cryptographic brute-force routine targeting a 3-byte key space
    all_variants = guess_key(encrypted_text, 3)
    
    print(f"🔍 Found {len(all_variants)} structurally valid printable ASCII variants.")
    print("🧠 Applying linguistic heuristic analysis (Space Frequency Filter)...")
    print("-" * 70)
    
    if all_variants:
        # Statistical Filter: Find the permutation containing the highest frequency of standard space characters
        # In human English, spaces represent the most consistent indicator of text readability
        best_match = max(all_variants, key=lambda variant: variant[1].count(' '))
        
        print(f"🔑 CRACKED XOR KEY  : '{best_match[0]}'")
        print("-" * 70)
        print(f"📝 DECRYPTED TEXT STREAM:\n\n{best_match[1]}\n")
    else:
        print("❌ Crypto-analysis failed. No valid keys matched the structural ASCII criteria constraints.")
    
    print("-" * 70)
