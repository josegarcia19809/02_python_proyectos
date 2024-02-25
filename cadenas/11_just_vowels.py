def justvowels(string):
    for letter in string:
        if letter in "aeiou":
            print(letter, end=" ")


def justvowels2(string):
    for letter in string:
        if letter in "aeiouAEIOU":
            print(letter, end=" ")


def justvowels3(string):
    for letter in string:
        if letter.lower() in "aeiou":
            print(letter, end=" ")


def notvowels(string):
    for letter in string:
        if not letter in "aeiou":
            print(letter, end=" ")


justvowels("hello world")
print()
notvowels("hello world")
print()
justvowels2("Old Brown Cow")
print()
justvowels3("Old Brown Cow")
print()
