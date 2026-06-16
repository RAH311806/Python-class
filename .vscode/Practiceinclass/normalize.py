#Give a list of names, normalize each name (strip whitespace, title case) and print the cleaned list.

names = [" rahul sah ", "MS Dhoni", "Spider Man", "COMPUTER" ]

cleaned = [name.strip().title() for name in names]

print (cleaned)
