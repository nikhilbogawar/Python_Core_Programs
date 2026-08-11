print("Numbers from 1 to N")
def gen_numbers(n):
    for i in range(1, n+1):
        yield i
for num in gen_numbers(5):
    print(num)

print("Even Numbers from 1 to N")
def gen_even(n):
    for i in range(2, n+1, 2):
        yield i
for num in gen_even(10):
    print(num)

print("Characters of a string")
def gen_chars(s):
    for ch in s:
        yield ch
for ch in gen_chars("Hello"):
    print(ch)


print("Characters of a string in a reverse order")
def gen_reverse_chars(s):
    for ch in reversed(s):
        yield ch
for ch in gen_reverse_chars("Hello"):
    print(ch)


print("Only vowels in a string")
def gen_vowels(s):
    vowels = "aeiouAEIOU"
    for ch in s:
        if ch in vowels:
            yield ch
for v in gen_vowels("Beautiful Day"):
    print(v)

print("Only digits present in a string")
def gen_digits(s):
    for ch in s:
        if ch.isdigit():
            yield ch
for d in gen_digits("abc123xyz45"):
    print(d)

print("Square element in list")
def gen_squares(lst):
    for num in lst:
        yield num * num
for sq in gen_squares([1,2,3,4]):
    print(sq)

print("Digits from an integer one by one")
def gen_int_digits(n):
    for ch in str(n):
        yield int(ch)
for d in gen_int_digits(12345):
    print(d)

print("Cumulative sum of numbers in a list")
def gen_cumulative_sum(lst):
    total = 0
    for num in lst:
        total += num
        yield total
for cs in gen_cumulative_sum([1,2,3,4]):
    print(cs)
