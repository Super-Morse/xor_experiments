# 🔐 Full-Stack XOR Cipher Crypto-Analytic Breaker

A robust, high-performance cryptographic utility designed to analyze, brute-force, and decrypt multi-byte XOR-encrypted payloads using ASCII frequency constraints and heuristic pruning techniques. 

This project showcases a modular full-stack architecture: an algorithmic prototyping core, a lightweight API service layer, and a dynamic Material-UI React interface.

---

## 🧠 The Cryptographic Challenge

The core engine targets multi-byte XOR encryption schemes. A standard repeating-key XOR cipher applies bitwise operations sequentially:
`Ciphertext[i] = Plaintext[i] ^ Key[i % KeyLength]`

### The Pruning Breakthrough
Instead of a naive brute-force that allocates memory for billions of garbage strings, the core engine implements an early-exit pruning mechanism during the key derivation space calculation:
```python
if resulting_value < 32 or resulting_value > 126:
    break
```
By evaluating the output against printable ASCII boundaries (32 to 126), the execution tree drops invalid keys within microseconds, compressing the processing search space.

---

## 🛠 Tech Stack & Architecture

- **Research & Core Engine:** Python 3 (Itertools Product Space, Stream IO)
- **Backend API Layer:** Python Service Engine (`server.py`)
- **Frontend Interface:** React.js (Legacy 16.8 Hooks/Lifecycle), Material-UI Core layouts.

```text
       ┌────────────────────────┐
       │   React SPA Frontend   │ ◄─── Material-UI (Input Encrypted Bytes)
       └───────────┬────────────┘
                   │
                   ▼ (REST JSON API / HTTP POST)
       ┌────────────────────────┐
       │ Python Backend Server  │ ◄─── Runtime Interface / Cryptographic Pipeline
       └───────────┬────────────┘
                   │
                   ▼
       ┌────────────────────────┐
       │  XOR Pruning Engine    │ ◄─── Heuristic Key Extraction Space Check
       └────────────────────────┘
```

---

## 🚀 Local Development & Execution Setup

### 1. Running the Core Algorithmic Proof-of-Concept
To execute the raw mathematical brute-force algorithm directly against the encrypted stream dump:
```bash
cd research
python3 xor.py
```

### 2. Launching the Backend Service Layer
Ensure you have the required environment extensions deployed locally, then spin up the API daemon:
```bash
cd backend/src
python3 server.py
```

### 3. Deploying the React Interface
Initialize node package structures and launch the local Webpack dev server:
```bash
cd frontend
npm install
npm start
```
Open [http://localhost:3000](http://localhost:3000) to view the interactive crypto-analysis console.

---

## 📊 Performance & Optimization Analysis
- **Key Space Dimension:** For a 3-byte lowercase alphabetic key space ([a-z]^3), the configuration spans 26^3 = 17,576 permutations.
- **Time Complexity:** Average runtime maps to O(N * K) where N represents text byte size and K represents total key search permutations.
- **Space Complexity:** O(M) where M represents verified printable matches, drastically lowering standard thread heap allocation overhead.

---

*Morse Code ..- ._ 📟*
