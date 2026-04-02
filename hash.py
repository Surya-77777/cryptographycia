def custom_hash(text):
    p = 31          # base (prime)
    m = 10**9 + 9   # large prime modulus
    hash_value = 0
    power = 1

    for char in text:
        # Convert char → number (handle all ASCII cleanly)
        x = ord(char)

        hash_value = (hash_value + x * power) % m
        power = (power * p) % m

    return hash_value


    return hash_value

if __name__ == "__main__":
    text = "HELLO WORLD"

    print(" Hash:", custom_hash(text))
