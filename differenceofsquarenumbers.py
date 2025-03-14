def one(i):
 
    sums=(i)*(1+i)//2
    sumsquare=sums**2
    return sumsquare
def two(i):
    squaresum=0
    for i in range(1,i+1):
        r=i**2
        squaresum+=r
    return squaresum
def difference(i):
  o=one(i)
  t=two(i)
  difference=o-t
  return difference
print (difference(100))
 