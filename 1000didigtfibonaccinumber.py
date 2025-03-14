import sys
sys.set_int_max_str_digits(100000)
index=0


blist=[]
a, b = 0, 1  

while True:
    
    a, b = b, a + b 
    
    blist.append(b)
    
   
    if b>=10**999:
     
        print(len(blist))
        break
        
          




