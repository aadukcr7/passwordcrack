"""
Brute Force Password Simulation (Educational)
For Educational Purposes Only
"""

import itertools
import string
import time


def brute_force_crack(target_password: str) -> tuple[str, int, float]:
    """Brute force a user-provided password locally (educational simulation only)."""
    allowed_chars = string.ascii_lowercase + string.digits
    attempts = 0
    start_time = time.perf_counter()

    for length in range(1, len(target_password) + 1):
        for combo in itertools.product(allowed_chars, repeat=length):
            guess = "".join(combo)
            attempts += 1
            if guess == target_password:
                elapsed = time.perf_counter() - start_time
                return guess, attempts, elapsed

    elapsed = time.perf_counter() - start_time
    return "", attempts, elapsed


def main() -> None:
    # For Educational Purposes Only
    print("Brute Force Password Simulation (Educational)")
    print("For Educational Purposes Only - Do not use on real systems.")
    target_password = input("Enter a weak password to test (lowercase letters and digits only): ").strip()

    if not target_password:
        print("No password provided. Exiting.")
        return

    allowed_chars = set(string.ascii_lowercase + string.digits)
    if any(ch not in allowed_chars for ch in target_password):
        print("Invalid input. Use only lowercase letters (a-z) and digits (0-9).")
        return

    cracked_password, attempts, elapsed = brute_force_crack(target_password)

    if cracked_password:
        print("\nPassword cracked!")
        print(f"Cracked password: {cracked_password}")
        print(f"Attempts: {attempts}")
        print(f"Time taken: {elapsed:.6f} seconds")
    else:
        print("\nPassword not found within search space.")
        print(f"Attempts: {attempts}")
        print(f"Time taken: {elapsed:.6f} seconds")


if __name__ == "__main__":
    main()
