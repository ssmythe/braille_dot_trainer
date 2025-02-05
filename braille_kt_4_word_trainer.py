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
        "Braille k-t Word Trainer - Identify the word corresponding to the given Braille characters. Press Enter to quit."
    )

    while remaining_words:
        word = random.choice(list(remaining_words))
        # Build the Braille representation for the word.
        braille_word = "".join(braille_dict[letter] for letter in word)
        user_input = input(f"Word '{braille_word}': ")

        if user_input == "":
            break

        total_attempts += 1
        if user_input.lower() == word:
            print("✔ Correct!")
            correct_attempts += 1
            remaining_words.remove(word)
        else:
            print(f"✘ Incorrect. The correct answer is '{word}'.")

    if total_attempts > 0:
        accuracy = (correct_attempts / total_attempts) * 100
        print(
            f"\nSession ended. Accuracy: {accuracy:.2f}% ({correct_attempts}/{total_attempts})"
        )
    else:
        print("\nNo attempts made.")


if __name__ == "__main__":
    braille_trainer()
