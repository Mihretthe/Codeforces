from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from bisect import bisect_left

def solve():
    n, k = II()
    a = IL()
    
    count = 0
    index = 0
    a.sort()

    for i in range(n):
        if (a[i] - k - index) >= 0:
            count += 1
            index += 1
    
    print(count)
 
 
 
 
T = I()
for _ in range(T):
    solve()