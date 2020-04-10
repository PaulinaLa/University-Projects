
def kwadrat(n):
   for i in range(n):
      for j in range(n):   
         print ("*", end="")
      print()
      
def kwadrat2(n):
   for i in range(n):
      print (n * "#")
   print()
  
for i in range(5) :
   print("Przebieg:",i)
   print (20*"-")
   kwadrat(3+2*i)
      
for i in range(5,10):
   print ("Przebieg:",i)
   print (20 * "-")
   kwadrat2(i-2)
print()
