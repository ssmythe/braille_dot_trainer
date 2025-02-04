#!/usr/bin/env python


import random


def braille_trainer():
    braille_dict = {
        "a": "\u2801",
        "b": "\u2803",
        "c": "\u2809",
        "d": "\u2819",
        "e": "\u2811",
        "f": "\u280b",
        "g": "\u281b",
        "h": "\u2813",
        "i": "\u280a",
        "j": "\u281a",
    }
    remaining_chars = set(braille_dict.keys())
    total_attempts = 0
    correct_attempts = 0

    print(
        "Braille aj Character Trainer - Identify the letter corresponding to the given Braille character. Press Enter to quit."
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
            print(f"✘ Incorrect. The correct answer is '{letter.upper()}'.")

    if total_attempts > 0:
        accuracy = (correct_attempts / total_attempts) * 100
        print(
            f"\nSession ended. Accuracy: {accuracy:.2f}% ({correct_attempts}/{total_attempts})"
        )
    else:
        print("\nNo attempts made.")


if __name__ == "__main__":
    braille_trainer()
