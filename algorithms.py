def fizz_buzz():
    for i in range(1, 101):
        if (i % 3 == 0) and (i % 5 == 0):
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# fizz_buzz()


def palindrome(word):
    word = word.lower()
    return word[::-1] == word

# print(palindrome("Level"))
# print(palindrome("Stage"))


def anagram(w1, w2):
    word1 = w1.lower()
    word2 = w2.lower()
    return sorted(word1) == sorted(word2)

# print(anagram("Lamp", "Palm"))
# print(anagram("Stone", "River"))
