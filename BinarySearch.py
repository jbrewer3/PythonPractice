#binary search algorith is most effecient way of finding an item in ordered list
# Hi Lo Game
import random

answer = random.randint(0, 1000)
low = 1
high = 1000
input("Press ENTER to start ")
print(answer)
guesses = 1
while low != high:
    #print("\tguessing in the range of {} to {}".format(low, high))
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Should I guess higher or lower enter h or l, or c if my guess was correct ".format(guess)).casefold()
    if high_low == "h":
      low = guess + 1
      #guess higher the low end become 1 greater than the guess
    elif high_low == "l":
      high = guess - 1
      #guess lower the high end of the range becomes one less that the guess
    elif high_low == "c":
      print("I got it in {} guesses! ".format(guesses))
      break
    else:
      print("please enter h, l or c ")
    guesses += 1
else:
    print("You thought of the number {}".format(low))
    print("I got it in {} guesses".format(guesses))