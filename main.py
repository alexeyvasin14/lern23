def single_root_words(root_word, *other_words):
    same_words = []
    for word in other_words:
        if (root_word.lower().find(word.lower()) >= 0) or (word.lower().find(root_word.lower()) >= 0):
            same_words.append(word)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies', 'ich')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)


