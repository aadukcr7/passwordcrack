"""
Brute Force Password Simulation (Educational)
For Educational Purposes Only
"""

import itertools
import string
import time


def brute_force_crack(
    target_password: str,
    allowed_chars: str,
    max_length: int,
) -> tuple[str, int, float]:
    """Brute force a user-provided password locally (educational simulation only)."""
    attempts = 0
    start_time = time.perf_counter()

    for length in range(1, max_length + 1):
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
    target_password = input("Enter a password to test: ").strip()

    if not target_password:
        print("No password provided. Exiting.")
        return

    include_upper = input("Include uppercase letters? (y/N): ").strip().lower() == "y"
    include_symbols = input("Include symbols? (y/N): ").strip().lower() == "y"

    allowed_chars = string.ascii_lowercase + string.digits
    if include_upper:
        allowed_chars += string.ascii_uppercase
    if include_symbols:
        allowed_chars += string.punctuation

    max_length_input = input(
        "Max length to search (press Enter to use password length): "
    ).strip()
    if max_length_input:
        try:
            max_length = int(max_length_input)
        except ValueError:
            print("Invalid max length. Enter a positive integer.")
            return
        if max_length <= 0:
            print("Invalid max length. Enter a positive integer.")
            return
    else:
        max_length = len(target_password)

    allowed_set = set(allowed_chars)
    if any(ch not in allowed_set for ch in target_password):
        print("Invalid input for the selected character set.")
        return

    cracked_password, attempts, elapsed = brute_force_crack(
        target_password,
        allowed_chars,
        max_length,
    )

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
