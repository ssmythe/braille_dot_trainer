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
        "u": "\u2825",
        "v": "\u2827",
        "w": "\u283a",
        "x": "\u282d",
        "y": "\u283d",
        "z": "\u2835",
    }
    short_words = [
        "cat",
        "dog",
        "fox",
        "bee",
        "ant",
        "owl",
        "bat",
        "rat",
        "pig",
        "eel",
        "yak",
        "bug",
        "zip",
        "jam",
        "mix",
        "fun",
        "sun",
        "sky",
        "joy",
        "win",
        "pop",
        "buzz",
        "fizz",
        "jazz",
        "quiz",
        "whiz",
        "vex",
        "sly",
    ]
    longer_words = [
        "candy",
        "fluffy",
        "bouncy",
        "sparkle",
        "tricky",
        "doodle",
        "whimsy",
        "bubbly",
        "mellow",
        "fuzzy",
        "quirky",
        "jingle",
        "dazzle",
        "puzzle",
        "fidget",
        "snappy",
        "glitter",
        "sizzle",
        "mystic",
        "poppet",
        "jolly",
        "mirth",
        "snazzy",
        "zingy",
        "zapper",
        "quiver",
        "glimmer",
        "breezy",
    ]
    word_list = short_words + longer_words

    remaining_words = set(word_list)
    total_attempts = 0
    correct_attempts = 0

    print(
        "Braille a-z Word Trainer - Identify the word corresponding to the given Braille characters. Press Enter to quit."
    )

    while remaining_words:
        word = random.choice(list(remaining_words))
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
