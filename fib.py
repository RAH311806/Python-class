limit = int(input("Limit: "))
a, b = 0, 1

while a <= limit:
    print(a, end=" ")
    a, b = b, a + b
    