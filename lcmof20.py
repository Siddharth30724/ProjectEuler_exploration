import math

def LCM(n):
 Product=1
 for i in range(1,n+1):
   Product = (Product * i) // math.gcd(Product, i)
 return Product

print(LCM(20))