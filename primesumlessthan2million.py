def prime(num):
    if num<2:
      return False
    else:
     if num==2:
       return True
     if num%2==0:
      return False
     
     else:
    
      while True:
       for limit in range(3,int(num**0.5)+1,2):
         if num%limit==0:
            return False
       return True

def primesum():
 
 
 primes=0
 for num in range(1,2000000):
   if prime(num):
    primes+=num
    
 print(primes)

primesum()
 