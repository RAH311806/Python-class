n = int(input("N: "))
limit = int(input("Limit: "))   
count = 0

for i in range(1, limit + 1):
    if i % n == 0:
        count += 1
print("Count:", count)