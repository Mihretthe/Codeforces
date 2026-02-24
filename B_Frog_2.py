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

    n, k = II()
    a = IL()
    
    memo = {}

    def dp(index):

        if index in memo:
            return memo[index]

        if index >= n - 1:
            return 0
        
        mini = inf

        for i in range(index + 1, min(n, index + k + 1)):
            mini = min(mini, abs(a[i] - a[index]) + dp(i))
        
        memo[index] = mini

        return memo[index]

    print(dp(0))



 
 
 
T = 1
for _ in range(T):
    solve()


