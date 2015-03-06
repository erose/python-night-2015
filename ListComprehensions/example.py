# This is a list of the first ten squares.
squares1 = []
for i in range(10):
    squares1.append(i**2)

# This is also a list of the first ten squares.
squares2 = [i**2 for i in range(10)]




n = 10
# Here's a list of n zeroes.
# ...done traditional style.
zeroes1 = []
for i in range(n):
    zeroes1.append(0)

# ...and listcomp style.
zeroes2 = [0 for i in range(n)]




# You can also attach a condition for inclusion.
# Traditional.
evens1 = []
for x in range(10):
    if x % 2 == 0:
        evens1.append(x)

# Listcomp.
evens2 = [x for x in range(10) if x % 2 == 0]




# The full synxtax is: [ <expression> for <name> in <iterable> if <condition>]

# Strings are also iterables.
vowels = [letter for letter in "fajitas" if letter in "aeiou"]
consonants = [letter for letter in "fajitas" if letter not in "aeiou"]
numbers = [int(c) for c in "1337 l1st c0mpr3h3ns10n sk1llz" if c.isdigit()]

# Don't forget files are iterable as well.
lines = [line.strip() for line in open("abc.txt") if line.strip()]

# You can do things with the results of listcomps once you've got them.
to_encode = "elbows"
rot128_encoded = "".join([chr((ord(c) + 128) % 256) for c in to_encode])

range_sum = sum([i for i in range(10)])

n = 2053
is_prime = not any([n % i == 0 for i in range(2, n)])




# You can use set and dictionary comprehensions in the same way.
# Just wrap them in curly braces/use a colon.
words = ["racecar", "icecream", "foof"]
palindromes_set = {word for word in words if word == word[::-1]}

ascii_dict = {c : ord(c) for c in "abcdefg"}

things = [1, -8, 0.0, "cat", None, lambda b: b + 2]
hashcodes_dict = {thing: hash(thing) for thing in things}

if __name__ == "__main__":
    pass
    # print("squares1:", squares1)
    # print("squares2:", squares2)

    # print("zeroes1:", zeroes1)
    # print("zeroes2:", zeroes2)

    # print("evens1:", evens1)
    # print("evens2:", evens2)

    # print("vowels:", vowels)
    # print("consonants:", consonants)
    # print("numbers:", numbers)
    # print("rot128_encoded:", rot128_encoded)
    # print("lines:", lines)
    # print("range_sum:", range_sum)
    # print("is_prime:", is_prime)

    # print("palindromes_set:", palindromes_set)
    # print("ascii_dict:", ascii_dict)
    # print("hashcodes_dict:", hashcodes_dict)