
def fibonacci(lim):
      evesum=0
      a,b=0,1
    
      while b<lim:
        a,b=b,a+b
        if b%2==0:
          evesum+=b
      return (evesum)

print(fibonacci(4000000))


       
       



    