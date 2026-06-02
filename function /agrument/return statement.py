#Return a single value 
def square(n):
    return n ** 2

#Return multiple values (tuple unpacking)
def min_max(nums):
    return min(nums), max (nums)

#Return ends the function immediately
def check_age(age):
    if age < 0:
        return "invalid"       
    if age < 18:
        return "minor"
    return "Adult"
# fffff