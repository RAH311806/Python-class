import re

#NLP preprocessing Pipeline
text = "Hello! Rahul Sah 10.  "

# Step 1: Normalize
clean = text.lower().strip()

# Step 2: Remove punctuation
text = re.sub(r'[^\w\s]', '', text)

# Step 3: Tokenize
tokens = text.split()

# Step 4: Remove stop words (example)
stop_words = set(['the', 'is', 'in', 'and', 'to', 'a'])
tokens = [t for t in tokens if t not in stop_words]

print(tokens)  