def char_after_before(word, letters):
    n = len(letters)
    counter = 0
    result = ""
    for let in word:
        if  let == letters[0]:
            position = counter
            result += word[position - 1]
            result += word[position + 1 + (n - 1)]
        counter += 1
    return result
