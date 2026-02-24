from sys import stdin
import sys

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

sys.setrecursionlimit(10**7)

def solve():
    n = I()

    days = []

    for _ in range(n):
        a = IL()
        days.append(a)
    
    memo = {}
    def dp(index, prev):

        if (index, prev) in memo:
            return memo[(index, prev)]

        if index >= n:
            return 0
        
        a, b, c = 0, 0, 0

        if prev == 0:
            b = days[index][0] + dp(index + 1, 1)
            c = days[index][0] + dp(index + 1, 2)

        elif prev == 1:
            a = days[index][1] + dp(index + 1, 0)
            c = days[index][1] + dp(index + 1, 2)

        else:
            b = days[index][2] + dp(index + 1, 1)
            a = days[index][2] + dp(index + 1, 0)
            
        memo[(index, prev)] = max(a, b, c)
        return memo[(index, prev)]
    

    print(max(dp(0, 0), dp(0, 1), dp(0, 2)))
 
 
 
T = 1
for _ in range(T):
    solve()