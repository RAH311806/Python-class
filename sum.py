num = int(input("Enter a number: "))
total = 0

for digit in str(num):
    total += int(digit)
    
print("The sum of the digits is:", total)