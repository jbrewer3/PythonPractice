LOW = 1
HIGH = 1000

def hilo(answer, low , high):
    guesses = 1
    while True:
        guess = low + (high - low) // 2

        if guess < answer:
            low = guess + 1
        elif guess > answer:
            high = guess -1

        elif guess == answer:

            return guesses

        guesses += 1

for number in range(LOW, HIGH + 1):
    number_of_guesses = hilo(number, LOW, HIGH)
    print("{} guessed in {}".format(number, number_of_guesses))
