from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from math import ceil

def solve():
    n = I()
    s = S()

    max_hash = 0
    running_hash = 0

    for i in range(n):
        val = s[i]
        if val == "*":
            max_hash = max(max_hash, running_hash)
            running_hash = 0
        else:
            running_hash += 1

    max_hash = max(max_hash, running_hash)

    print(ceil(max_hash / 2))

 
 
 
 
T = I()
for _ in range(T):
    solve()