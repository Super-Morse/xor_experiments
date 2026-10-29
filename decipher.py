from itertools import product

def xor_decrypt(key: list[int], encrypted_text: list[int]) -> list[int]:
    """
    Decrypts the encrypted integer byte array using the provided multi-byte XOR key.
    Applies early-exit pruning if any character falls outside printable ASCII bounds.
    """
    text = []
    key_len = len(key)
    
    for idx, item in enumerate(encrypted_text):
        # Core cryptographic loop: Apply bitwise XOR with the repeating key pattern
        resulting_value = item ^ key[idx % key_len]
        
        # Heuristic Pruning: Exit early if the character is outside printable ASCII bounds (32 to 126)
        if resulting_value < 32 or resulting_value > 126:
            break
        text.append(resulting_value)

    return text

def guess_key(encrypted_text: list[int], key_size: int) -> list[list[str]]:
    """
    Breaks the XOR encryption using optimized product space brute-force for a specific key size.
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
    try:
        with open('encrypted.txt') as file:
            encrypted_text = [int(_) for _ in next(file).split(',')]
    except FileNotFoundError:
        print("❌ Error: 'encrypted.txt' file not found in the current directory.")
        exit(1)
        
    print("🧠 Starting Dynamic Key Length Crypto-Analysis...")
    print("-" * 70)
    
    best_overall_match = None
    max_spaces = -1
    
    # Iteratively attempt to crack the payload using progressive key lengths (from 1 up to 5 bytes)
    for current_size in range(1, 6):
        print(f"📊 Testing key size dimension: {current_size}-byte space ({26**current_size:,} permutations)...")
        
        # Run brute-force for the current key length configuration
        variants = guess_key(encrypted_text, current_size)
        
        if variants:
            print(f"   ↳ 🔍 Found {len(variants)} structurally valid printable ASCII variants.")
            
            # Statistical Filter: Find the local candidate with the highest frequency of standard spaces
            local_best = max(variants, key=lambda variant: variant[1].count(' '))
            local_spaces = local_best[1].count(' ')
            
            # Update the global champion if this key length yields a higher linguistic space ratio
            if local_spaces > max_spaces:
                max_spaces = local_spaces
                best_overall_match = local_best
        else:
            print("   ↳ ❌ No valid structural variants detected.")
            
    print("-" * 70)
    
    # Render final output report based on the linguistic heuristic results
    if best_overall_match and max_spaces > 0:
        print(f"🔑 CRACKED XOR KEY  : '{best_overall_match[0]}' (Length: {len(best_overall_match[0])})")
        print("-" * 70)
        print(f"📝 DECRYPTED TEXT STREAM:\n\n{best_overall_match[1]}\n")
    else:
        print("❌ Crypto-analysis failed. No valid keys matched the structural or linguistic constraints.")
        
    print("-" * 70)
