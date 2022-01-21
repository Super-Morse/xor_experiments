from itertools import product

def xor_decrypt(encrypted_text: list[int], key: list[int]) -> list[int]:
    """
      Decrypt encrypted text by key
    """

    text = []
    key_len = len(key)
    for idx,item in enumerate(encrypted_text):
        if 32 > item > 126:
            break
        text.append(item ^ key[idx % key_len])

    return text

def guess_key(encrypted_text: list[int], key_size: int) -> list[list]:
    """
        Break XOR decryption with brute force to find all possible combinations if decrypted string and a key
    """
    possible_text_and_key_list = []
    for k in product(range(ord("a"), ord("z") + 1), repeat=key_size):
        examined_list = xor_decrypt(encrypted_text, list(k))
        if len(examined_list) == len(encrypted_text):
            possible_text_and_key_list.append([''.join(chr(_) for _ in examined_list), ''.join(chr(_) for _ in k)])

    return possible_text_and_key_list


if __name__ == '__main__':
    with open('encrypted.txt') as file:
        names = [int(_) for _ in next(file).split(',')]

    print(guess_key(names, 3))