def Hours(a:int, b:int) :
    return 4*a+b
    
for i in range(int(input())) :
    a, b = map(int, input().split())
    print(Hours(a, b))