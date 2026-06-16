def analyze_text(text):
    """Analyzes a given text  string and return statistics."""
    cleaned = text.lower().strip()
    words = clean. split()
    chars = [c for c in clean if c.isalpha()]
    vowels = [c for c in chars if c in 'aeiou']
    sentences = text.split('.')

    # Word frequency
    freq = {w: words.count(w) for w in set(words)}
    top3 = sorted(freq, key=lambda w: freq[w], reverse=True)[:3]

    return {
        "total_chars"   : len(text),
        "total_words"   : len(words),
        "unique_words" : len(set(words)),
        "total_sentences" : len([s for s in sentences if s.strip()]),
        "vowels"      : len(vowels),
        "top_3_words" : top3,
        " is_all_lower" : text == text.lower()


    }

sample = "python is great. Python is fun and powerful."
result = anal



