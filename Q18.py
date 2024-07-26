# MY CODE
def fun(a, b) :
    c = a%6
    if c==0 :
        result = (a//6)*b
    else :
        result = ((a//6)+1)*b
    return result

answerlist = []
for i in range(int(input())) :
    A, B = map(int, input().split())
    answerlist.append(fun(A, B))

for x in answerlist :
    print(x)


# BEST CODE     
import math
t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    n=math.ceil(n/6)
    print(n*x)