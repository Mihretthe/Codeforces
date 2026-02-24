def I(): return int(input())


T = I()

for _ in range(T):
    n = I()
    m = n // 2

    if n % 2:
        print(1 + (m *(m + 1)))
    else:
        print(1 + (m *(m + 1)) - m)

    
    

