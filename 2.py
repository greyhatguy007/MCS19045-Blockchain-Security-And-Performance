import random
# Function to generate prime numbers
def generate_prime():
    primes = [i for i in range(2, 100) if all(i % j != 0 for j in range(2, int(i**0.5) + 1))]
    return random.choice(primes)
# Function to find gcd
def gcd(a, b):
    while b != 0:
    a, b = b, a % b
    return a
# Function to find modular inverse
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1
# Function to generate public and private keys
def generate_keys():
    p = generate_prime()
    q = generate_prime()
    n = p * q
    phi = (p - 1) * (q - 1)
    # Choose e such that 1 < e < phi and gcd(e, phi) = 1
    while True:
        e = random.randrange(2, phi)
        if gcd(e, phi) == 1:
            break
        # Compute d as modular inverse of e
    d = mod_inverse(e, phi)
    print(f"p:{p}\nq:{q}\nn:{n}\nphi:{phi}\ne:{e}\nd:{d}")
    return ((e, n), (d, n))
# Function to encrypt plaintext
def encrypt(plaintext, public_key):
    e, n = public_key
    encrypted_msg = [pow(ord(char), e, n) for char in plaintext]
    return encrypted_msg
# Function to decrypt ciphertext
def decrypt(ciphertext, private_key):
    d, n = private_key
    decrypted_msg = ''.join([chr(pow(char, d, n)) for char in ciphertext])
    return decrypted_msg
# Main function
def main():
# Generate public and private keys
    public_key, private_key = generate_keys()
    print("Public Key:", public_key)
    print("Private Key:", private_key)
    # Encrypt a message
    plaintext = input("Enter plaintext to encrypt: ")
    encrypted_msg = encrypt(plaintext, public_key)
    print("Encrypted Message:", encrypted_msg)
    # Decrypt the message
    decrypted_msg = decrypt(encrypted_msg, private_key)
    print("Decrypted Message:", decrypted_msg)

if __name__ == "__main__":
    main()