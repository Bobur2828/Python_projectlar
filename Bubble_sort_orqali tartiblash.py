def bubble_sort(a):
    sanoglar = {}
    b=[]
    d={}
    for element in a:
        b.append(element)
        if element in sanoglar:
            sanoglar[element] += 1
        else:
            sanoglar[element] = 1
    
    for key, value in sanoglar.items():
        if key >= 2 and value % 2 == 0:
            d.update({key:value})        
            b.extend([int(str(key)[::-1])] * value)
            for i in b:
                if key == i:
                    b.remove(key)
    
    indeks=len(b)

    for i in range(indeks-1):
        for j in range(0, indeks - 1):
            if b[j] > b[j + 1]:
                b[j], b[j+1]=b[j+1], b[j]
    return(f"Natija {b},va taroriy elementlar va takror sanogi{d}")
print(bubble_sort([1,1,23,56,23,48,23,98,92,56,74,23]))
# Natija 
# [1, 1, 32, 32,,32,32 48, 65, 65, 74, 92, 98],va taroriy elementlar va takror sanogi{23: 4, 56: 2}