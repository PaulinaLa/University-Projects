def krzyzyk(n):
 for i in range(3*n):
   if (0<=i<n or 2*n<=i<3*n):
     print(" "*n+"*"*n+" "*n)
   else:
     print("*"*3*n)
print()


