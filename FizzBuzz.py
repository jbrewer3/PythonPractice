def FizzBuzz(number: int) -> str:
    if i % 3 == 0 and i % 5 ==0:
        return("FizzBuzz")
    elif i % 3 == 0:
        return("Fizz")
    elif i % 5 == 0:
        return("Buzz")
    else:
        return str(number)


for i in range(1, 101):
    print(FizzBuzz(i))

