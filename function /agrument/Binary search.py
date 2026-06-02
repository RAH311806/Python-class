#part1
#factorial - classic recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)   
    
    #fibonacci - tree recursion
def fibonacci(n):
    if n <= 1 :
     return n
    return fibonacci(n-1) + fibonacci(n-2) #recursive case


#part 2
# Binary search - divide and conquer recursion
def binary_search(arr, target, lo=0, hi=None):
    if hi is None:
        hi = len(arr) - 1
    if lo > hi:
        return -1 # target not found
    mid = (lo + hi) // 2
    if arr[mid] == target:
        return mid # target found
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, hi) # search in the right half
    else:
        return binary_search(arr, target, lo, mid - 1) # search in the left half
    print(factorial(5)) # Output: 120
print(fibonacci(10)) # Output: 55
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(arr, 5)) # Output: 4