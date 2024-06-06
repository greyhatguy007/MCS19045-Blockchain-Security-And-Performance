import random
def mod_exp(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent //= 2
        base = (base * base) % modulus
    return result
# Function to generate a random prime number
def generate_prime():
    def is_prime(n, k=5):
        if n <= 1:
            return False
        if n <= 3:
            return True
        for _ in range(k):
        a = random.randint(2, n - 2)
        if mod_exp(a, n - 1, n) != 1:
            return False
        return True
    while True:
        p = random.randint(100, 1000)
        if is_prime(p):
        print("Selected Prime Number : ", p)
        return p
# Function to generate public and private keys
def generate_keys(p):
    g = 2 # Generator value
    a = random.randint(2, p - 1) # Private key for Alice
    b = random.randint(2, p - 1) # Private key for Bob
    A = mod_exp(g, a, p) # Public key for Alice
    B = mod_exp(g, b, p) # Public key for Bob
    return (p, g, A, B, a, b)

# Function to compute shared secret key
def compute_shared_secret(p, A, b):
    return mod_exp(A, b, p)

# Main function
def main():
    # Generate a random prime number
    p = generate_prime()
    # Generate public and private keys for Alice and Bob
    p, g, A, B, a, b = generate_keys(p)
    print(f"pub_a:{A}\npub_b:{B}\npri_a:{a}\npri_b:{b}")
    # Compute shared secret key
    secret_key_A = compute_shared_secret(p, B, a)
    secret_key_B = compute_shared_secret(p, A, b)
    # Both Alice and Bob should have the same secret key
    print("Shared Secret Key (Alice):", secret_key_A)
    print("Shared Secret Key (Bob):", secret_key_B)


if __name__ == "__main__":
    main()