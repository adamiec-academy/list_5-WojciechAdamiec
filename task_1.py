def longest_word():
    longest_word = ""
    
    for line in open("words.txt", encoding="utf-8"):
        word = line.strip()
        
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word
