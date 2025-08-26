import secrets
import sys

def find_special_hash(max_attempts=1000):
    print(f"Searching for a hash starting with '00' (max {max_attempts} attempts)...")

    for i in range(1, max_attempts + 1):
        random_hash = secrets.token_hex(16)

        if random_hash.startswith('00'):
            print(f"\nSuccess! Found a matching hash on attempt {i}:")
            print(f"Hash: {random_hash}")
            sys.exit(0)

        if i % 100 == 0:
            print(f"  ...checked {i} hashes.")

    print(f"\nFailure. Could not find a matching hash within {max_attempts} attempts.")
    sys.exit(1)

if __name__ == "__main__":
    find_special_hash()