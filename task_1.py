def longest_word():
    longest_word = None
    longest_length = 0
    for line in open("words.txt"):
        word = line.strip()
        word_len = len(word)
        if word_len > longest_length:
            longest_length = word_len
            longest_word = word
    return longest_word
