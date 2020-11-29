 
''' Solution 1 '''
 
n = int(input())
 
load = list(map(int, input().split()))
 
x = 5
 
 
interval = load[-1::x]
 
for i in interval:
 
   if i<50:
       print(n/2)
   else:
       print((2*n)+1)
