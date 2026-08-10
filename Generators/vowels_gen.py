def yield_vowels(text: str):
    vowels = set("aeiouAEIOU")
    for char in text:
        if char in vowels:
            yield char
v1=yield_vowels("If you miss the train")
print(next(v1))
print(next(v1))
print(next(v1))
print(next(v1))
print(next(v1))
print(next(v1))
print(next(v1))