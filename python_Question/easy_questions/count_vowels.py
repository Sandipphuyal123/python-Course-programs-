def count_vowels(s):
    vowels = 'aeiou'
    return sum(1 for c in s.lower() if c in vowels)

# Test
print(count_vowels('hello world'))
print(count_vowels('Python'))
print(count_vowels('AEIOU'))