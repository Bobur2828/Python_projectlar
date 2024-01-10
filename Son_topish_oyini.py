def binary_search():
    bezak = "\n---------------------------------------------------\n         "
    bosh_joy = "         "
    savol = input("O'yinni boshlaymizmi? (Ha / Yo'q) ").capitalize()

    while savol == "Ha":
        x = input(f"{bezak}[A] soni dan [B] sonigacha bo'lgan sonlar\n{bosh_joy}ichida taxmin qilishingiz kerak\n{bosh_joy}[A] va [B] sonlarini kiriting. Misol uchun: \n{bosh_joy}{bosh_joy}[33,456]\n{bosh_joy}sonlar orasi vergul bilan kiritilsin ").split(',')
        if len(x) == 2:
            if x[0].isnumeric() and x[1].isnumeric():
                print(f"{bezak}{x[0]} sonidan {x[1]} gacha bo'lgan \n{bosh_joy}sonlar ichidan birini taxmin qiling")
                start = int(x[0])
                end = list(range(1, int(x[1]) + 1))  
                indeks = len(end) - 1
                sanoq = 0
                smaylik = "\U0001F604"
                while start <= indeks:
                    sanoq += 1
                    orta_indeks = start + (indeks - start) // 2
                    orta_qiymat = end[orta_indeks]

                    b = input(f"{bezak}Sizning taxminingiz==[--[{smaylik} {orta_qiymat} {smaylik}]--]\n{bosh_joy}To'gri bo'lsa {bosh_joy}----[OK]----,\n{bosh_joy}Kichik bo'lsa {bosh_joy}----[KICHIK]----,\n{bosh_joy}Katta bo'lsa {bosh_joy}----[KATTA]---\n{bosh_joy}commandasini kriting: ").capitalize()

                    if b == "Ok":
                        print(f"{bezak}     Siz o'ylagan son [{orta_qiymat}],\n{bosh_joy}va men uni [{sanoq}]ta urinishda topdim")
                        break
                    elif b == "Kichik":
                        indeks = orta_indeks - 1
                    elif b == "Katta":
                        start = orta_indeks + 1
                    else:
                        print("Noto'gri kommanda kiritdingiz. OK, Kichik yoki Katta kiriting.")
                    if indeks==0 or start==indeks+1:
                        print(f"{bezak}{bosh_joy} Siz meni aldashga urinmang\n{bosh_joy*2}G'irromlik qilmang")
                savol = input(f"{bezak}Yana bir martta o'ynaysizmi? (Ha / Yo'q) ").capitalize()

            else:
                print("Siz raqam kiritmadingiz.")
        else:
            print("[A] va [B] raqamlari da faqat 2 ta qiymat kiriting")
            savol = input(f"{bezak}Yana bir martta o'ynaysizmi? (Ha / Yo'q) ").capitalize()

    if savol == "Yoq":
        print("Afsus, birga o'ynashni xoxlagandik.")
    else:
        print("Noto'gri komanda kiritdingiz.")

binary_search()
