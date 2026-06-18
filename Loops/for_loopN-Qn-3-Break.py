# Nested For Loop to check if the content in the list - 
# - have vowels or not 

words = ['Sky', 'zed', 'IAmNotInDangerSkylerIAmTheDanger', 'Nicholas', 'Rice']

for word in words:
    for letter in word:
        if letter.lower() in 'aeiou':
            print(f'{word} has {letter} vowel')
            break
    else:
        print(f"{word} doesn't have a vowel inside it")