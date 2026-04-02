from affine import encrypt, decrypt
from hash import custom_hash


def run_test():
    text = "HELLO WORLD"
    a = 5
    b = 8

    print("Original Text:", text)

    # Step 1: Encrypt
    cipher = encrypt(text, a, b)
    print("Encrypted Text:", cipher)

    # Step 2: Hash the ciphertext
    hash_value = enhanced_hash(cipher)
    print("Hash Value:", hash_value)

    # Step 3: Decrypt
    decrypted = decrypt(cipher, a, b)
    print("Decrypted Text:", decrypted)

    # Step 4: Verify round-trip
    if decrypted == text:
        print(" SUCCESS: Decryption matches original text!")
    else:
        print(" ERROR: Something went wrong!")


if __name__ == "__main__":
    run_test()

def additional_tests():
    test_cases = [
        "Affine Cipher",
        "crypto123",
        "OpenAI GPT",
        "Security Lab"
    ]

    a = 7
    b = 3

    for text in test_cases:
        cipher = encrypt(text, a, b)
        decrypted = decrypt(cipher, a, b)
        hash_value = enhanced_hash(cipher)

        print("\nText:", text)
        print("Cipher:", cipher)
        print("Hash:", hash_value)
        print("Decrypted:", decrypted)

if __name__ == "__main__":
    run_test()
    additional_tests()