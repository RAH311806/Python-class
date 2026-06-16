#Write a program that a sentence and counts the number of vowels and consonants.

sentence = input("Enter a sentence")
vowels = 0
consonants = 0

for char in sentence.lower():
    if char.isalpha():
        vowels += 1
    else:
        consonants += 1

print(f"vowels: {vowels}")
print(f"Consonants: {consonants}")
            