import timeit
def topish(my_list):
    boshlar=[]
    takror=[]
    for i in my_list:
        if i not in boshlar:
            boshlar.append(i)
        else:
            takror.append(i)
    for element in boshlar:
        if element not in takror:
            yield element        
    return element

natija=(topish([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,
                22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,
                39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,56,57,
                58,59,60,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,
                22,23,24,25,26,27,28,29,31,32,33,34,35,36,37,38,
                39,40,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,56,57,
                58,59,60,]))
for i in natija:
    print(i)
vaqt = timeit.timeit(lambda: list(natija), number=100)
print(f"ketkan vaqt {vaqt}")
