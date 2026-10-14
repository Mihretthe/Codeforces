
from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import defaultdict
from math import ceil

def solve():
    n = I()
    a = list(S())
    b = list(S())

    def check(a, b):

        evensa = [0,0]
        oddsa = [0,0]

        evensb = [0,0]
        oddsb = [0,0]

        for i in range(n):
            if i % 2:
                indexa = int(a[i])
                indexb = int(b[i])

                oddsa[indexa] += 1
                oddsb[indexb] += 1

            else:
                indexa = int(a[i])
                indexb = int(b[i])

                evensa[indexa] += 1
                evensb[indexb] += 1

        return not (oddsa != oddsb or evensa != evensb)
    


    if check(a, b):
        
        answer = 0
        needs_swap_ones = []
        actual_ones = defaultdict(list)
        for i in range(n):
            if a[i] != b[i]:
                if a[i] != "0":
                    needs_swap_ones.append(i)
                if b[i] == "1":
                    actual_ones[i % 2].append(i)

        count = 0
        indexo = 0
        indexe = 0
        for one in needs_swap_ones:
            if one % 2:
                count += (abs(actual_ones[1][indexo] - one)//2)
                indexo += 1
            else:
                count += (abs(actual_ones[0][indexe] - one)//2)
                indexe += 1


        print(count)


    else:
        print(-1)



T = I()
for _ in range(T):
    # print(_)
    solve()