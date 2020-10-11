
def filtro(elem):
    return (elem > 0)

f = [1,-3,2,-7,-8,-9,10]

lr = filter(filtro,f)

print (f)
for x in lr:
  print(x) 
