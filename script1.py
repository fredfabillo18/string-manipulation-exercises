def sliding_window(text, n):
    phrase = []
    splitted_text = text.split() #list of words
    for index in range(0, len(splitted_text), n):
        phrase.append(" ".join(splitted_text[index:index+n]))
    return phrase

sample_text = "oh my god im so inlove i found you finally"
print(sliding_window(sample_text, 2))

