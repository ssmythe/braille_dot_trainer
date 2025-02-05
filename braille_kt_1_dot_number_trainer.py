#!/usr/bin/env python

import random


def braille_trainer():
    braille_dict = {
        "k": "13",
        "l": "123",
        "m": "134",
        "n": "1345",
        "o": "135",
        "p": "1234",
        "q": "12345",
        "r": "1235",
        "s": "234",
        "t": "2345",
    }
    remaining_letters = set(braille_dict.keys())
    total_attempts = 0
    correct_attempts = 0

    print(
        "Braille k-t Dot Trainer - Enter the dot numbers for the given letter. Press Enter to quit."
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
