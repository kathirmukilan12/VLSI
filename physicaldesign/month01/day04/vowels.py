def count_vowels(s):
    counts = {vowel: 0 for vowel in "aeiou"}

    for char in s.lower():
        if char in counts:
            counts[char] += 1

    return counts


print(count_vowels("hello world"))