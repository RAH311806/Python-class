for n in range(1, 501):
    div_sum = 0
    for d in range(1, n):
        if n % d == 0:
            div_sum += d
    if div_sum == n:
        print(n, end=" ")
        