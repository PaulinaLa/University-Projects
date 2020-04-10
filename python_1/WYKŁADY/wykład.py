D = {
  'girl' : 'dziewczyna', 
  'boy' : 'chłopiec', 
  'house' : 'dom', 
  'car' : 'samochód'
}


print ('Angielskie girl to', D['girl'])



D['table'] = 'stół'
D['ass'] = "dupa"
print (D)
"""
for k in D:
  print ('Klucz', k, D[k]) #szybkie


  
print (list(D), len(D))


for k,v in D.items():
  print (k,v)

print (D.keys())
print (D.values())  

for k in ['a', 'the', 'girl']:
  print (k, k in D) #UWAGA: szybkie

"""
