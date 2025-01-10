def count_words(string):
    string = string.lower()

    empty_string = ""
    for char in string:
        if char.isalpha() or char.isspace():
            empty_string += char 
        else:
            empty_string += " "
            
    words = empty_string.split()

    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1  
        else:
            word_count[word] = 1 

    return word_count

print(count_words("A man, a plan, a canal -- Panama"))
print(count_words("Doo bee doo bee doo"))
