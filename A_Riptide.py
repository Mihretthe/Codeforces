from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def solve():
    a, b, c = II()

    count = 0

    def check(a, b, c, count):
        # print(a, b, c)
        if a == b or a == c or b == c:
            print(count)
            return "END"
        else:
            maxi = max(a, b, c) 
            mini = min(a, b, c)

            mid = [i for i in [a, b, c] if i != maxi and i != mini][0]

            val = check(maxi - 1, mid, mini + 1, count + 1)
            if val == "END":
                return "END"

    check(a, b, c, 0)





 
 
 
 
T = I()
for _ in range(T):
    solve()