print("\nQ1a\n")
# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1

# A1a:

def divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

print(divisors(12))


print("\nQ1b\n")
# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function

# A1b:
def is_factor(a, b):
    return a in divisors(b) or b in divisors(a)

print(is_factor(4, 12))
print(is_factor(5, 12))


# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
# alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
#             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

# A2a:
def letter_position(letter):

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return alphabet.index(letter.lower()) + 1

print(letter_position("z"))


print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14

# A2b:
def name_to_id(name):

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    id_number = ""
    for letter in name.lower():
        if letter.isalpha():
            id_number += str(alphabet.index(letter))
    return id_number

print(name_to_id("bob"))


print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)

# A2c:
def id_to_password(name):

    id_number = name_to_id(name)
    digit_sum = sum(int(digit) for digit in id_number)
    return int(id_number) - digit_sum

print(id_to_password("bob"))


# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.

# A3a:
def is_prime(n):

    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(7))
print(is_prime(9))


print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit

# A3b:
def is_prime_safe(input_value):

    try:
        n = int(input_value)
        return is_prime(n)
    except ValueError:
        return False


print(is_prime_safe(7))
print(is_prime_safe("abc"))
print(is_prime_safe("11"))
