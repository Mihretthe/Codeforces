from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from bisect import bisect_left

def solve():
    n, m = II()
    a = IL()
    b = IL()

    a.sort()

    if max(a) >= max(b) and min(a) <= min(b):
        # for every num in b count the one before it and the one after it
        before = [0] * n
        after = [0] * n

        for i in range(m):
            num = b[i]
            index = bisect_left(a, num)
            print(num, index)
            if index - 1 >= 0:
                before[index - 1] += 1
            if index < n:
                after[index] += 1

        # do prefix for a how much that num is needed before and after
        
        # before
        for i in range(n - 2, -1, -1):
            before[i] += before[i + 1]

        # after
        for i in range(1, n):
            after[i] += after[i - 1]

        print(before, after)


    else:
        print("NO")
 
 
 
 
T = I()
for _ in range(T):
    solve()