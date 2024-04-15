import csv

with open('common_english_words.csv') as data:
    words = data.readlines()
    words_clean = []
    for word in words:
        new_word = (word.split(' '))
        word = new_word[0]
        words_clean.append(word)

    words_cleaner = words_clean

