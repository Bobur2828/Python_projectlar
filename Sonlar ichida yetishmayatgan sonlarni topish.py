def kam_sonlar(a):
    
    
    x=[]
    z=[]
    for i in range(0,max(a)+1):
        if not i in a:
            x.append(i)
        else:
            z.append(i)        
    return f"Berilgan sonlar {sorted(z)},  Ular ichida yetishmayatgan sonlar {x}"
print(kam_sonlar([9,7,4,2,3,6]))