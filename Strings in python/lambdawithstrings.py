#lambda for strings transformations
upper = lambda s: s.upper()
print(upper("hello world"))  # HELLO

#Sorting strings by length
words = ["apple", "banana", "kiwi", "grapefruit"]
words.sort(key=lambda w: len(w))
print(words)

#Using map() with lambda
names = ["Alice", "Bob", "Charlie"]
titled = list(map(lambda n: n.title(), names))
print(titled)

#Filter: words longer than 4 chars
long_words = list(filter(lambda w: len(w) > 4, words))
print(long_words)
