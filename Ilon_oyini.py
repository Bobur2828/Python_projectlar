a=input("O'yinni boshlaymizmi Javob Ha/Yo'q")
def ilon_oyin(a):
    
    tepa={2:38,7:14,8:31,15:26,28:84,21:42,36:44,51:67,71:91,78:98,87:94}
    pas={16:6,46:25,49:11,62:19,64:60,74:53,89:68,92:88,95:75,99:80}
    if a=="ha" or a=="Ha" or a=="hA" or a=="HA":
        sanoq=0
        a=0
        ball=a
        while not a>=100:
            b=int(input("Sakrashlar sonini kiriting"))
            if b<10:
                print(f"siz [{a}]chi xonadan [{b}] marta sakradiz")
                a=a+b
                for k,v in tepa.items():
                    if k==a:
                        print(f"siz [{a}]chi xonadasiz")
                        a=(a+v)-a
                        print(f"uraa [{a}]chi xonaga ko'tarildingiz ")
                for k,v in pas.items():
                    if k==a:
                        print(f"siz [{a}]chi xonadasiz")
                        a=v
                        print(f"afsus [{a}]chi xonasiga tushib qoldingiz")
                print(f"Siz [{a}]chi xonadasiz")  
            else:
                print("10 dan pas son kiriting")
            sanoq=sanoq+1          
        print(f"Tabriklaymiz  siz {sanoq} urinishda yutdingiz")
    else:
        print("Afsus siz bilan oynab bo'lmas ekan")
ilon_oyin(a)