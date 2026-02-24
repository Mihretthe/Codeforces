from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

import sys

sys.setrecursionlimit(10**8)

def solve():
    n, w = II()

    array = []

    for _ in range(n):
        weigh, value = II()
        array.append((weigh, value))
    

    memo = {}

    def dp(index, weigh):


        if (index, weigh) in memo:
            return memo[(index, weigh)]
        
        # print(index,weigh)

        if index >= n:
            memo[(index, weigh)] = 0
            return 0
        
        if weigh <= 0:
            memo[(index, weigh)] = 0
            return 0

        
        take = 0        

        if weigh - array[index][0] >= 0:
            take = array[index][1] + dp(index + 1, weigh - array[index][0])        

        leave = dp(index + 1, weigh)
        # else:
        memo[(index, weigh)] = max(take, leave)
        
        return memo[(index, weigh)]
 
 
    print(dp(0, w))
 
T = 1
for _ in range(T):
    solve()