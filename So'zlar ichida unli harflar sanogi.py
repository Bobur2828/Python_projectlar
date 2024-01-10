def unli_harflar(word_list):
    unli_harflar = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    b = {}
    c=[]  # kod kop bo'lishi mumkin lekin kalta kod bo'lsa unli harflar soni bir hil 
    d=0   # bo'lsa faqatgina bitta sozni olib beryatgandi shunga sal kopaytirvordim 
    x=[]
    for word in word_list:
        unli = []
        for harf in word:
            if harf in unli_harflar:
                unli.append(harf)
                b[word] = len(unli)
    for key,val in b.items():
        c.append(val)
        d=max(c)
    for key,val in b.items():
        if val==d:
            x.append(key)
    return(f"Eng kop unli harflar ishlatilgan so'z(lar) {x} unli harflar soni {d} ta")            
print(unli_harflar(['hello', 'world', 'salom', 'dunyo']))

# Natija   
# Eng kop unli harflar ishlatilgan so'z(lar) ['hello', 'salom', 'dunyo'] unli harflar soni 2 ta