text = "Hello, World!"

# 1. Clean and normalize
clean = text.strip().lower()
print(clean)

# 2. Replace & split
words = clean.replace(",", "").split()
print(words)  # ['hello', 'world']

# 3. Reverse a string
rev = clean[::-1]
print(rev)

# 4. Count word frequency
sentence = "hello world hello"
word_freq = {w: sentence.split().count(w) for w in set(sentence.split())}
print(word_freq)