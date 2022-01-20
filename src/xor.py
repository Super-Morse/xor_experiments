from itertools import product

def xor_decrypt(encrypted_text: list[int], key: list[int]) -> list[int]:
    """
      Decrypt encrypted text by key
    """

    text = []

    for idx,item in enumerate(encrypted_text):
        text.append(item ^ key[idx % len(key)])

    return text

print(xor_decrypt([24, 24, 26, 30, 28], [1, 2]))
print(xor_decrypt(xor_decrypt([25, 26, 27, 28, 29], [1, 2]), [1, 2]))
#for k in product(range(ord("a"), ord("z") + 1), repeat=3):
    #print(''.join(k))