#!/usr/bin/env python

import random

def braille_trainer():
    braille_dict = {
        "u": "\u2825",
        "v": "\u2827",
        "w": "\u283a",
        "x": "\u282d",
        "y": "\u283d",
        "z": "\u2835",
    }
    remaining_chars = set(braille_dict.keys())
    total_attempts = 0
    correct_attempts = 0

    print(
        "Braille u-z Character Trainer - Identify the letter corresponding to the given Braille character. Press Enter to quit."
    )

    while remaining_chars:
        letter = random.choice(list(remaining_chars))
        braille_char = braille_dict[letter]
        user_input = input(f"Character '{braille_char}': ")

        if user_input == "":
            break

        total_attempts += 1
        if user_input.lower() == letter:
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
