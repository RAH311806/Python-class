text = "hello world"
#for loop
for ch in text:
    print(ch, end=" ")
    #enum
for i, ch in enumerate(text):
    print(f"(i={i}: {ch})", end=' ')

    #comprehension
    vowels = [ch for ch in text if ch in 'aeiouAEIOU']
    print(f"\nVowels in text: {vowels}")