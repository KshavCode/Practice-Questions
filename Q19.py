def passOrfail(a:int, b:int, c:int) :
    return "YES" if (a*b)/2 < c else "NO"

for i in range(int(input())) :
    a, b, c = map(int, input().split())
    print(passOrfail(a, b, c))