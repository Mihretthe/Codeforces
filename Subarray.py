from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import defaultdict

def solve():
    n, k = II()
    a = IL()
    counter = defaultdict(int)

    maxi = [0] * n
    maxi[-1] = a[-1]
    for i in range(n - 2, -1, -1):
        maxi[i] = max(a[i], maxi[i + 1])

    left = 0
    longest = 0

    for right in range(n):
        counter[a[right]] += 1
        if counter[maxi[right]] > k:
            while left < n and counter[maxi[right]] > k:
                counter[a[left]] -= 1
                left += 1
        longest = max(longest, right - left + 1)

    print(longest)
        
        



 
 
 
T = I()
for _ in range(T):
    solve()