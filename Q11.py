N = int(input())
M1 = int(input())
M2 = M1

# # CONDITIONS TO SOLVE ---> 
# when y = F, x = (F*2) - y 
# check if left pairs are less than number of friends

# MY VERSION
if M1 < N : 
    buy_more_left = N - M1
else : 
    buy_more_left = 0

M1 = N 
right = N*2 - M1

print(right+buy_more_left)



# BETTER VERSION
if N <= M2:
    print('We need to buy',N,'shoes')
else:
    print('We need to buy',(2*N-M2),'shoes')