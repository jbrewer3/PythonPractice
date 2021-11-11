choice = "-"

while choice != "0":
    if choice in "12345":
        print("You chose {}".format(choice))
    else:
        print("Please chooe you option form the list below: ")
        print("1:\tLearn Python")
        print("2:\tLearn Java")
        print("3:\tgo swimming")
        print("4:\thave dinner")
        print("5:\tgo to bed")
        print("0:\texit") 
choice = input()