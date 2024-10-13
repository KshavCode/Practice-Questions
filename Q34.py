# MY CODE

def cards(a:int, b:int) :
    shortest = 0
    if a == 0 or b == 0 or a == b:
        return 0
    if a > b :
        shortest = b
    else :
        shortest = a
    if abs(a-b) < shortest :
        shortest = abs(a-b)
    return shortest
for _ in range(int(input())) :
    x, y = map(int, input().split())
    print(cards(x, y))
    
    
    
# BEST CODE
for i in range(int(input())):
    n, x = map(int, input().split())
    if x!=n:
        print(min(x, n-x))
    else:
        print(0)