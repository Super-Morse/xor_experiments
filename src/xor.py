from itertools import product

def xor_decrypt(encrypted_text: list[int], key: list[int]) -> list[int]:
    """
      Decrypt encrypted text by key
    """

    text = []

    for idx,item in enumerate(encrypted_text):
        text.append(item ^ key[idx % len(key)])

    return text

def guess_key(encrypted_text: list[int], key_size: int) -> list[list]:
    """
        Break XOR decryption with brut force to find encrypted string and a key
    """
    possible_text_and_key_list = []
    for k in product(range(ord("a"), ord("z") + 1), repeat=key_size):
        string = ""
        for i in xor_decrypt(encrypted_text, list(k)):
            if chr(i).isalnum or chr(i).punctuation:
                string += chr(i)
        possible_text_and_key_list.append([string,list(k)])
    return possible_text_and_key_list



print(guess_key([24, 24, 26, 30, 28], 2))
print(chr(121),chr(122))