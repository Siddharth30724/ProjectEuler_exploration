import random
import matplotlib.pyplot as plt


i=20000


ilist=[] 


 

nlist=[]


def A():
   global i
   
   if random.random()>0.49:
        i-=1
       
       
   else:
        i+=1
   
def B():
      global i


  
    
      if i%3==0:
       if random.random()>0.095:   
         i-=1
       else:
         i+=1
      else:
         if random.random()>0.745:
           i-=1
         else:
           i+=1
      
     
def C():
  global i


  for n in range(0,15001):
   nlist.append(n)
   random.choice([A,B])()
   ilist.append(i)

   
  


C()
plt.plot (nlist, ilist, linestyle='-', color='r', label="Turns vs Points")


plt.xlabel("turns")
plt.ylabel("points")
plt.title("Plot of X vs. Y (Iterated Values)")  
plt.legend()  
plt.grid(True)  
plt.show()

