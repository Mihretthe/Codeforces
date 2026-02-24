from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n = I()
    s = S()

    def next(string):
        if string == "mM":
            return "eE"
        elif string == "eE":
            return "oO"
        elif string == "oO":
            return "wW"
        else:
            return ""
    

    find = 'mM'

    for i in range(n):
        if s[i] not in find:
            if i > 0 and s[i] in next(find):
                find = next(find)
            else:
                print("NO")
                return 
    if find == "wW":
        print("YES")
    else:
        print("NO")

 
 
 
 
T = I()
for _ in range(T):
    solve()