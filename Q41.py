# Memoization method
def grid(m:int, n:int, memo=dict()) :
    if m==n==1 :
        return 1
    if m==0 or n==0 :
        return 0
    string = ",".join([str(m), str(n)])
    if string not in memo :
        memo[string] = grid(m-1, n) + grid(m, n-1)
    return memo[string]

print(grid(2, 3))
print(grid(2, 1))
print(grid(4, 6))
print(grid(17, 18))
print(grid(54, 22))