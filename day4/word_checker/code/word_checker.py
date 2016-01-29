# -*-coding: utf-8 -*-#


def words(data):
    data = data.strip().split()
    words = {}
    for word in data:
        try:
            word = int(word)
        except ValueError:
            pass
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1
    return words
