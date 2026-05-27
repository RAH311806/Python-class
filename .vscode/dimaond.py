n = int(input("N: "))

# Top half
for i in range(1, n+1):
    print(" "*(n-1) + (str(i) +" " ) *i )

    # Bottom half

    for i in range(n-1, 0, -1):
            print(" "*(n-1) + (str(i) +" " ) *i )
