def filter_anagrams(word, words):
    sorted_word = sorted(word)
    return [w for w in words if sorted_word == sorted(w)]

print(filter_anagrams('abba',  ['aabb', 'abcd', 'bbaa', 'dada'] ))