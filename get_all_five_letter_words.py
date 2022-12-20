import random


def get_random_word():
    with open('5_letter_words.txt', 'r') as f:
        # Read the contents of the file into a string
        contents = f.read()
    # Split the string into a list of words
    word_list = contents.split('\n')
    return random.choice(word_list).lower()
