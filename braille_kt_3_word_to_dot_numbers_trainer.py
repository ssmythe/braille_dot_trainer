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
    word_list = [
        "look",
        "took",
        "tool",
        "loop",
        "molt",
        "toll",
        "knot",
        "not",
        "ton",
        "pot",
        "top",
        "slot",
        "stool",
        "monk",
        "pork",
        "torn",
        "storm",
        "romp",
        "mop",
        "prom",
        "pronk",
        "knoll",
        "troll",
        "sort",
        "port",
        "sport",
    ]
    remaining_words = set(word_list)
    total_attempts = 0
    correct_attempts = 0

    print(
        "Braille k-t Dot Word Trainer - Enter the dot numbers for each letter separated by a space. Press Enter to quit."
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
