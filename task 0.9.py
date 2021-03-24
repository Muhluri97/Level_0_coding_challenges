def vowel(word):
    vowels = 'aeiou, AEIOU'
    for vowel in vowels:
        if vowel in word:
            print(vowel, end = ", ")
