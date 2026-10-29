# 🔐 Heuristic XOR Cipher Crypto-Analytic Breaker

A high-performance cryptographic utility written in pure Python, designed to analyze, brute-force, and decrypt multi-byte XOR-encrypted payloads using ASCII frequency constraints and heuristic pruning techniques.

---

## 🧠 The Cryptographic Challenge

The core engine targets multi-byte XOR encryption schemes. A standard repeating-key XOR cipher applies bitwise operations sequentially:
`Ciphertext[i] = Plaintext[i] ^ Key[i % KeyLength]`

### The Pruning Breakthrough
Instead of a naive brute-force that allocates memory for thousands of garbage strings, the script implements an early-exit pruning mechanism during the key derivation space calculation:
```python
if resulting_value < 32 or resulting_value > 126:
    break
```
By evaluating the output against printable ASCII boundaries (32 to 126), the execution tree drops invalid keys within microseconds, drastically compressing the processing search space.

---

## 🚀 Execution & Verification Setup

To execute the mathematical brute-force algorithm directly against the encrypted stream dump:
```bash
python3 xor.py
```

The script will automatically execute the key space permutation search, apply statistical linguistic filters based on space character frequency, and output the cracked key along with the plaintext payload.

---

## 📊 Performance Analysis
- **Key Space Dimension:** For a 3-byte lowercase alphabetic key space ([a-z]^3), the configuration spans 26^3 = 17,576 permutations.
- **Time Complexity:** Average runtime maps to O(N * K) where N represents text byte size and K represents total key search permutations.
- **Space Complexity:** O(M) where M represents verified printable matches, ensuring near-zero heap memory overhead.

---

                                                                              *Morse Code ..- ._ 📟*
