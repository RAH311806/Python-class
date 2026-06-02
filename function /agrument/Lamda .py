# LAmda vs def - same thing, different Syntax
def square(x):  return x ** 2 
sq = lambda x:  x ** 2
print(sq(5))


# Lambda with sorted() - real AI use 
 students = 









# Lambda with map() and filter()
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,]
doubled = list(map(lambda x: x*2, nums))
evens = list(filter(lambda x: x%2==0, nums))
print(doubled)
print(evens)

# Lambda in ML - custom loss weight
loss_weight = lambda epoch:
