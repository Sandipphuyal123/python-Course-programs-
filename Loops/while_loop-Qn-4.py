# Secret Number Guessing game

secret_number = 5
guess = 0

while guess != secret_number:
    guess  = int(input("Enter your Guess: "))
    if guess != secret_number:
        print(f'your guess {guess} was wrong, Try again')

print(f'Your {guess} is correct!!')