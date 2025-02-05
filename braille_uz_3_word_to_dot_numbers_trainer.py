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
    word_list = [
        "wux",
        "vux",
        "zux",
        "xyzz",
        "uv",
        "wvy",
        "yx",
        "zwy",
        "wxy",
        "zwyx",
    ]
    remaining_words = set(word_list)
    total_attempts = 0
    correct_attempts = 0

    print(
        "Braille u-z Dot Word Trainer - Enter the dot numbers for each letter separated by a space. Press Enter to quit."
    )

    while remaining_words:
        word = random.choice(list(remaining_words))
        # Build the dot representation for the word by looking up each letter.
        dot_representation = " ".join(braille_dict[letter] for letter in word)
        user_input = input(f"Word '{word}': ")

        if user_input == "":
            break

        total_attempts += 1
        if user_input == dot_representation:
            print("✔ Correct!")
            correct_attempts += 1
            remaining_words.remove(word)
        else:
            print(f"✘ Incorrect. The correct answer is '{dot_representation}'.")

    if total_attempts > 0:
        accuracy = (correct_attempts / total_attempts) * 100
        print(
            f"\nSession ended. Accuracy: {accuracy:.2f}% ({correct_attempts}/{total_attempts})"
        )
    else:
        print("\nNo attempts made.")

if __name__ == "__main__":
    braille_trainer()
