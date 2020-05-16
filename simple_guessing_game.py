# simple guessing game


secret_word = "hello"
guess = ""
guess_count = 0

while guess != secret_word:
    guess = input("Enter your guess:")
    if guess != secret_word:
        guess_count += 1

    if guess_count == 3:
        print("you lost")
        break

if guess_count < 3:
    print("you win")


def raise_to_power(base_num, pow_num):
    result = 1
    for num in range(pow_num):
        result = result * base_num
    return result


print(raise_to_power(2, 2))


