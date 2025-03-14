
i=0
j=2
k=4
ylist=[]
def main(x):
 mapx=x%4
 if mapx>=i and mapx<=j:
       y= (2**mapx)+5
       ylist.append(y)
       return y

    
 elif mapx>j and mapx<=k:
       y=(3*mapx)+1
       ylist.append(y)
       return y
 else:
    
    
         return mapx
     
print(main(2018)-main(9))



     

 
       
    
