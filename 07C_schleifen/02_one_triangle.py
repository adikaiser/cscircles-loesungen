n=int(input())
for i in range(0,n):
   S = ''
   for j in range(n,0,-1):
      S = n * '1'
   n = n - 1 
   print(S)
