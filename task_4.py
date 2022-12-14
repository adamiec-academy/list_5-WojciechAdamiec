def reversed_words():
    result = []

    words = set()

    for word in open("words.txt", encoding="utf-8"):
        words.add(word.strip())


    for word in words:
        rev_word = word[::-1]
        if rev_word in words and rev_word != word:
            result.append(tuple(sorted((word, rev_word))))


    result = list(set(result))
    result.sort()
    return result
