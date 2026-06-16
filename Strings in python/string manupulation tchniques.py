text = " Hello World!"

# 1. Clean and normalize
clean = text.strip().lower()
print(clean)         #hello, world!

# 2. Replace & split
words = clean.replace(",", "").split()
print(words)        #['hello', 'world!']

# 3. Reverse a string
rev = clean[::-1]
print(rev)          #!dlrow ,olleh