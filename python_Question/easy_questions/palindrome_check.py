def palindrome_check(s):
    cleaned_string = s.replace(' ', '').lower()
    if cleaned_string == cleaned_string[::-1]:
        return True
    else:
        return False
print(palindrome_check('l  o   l'))