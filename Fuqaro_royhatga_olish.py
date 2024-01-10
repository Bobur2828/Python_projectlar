# shunchaKI RUN QILING 

class Person:  
    eng_letters = 'abcdefghijklmnopqrstuvwxyz'
    top_lettersK = eng_letters.upper()

    def __init__(self, fio, age, phone, passport,pochta,card):
        self.validate_fio(fio)
        self.validate_age(age)
        self.validate_phone(phone)
        self.validate_passport(passport)
        self.validate_pochta(pochta)
        self.validate_card(card)
        self.__fio = fio
        self.__age = age
        self.__phone = phone
        self.__passport = passport
        self.__pochta = pochta
        self.__card = card

    @classmethod
    def validate_fio(cls, fio):
        if type(fio) != str:
            raise TypeError("Kiritilyatgan malumot tekst ko'rinishida bolishi kerak")
        names = fio.split()

        if len(names) != 4:
            raise TypeError("Kiritilgan malumotda nimadir yetishmayapti yoki ortiqcha")

        letters = cls.eng_letters + cls.top_lettersK

        for name in names:
            if len(name.strip(letters)) != 0:
                raise TypeError("Malumot faqat  English alifbosida kiritilsin")
                        

    @classmethod
    def validate_age(cls, age):
        if type(age) != int:
            raise TypeError("Malumot raqam shaklida kiritilsin")
        if age >= 120 or age < 16:
            raise TypeError("Yoshingiz mos kelmaydi")


    @classmethod
    def validate_phone(cls, phone):
        if type(phone) == int:
            phone = str(phone)
        if phone[1:11].isdigit():
            if len(phone) != 13:
                raise TypeError("Raqamlar kam yoki kop kiritilgan: +99891237274")
            if phone[0]!="+":
                raise TypeError("Raqam boshida  + belgisini orniga boshqa narsa yozdiz ")
        else:
            raise TypeError("Telefon nomer  faqat raqamda kiritilsin")

    @classmethod
    def validate_passport(cls, passport):
        if len(passport) != 9:
            raise TypeError("Pasport seriya va raqamlari 9 tadan oshmasligi kerak")
        if not passport[:2].isupper():
            raise TypeError("Passport seriyani faqat katta harflarda kiriting")
        if not passport[2:].isdigit():
            raise TypeError("Passport raqamlarini faqat raqamlarda kiriting")
    


    @classmethod
    def validate_pochta(cls,pochta):
        if not pochta.endswith("@mail.ru") and not pochta.endswith("@gmail.com") and not pochta.endswith("@inbox.ru"):
            
            raise TypeError("Biz faqat @mail.ru, @inbox.ru, @gmail.com  pochtalarini qabul qilamiz ")
        
    @classmethod
    def validate_card(cls,card):
        if type(card)==int:
            card=str(card)
        if len(card)!=16:
            raise TypeError("Karta raqamini kam yoki ko'p kiritib yubordingiz")
        if not card.startswith("8600") and not card.startswith("9860"):
            raise TypeError("Biz faqat UzCard va Humo kartalaridan to'lov qabul qilamiz")


    @property
    def fio(self):
        return self.__fio


    @fio.setter
    def fio(self, new_fio):
        self.validate_fio(new_fio)
        self.__fio = new_fio


    @property
    def age(self):
        return self.__age


    @age.setter
    def age(self, new_age):
        self.validate_age(new_age)
        self.__age = new_age


    @property
    def phone(self):
        return self.__phone


    @phone.setter
    def phone(self, new_phone):
        self.validate_phone(new_phone)
        self.__phone = new_phone


    @property
    def passport(self):
        return self.__passport


    @passport.setter
    def passport(self, new_passport):
        self.validate_passport(new_passport)
        self.__passport = new_passport



    @property
    def pochta(self):
        return self.__pochta


    @pochta.setter
    def pochta(self, new_pochta):
        self.validate_pochta(new_pochta)
        self.__pochta = new_pochta


    @property
    def card(self):
        return self.__card


    @card.setter
    def card(self, new_card):
        self.validate_card(new_card)
        self.__card = new_card


