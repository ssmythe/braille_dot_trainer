#!/usr/bin/env python

import random


def braille_trainer():
    braille_dict = {
        "k": "\u2805",
        "l": "\u2807",
        "m": "\u280d",
        "n": "\u281d",
        "o": "\u2815",
        "p": "\u280f",
        "q": "\u281f",
        "r": "\u2817",
        "s": "\u280e",
        "t": "\u281e",
    }
    remaining_chars = set(braille_dict.keys())
    total_attempts = 0
    correct_attempts = 0

    print(
        "Braille k-t Character Trainer - Identify the letter corresponding to the given Braille character. Press Enter to quit."
    )

    while remaining_chars:
        letter = random.choice(list(remaining_chars))
        braille_char = braille_dict[letter]
        user_input = input(f"Character '{braille_char}': ")

        if user_input == "":
            break

        total_attempts += 1
        if user_input == letter:
            print("✔ Correct!")
            correct_attempts += 1
            remaining_chars.remove(letter)
        else:
            print(f"✘ Incorrect. The correct answer is '{letter}'.")

    if total_attempts > 0:
        accuracy = (correct_attempts / total_attempts) * 100
        print(
            f"\nSession ended. Accuracy: {accuracy:.2f}% ({correct_attempts}/{total_attempts})"
        )
    else:
        print("\nNo attempts made.")


if __name__ == "__main__":
    braille_trainer()
