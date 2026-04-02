def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def mod_inverse(a, m):
    # Brute-force method (simple and allowed)
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None
def encrypt(text, a, b):
    result = ""

    if gcd(a, 26) != 1:
        raise ValueError("Key 'a' is not coprime with 26!")

    for char in text:
        if char.isalpha():
            x = ord(char.upper()) - ord('A')
            encrypted = (a * x + b) % 26
            result += chr(encrypted + ord('A'))
        else:
            result += char  # keep spaces/symbols

    return result
def decrypt(cipher, a, b):
    result = ""

    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        raise ValueError("Modular inverse does not exist!")

    for char in cipher:
        if char.isalpha():
            x = ord(char.upper()) - ord('A')
            decrypted = (a_inv * (x - b)) % 26
            result += chr(decrypted + ord('A'))
        else:
            result += char

    return result

if __name__ == "__main__":
    text = "HELLO WORLD"
    a = 5
    b = 8

    cipher = encrypt(text, a, b)
    print("Encrypted:", cipher)

    plain = decrypt(cipher, a, b)
    print("Decrypted:", plain)