def poweroftwo(i):
    sumlist=0
    
    num=2**i
    strnum=str(num)
        
    for digit in range(len(strnum)):
        sumlist+=int(strnum[digit])
    return sumlist
print(poweroftwo(1000))
