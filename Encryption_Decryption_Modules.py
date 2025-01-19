import random
from sympy import isprime

# =======================
# Generalized Caesar Cipher Functions
# =======================

def modular_inverse(a, m):
    """Computes the Modular Inverse."""
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def gcd(a, b):
    """Computes the Greatest Common Divisor."""
    while b != 0:
        a, b = b, a % b
    return a

def generalized_caesar_encrypt(plaintext, a, b):
    """Encrypts plaintext using Generalized Caesar Cipher."""
    encrypted_text = ""
    for char in plaintext:
        if 32 <= ord(char) <= 126:  # Printable ASCII range
            x = ord(char) - 32
            encrypted_char = chr(((a * x + b) % 95) + 32)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  # Keep other characters unchanged
    return encrypted_text

def generalized_caesar_decrypt(ciphertext, a, b):
    """Decrypts ciphertext using Generalized Caesar Cipher."""
    decrypted_text = ""
    a_inv = modular_inverse(a, 95)  # Modular inverse of a under modulo 95
    for char in ciphertext:
        if 32 <= ord(char) <= 126:
            y = ord(char) - 32
            decrypted_char = chr(((a_inv * (y - b)) % 95) + 32)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

def frequency_analysis_break(ciphertext):
    """Break Caesar Cipher using frequency analysis."""
    english_frequencies = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
    char_count = {}

    for char in ciphertext:
        if char.isalpha():
            char = char.upper()
            char_count[char] = char_count.get(char, 0) + 1

    sorted_characters = sorted(char_count, key=char_count.get, reverse=True)

    possible_plaintexts = []
    for i, char in enumerate(sorted_characters):
        shift = (ord(char) - ord(english_frequencies[i % len(english_frequencies)])) % 26
        possible_plaintext = generalized_caesar_decrypt(ciphertext, 1, shift)  # Assume a = 1 for simplicity
        possible_plaintexts.append((shift, possible_plaintext))

    return possible_plaintexts

# =======================
# RSA Functions
# =======================

def generate_prime():
    """Generates a random prime number."""
    while True:
        num = random.randint(20, 60)
        if isprime(num):
            return num

def generate_keys():
    """Generates RSA public and private keys."""
    p = generate_prime()
    q = generate_prime()

    n = p * q
    phi = (p - 1) * (q - 1)

    e = 65537
    while gcd(e, phi) != 1:
        e = random.randint(2, phi)

    d = modular_inverse(e, phi)

    return (e, n), (d, n)

def rsa_encrypt(plaintext, public_key):
    """Encrypts plaintext using RSA."""
    e, n = public_key
    plaintext_numbers = [ord(char) for char in plaintext]
    ciphertext = [pow(num, e, n) for num in plaintext_numbers]
    return ciphertext

def rsa_decrypt(ciphertext, private_key):
    """Decrypts ciphertext using RSA."""
    d, n = private_key
    decrypted_numbers = [pow(num, d, n) for num in ciphertext]
    plaintext = ''.join(chr(num) for num in decrypted_numbers)
    return plaintext

# =======================
# File Handling Functions
# =======================

def save_to_file(filename, data):
    """Saves data to a file."""
    with open(filename, 'w') as file:
        file.write(data)

def read_from_file(filename):
    """Reads data from a file."""
    with open(filename, 'r') as file:
        return file.read()
