def is_anagram(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    return sorted(s1) == sorted(s2)

# Test
print(is_anagram('listen', 'silent'))
print(is_anagram('hello', 'world'))
print(is_anagram('Dormitory', 'dirty room'))