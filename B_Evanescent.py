from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import Counter
from math import inf

def solve():
    n = I()
    s = S()

    
    collect = []
    

    for i in range(n):
        letter = s[i]

        if collect and collect[-1][0] == letter:
            letter, count = collect.pop()
            collect.append((letter, count + 1))
        else:
            collect.append((letter, 1))

    mini = inf

    for i in range(len(collect)):
        if  i == 0 or i == len(collect) - 1:
            continue
        else:
            letter, count = collect[i]
            if count == 1:
                
                bletter, bcount = collect[i - 1]
                aletter, acount = collect[i + 1]

                if bletter == aletter:
                    mini = min(mini, len(collect) - 2)
                else:
                    mini = min(mini, len(collect) - 1)

    print(mini if mini != inf else len(collect))





    
 
 
 
T = I()
for _ in range(T):
    solve()