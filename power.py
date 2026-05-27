base = int(input("Base: "))
exp = int(input("Exponent: "))

result = 1
for _ in range(exp):
    result = result * base
print("Result:", result)