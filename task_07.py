def combine_anagrams(words_array):
    anagrams = []

    for word in words_array:
        sorted_word = ''.join(sorted(word.lower()))

        for group in anagrams:
            if sorted_word == ''.join(sorted(group[0].lower())):
                group.append(word)
                break
        else:
            anagrams.append([word])

    return anagrams

print(combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar", "creams", "scream"]))
