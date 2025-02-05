#!/usr/bin/env python

import random

def braille_trainer():
    braille_dict = {
        "u": "136",
        "v": "1236",
        "w": "2456",
        "x": "1346",
        "y": "13456",
        "z": "1356",
    }
    remaining_letters = set(braille_dict.keys())
    total_attempts = 0
    correct_attempts = 0

    print(
        "Braille u-z Dot Trainer - Enter the dot numbers for the given letter. Press Enter to quit."
    )

    while remaining_letters:
        letter = random.choice(list(remaining_letters))
        answer = braille_dict[letter]
        user_input = input(f"Letter '{letter}': ")

        if user_input == "":
            break

        total_attempts += 1
        if user_input == answer:
            print("✔ Correct!")
            correct_attempts += 1
            remaining_letters.remove(letter)
        else:
            print(f"✘ Incorrect. The correct answer is {answer}.")

    if total_attempts > 0:
        accuracy = (correct_attempts / total_attempts) * 100
        print(
            f"\nSession ended. Accuracy: {accuracy:.2f}% ({correct_attempts}/{total_attempts})"
        )
    else:
        print("\nNo attempts made.")

if __name__ == "__main__":
    braille_trainer()
