def mario(a:int, b:int, c:int) :
    return c-(b//a) if b//a<=c else 0
    
for _ in range(int(input())) :
    x, y, z = map(int, input().split())
    print(mario(x, y, z))
    