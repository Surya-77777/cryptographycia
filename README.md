# cryptography cia
#  Affine Cipher with Custom Hash Function

##  Overview

This project implements the **Affine Cipher**, a classical encryption technique, along with a **custom-built hashing function**. The system demonstrates a complete workflow:

> **Encryption → Hashing → Decryption → Verification

All components are implemented  without using any built-in cryptographic libraries.

---

##  Theory

###  Affine Cipher

The Affine Cipher is a substitution cipher that uses a mathematical function to encrypt and decrypt text.

#### Encryption:

[
E(x) = (ax + b) \mod 26
]

#### Decryption:

[
D(x) = a^{-1}(x - b) \mod 26
]

Where:

* `x` = numerical value of letter (A=0, B=1, ..., Z=25)
* `a`, `b` = keys
* `a⁻¹` = modular inverse of `a` under modulo 26

**Important Condition:**
`a` must be coprime with 26 (i.e., gcd(a, 26) = 1)

---

###  Custom Hash Function

A simple polynomial rolling hash function that converts a string into a numeric hash value.

###  Overview

This function computes a hash by treating the input string as a polynomial, where each character contributes based on its ASCII value and position. It uses modular arithmetic to keep the result within a fixed range and reduce overflow.

###  How It Works

* Each character is converted to its ASCII value using `ord(char)`.
* A prime number (`p = 31`) is used as the base.
* Each character’s contribution is multiplied by increasing powers of `p`.
* All operations are performed modulo a large prime (`m = 10^9 + 9`) to avoid large numbers and reduce collisions.

###  Formula

[
\text{hash} = \sum_{i=0}^{n-1} (\text{ord}(text[i]) \times p^i) \mod m
]

###  Parameters

* `text` *(str)*: The input string to hash.

###  Returns

* *(int)*: The computed hash value.

###  Properties

* Deterministic: Same input → same hash.
* Order-sensitive: `"abc"` and `"cba"` produce different hashes.
* Efficient: Runs in **O(n)** time.

###  Use Cases

* String comparison
* Hash tables
* Rolling hash (e.g., Rabin–Karp algorithm)
* Detecting duplicate strings

---


##  Implementation Details

  Files

```
Affine-Cipher/
│
├── affine.py     # Encryption & Decryption logic
├── hash.py       # Custom hash function
├── test.py       # Test script (end-to-end demo)
└── README.md     # Documentation
```

---

##  How to Run

1. Make sure Python is installed (Python 3.x recommended)

2. Run the test script:

```
python test.py
```

---

  Example Output

```
Original Text: HELLO WORLD
Encrypted Text: RCLLA OAPLX
Hash Value: 87346219
Decrypted Text: HELLO WORLD
SUCCESS: Decryption matches original text!
```

---

  Test Workflow

The system performs the following steps:

1. Encrypts plaintext using Affine Cipher
2. Generates a hash of the ciphertext
3. Decrypts the ciphertext back to plaintext
4. Verifies correctness by comparing original and decrypted text

---

## 🧾 Sample Test Cases

| Plaintext     | Ciphertext  | Decrypted     |
| ------------- | ----------- | ------------- |
| HELLO WORLD   | RCLLA OAPLX | HELLO WORLD   |
| Affine Cipher | (varies)    | Affine Cipher |


---

##  Constraints Followed

* No use of cryptographic libraries
* All algorithms implemented from scratch
* Custom hashing function used (not MD5/SHA)

---

## Key Features

* Clean and modular implementation
* Handles uppercase, lowercase, and spaces
* Includes multiple test cases
* Demonstrates full encryption-decryption cycle

---

##  Conclusion

This project successfully demonstrates:

* A working classical cipher (Affine Cipher)
* A custom-designed hash function
* A complete secure data transformation pipeline

---

##  S.Surya
Roll No:23011102081