savol=input("Yangi fuqaro ro'yhatga olasizmi Javob HA/YOQ").capitalize()
if savol=="Ha":
    ism=input("Fuqaro FIO sini kiriting")
    yosh=int(input("Fuqaro yoshinini kiriting"))
    tel=input("Fuqaro telefon nomerini kiriting + bilan ")
    seriya=input("Fuqaro Passport seriya va raqamlarini kiriting (masalan: AB5788443)")
    mail=input("Fuqaro email pochtasini  kiriting ")
    karta=input("Fuqaro plastik karta raqamini kiriting")
else:
    raise TypeError("Dastur bn to'liq tanishish uchun oldin 1 chi fuqaroni ro'yhatga oling")
    
    
A = Person(ism, yosh, tel, seriya,mail,karta)


print(f"Fuqaro FIO si {[A.fio]},\nYoshi {[A.age]},\nTelefon raqami {[A.phone]},\nPasport seriya va raqami {[A.passport]},\nFuqaro email manzili {[A.pochta]}, \nFuqaroning  Plastik karta raqamlari {[A.card]}")



b=input("Fuqaro malumotlariga o'zgartish kiritmoqchimichisiz javob HA/YOQ").capitalize()
if b=="Ha":
    c=input("Qaysi malumot turini o'zgartirmoqchisiz? FIO,YOSH,TELEFON,PASSPORT,MAIL,KARTA").capitalize()
    if c=="Fio":
        A.fio = input("Fuqaro FIO sini kiriting: ")
        print(f"Fuqaro FIO si {[A.fio]},\nYoshi {[A.age]},\nTelefon raqami {[A.phone]},\nPasport seriya va raqami {[A.passport]},\nFuqaro email manzili {[A.pochta]}, \nFuqaroning  Plastik karta raqamlari \n{[A.card]}")
        
    elif c=="Yosh":
        A.age = int(input("Fuqaro yoshini kiriting : "))        
        print(f"Fuqaro FIO si {[A.fio]},\nYoshi {[A.age]},\nTelefon raqami {[A.phone]},\nPasport seriya va raqami {[A.passport]},\nFuqaro email manzili {[A.pochta]}, \nFuqaroning  Plastik karta raqamlari \n{[A.card]}")
    elif c=="Telefon":
        A.phone = int(input("Fuqaro telefon nomerini kiriting: "))
        print(f"Fuqaro FIO si {[A.fio]},\nYoshi {[A.age]},\nTelefon raqami {[A.phone]},\nPasport seriya va raqami {[A.passport]},\nFuqaro email manzili {[A.pochta]},\n Fuqaroning  Plastik karta raqamlari \n{[A.card]}")
    elif c=="Passport":
        A.passport = input("Fuqaro passport seriyalarini kiriting: ")
        print(f"Fuqaro FIO si {[A.fio]},\nYoshi {[A.age]},\nTelefon raqami {[A.phone]},\nPasport seriya va raqami {[A.passport]},\nFuqaro email manzili {[A.pochta]}, \nFuqaroning  Plastik karta raqamlari \n{[A.card]}")
    elif c=="Mail":
        A.pochta = (input("Fuqaro email manzilini kiriting: "))
        print(f"Fuqaro FIO si {[A.fio]},\nYoshi {[A.age]},\nTelefon raqami {[A.phone]},\nPasport seriya va raqami {[A.passport]},\nFuqaro email manzili {[A.pochta]},\n Fuqaroning  Plastik karta raqamlari\n{[A.card]}")
    elif c=="Karta":
        A.card = (input("Yangi karta raqamini kiriting: "))
        print(f"Fuqaro FIO si {[A.fio]},\nYoshi {[A.age]},\nTelefon raqami {[A.phone]},\nPasport seriya va raqami {[A.passport]},\nFuqaro email manzili {[A.pochta]}, \nFuqaroning  Plastik karta raqamlari\n {[A.card]}")
                    
else:
    print(f"Fuqaro FIO si {[A.fio]},\nYoshi {[A.age]},\nTelefon raqami {[A.phone]},\nPasport seriya va raqami {[A.passport]},\nFuqaro email manzili {[A.pochta]},\n Fuqaroning  Plastik karta raqamlari \n{[A.card]}")
    print("Fuqaro malumotlariga o'zgartirish kiritilmadi")
        
                        

