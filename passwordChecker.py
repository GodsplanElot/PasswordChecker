#You can set the secret code to be any value with an input function ⚡

secret_code = 32099957
guess_attempts = 0
attempts_limit = 3

while guess_attempts < attempts_limit:
    guess = int (input(f"Enter Password(MAX Attempts '3' num only)==>? "))
    guess_attempts += 1
    if guess == secret_code:
        print('"Successful" Welcome')
        break
else:
    print('Max Attempt Reached')