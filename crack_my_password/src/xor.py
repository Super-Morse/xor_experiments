from itertools import product

def xor_decrypt(key: list[int], encrypted_text: list[int] ) -> list[int]:
    """
      Decrypt encrypted text by key
    """

    text = []
    key_len = len(key)
    for idx,item in enumerate(encrypted_text):
        resulting_value = item ^ key[idx % key_len]
        if resulting_value < 32 or resulting_value > 126:
            break
        text.append(resulting_value)

    return text

def guess_key(encrypted_text: list[int], key_size: int) -> list[list]:
    """
        Break XOR decryption with brute force to find all possible combinations if decrypted string and a key
    """
    possible_text_and_key_list = []
    for k in product(range(ord("a"), ord("z") + 1), repeat=key_size):
        decrypted_text = xor_decrypt(list(k), encrypted_text)
        if len(decrypted_text) == len(encrypted_text):
            possible_text_and_key_list.append([ ''.join(chr(_) for _ in k), ''.join(chr(_) for _ in decrypted_text)])

    return possible_text_and_key_list


if __name__ == '__main__':
    with open('encrypted.txt') as file:
        encrypted_text = [int(_) for _ in next(file).split(',')]
    #print(xor_decrypt([122,122,122] ,encrypted_text))
    print(guess_key(encrypted_text, 3))

