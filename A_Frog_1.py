from sys import stdin
import sys

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from math import inf

sys.setrecursionlimit(10**7)
def solve():

    n = I()
    a = IL()
    
    memo = {}

    def dp(index):

        if index in memo:
            return memo[index]

        if index >= n - 1:
            return 0
        
        one = abs(a[index] - a[index + 1]) + dp(index + 1) if index + 1 < n else inf
        two = abs(a[index] - a[index + 2]) + dp(index + 2) if index + 2 < n else inf
        
        memo[index] = min(one, two)

        return memo[index]

    print(dp(0))



 
 
 
T = 1
for _ in range(T):
    solve()


