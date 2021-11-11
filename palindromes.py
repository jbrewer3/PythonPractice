# Reads the same backwards as it does forwards

def palindrome_sentence(sentence):
    string = ''
    for char in sentence:
        if char.isalnum():
            string += char
    return string[::-1].casefold() == string.casefold()

word = input("Please enter a word to check: ")

if palindrome_sentence(word):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' ins not a palindrome".format(word))
