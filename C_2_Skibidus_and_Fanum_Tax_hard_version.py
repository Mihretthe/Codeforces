from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from bisect import bisect_left, bisect_right

def solve():
    n, m = II()
    a = IL()
    b = IL()

    b.sort()
    
    for i in range(1, n):
        num = a[i]
        before = a[i - 1]

        calc = num + before

        index = bisect_left(b, calc)
        if index < m:
            val = b[index] 
        else:
            continue
        if i == 0:
            a[i] = max(a[i], val)
        elif val > a[i] and a[i - 1] >= val:
            a[i] = val
        elif a[i - 1] < a[i]:
            a[i] = val


 
    print(a)
 
 
T = I()
for _ in range(T):
    solve()