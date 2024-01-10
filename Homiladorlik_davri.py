from datetime import datetime,timedelta

import pytz 

def yashagan_umr(yil,oy,kun):
    #  bu funksiya hozirgi kungacha nechchi kun yashaganini aniqlaydi 
    
    today = datetime.datetime.today()
    date_of_birth=datetime.datetime(yil,oy,kun)
    natija=today-date_of_birth
    print(f"Siz tugilganizdan beri shuncha kun yashadingiz {natija}")
# yashagan_umr(1998,5,22)

def tugilgan_kun_nomi(yil,oy,kun):

    # bu funksiya tugilgan yil oy kunini kiritib  haftaning qaysi kunida tugilganligini aniqlaydi
    sanoq = datetime.datetime(yil,oy,kun)

    haftaning_kuni = sanoq.weekday()

    haftaning_nomlari = ["Yakshanba", "Dushanba", "Seshanba", "Chorshanba", "Payshanba", "Juma", "Shanba"]

    print(f"Sizning tugilgan kuningiz {sanoq.year}-{sanoq.month}-{sanoq.day} haftaning {haftaning_nomlari[haftaning_kuni]} kuni")

# tugilgan_kun_nomi(1999,3,16)
def mintaqaviy_vaqt():
    # bu funksiya orqali Mintaqa va shaxarni kiritib osha shaxar Mintaqaviy vaqtini bilib oling
    a=input('Mintaqani kiriting Masalan=Asia,Europe,America').capitalize()
    b=input("Kiritilgan mintaqa ichidagi Shaxarni kiriting Masalan=Tokyo,Dubay, ").capitalize()
    
    dt_now = datetime.datetime.now(tz=pytz.UTC)

    dt_utc = dt_now.astimezone(pytz.timezone(f"{a}/{b}"))
    print(f"{b} bo'yicha mintaqaviy vaqt {dt_utc}")
    
    print(dt_utc.strftime('Kun %d Oy %B Yil %Y Hafta kuni %A Soat %H Daqaiqa %M Sekund %S '))
# mintaqaviy_vaqt()

def homiladorlik_davri(homila_kuni):
    # Bu funksiya yordami homilador ayolni qachon farzandli bolishi taxminiy hisoblab beradi 
    # ustoz kulmen miyyaga shu keb qoldida:-D
    # # homiladorlik bo'lgan sanani foydalanuvchidan qabul qilamiz
    yil= datetime.strptime(homila_kuni, '%Y-%m-%d')
    # qabul qilingan sanaga 266 kun yani 9 oy qoshamiz
    yil+=timedelta(days=266)
    # haftaning kunlarini olvolamiz
    haftaning_kuni = yil.weekday()
    # oylarni index boyicha nomlab olamiz
    oy_nomi=['Yanvar','Fevral', 'Mart','Aprel', 'May', 'Iyun', 'Iyul', 'Avgust', 'Sentyabr', 'Oktyabr','Noyabr', 'Dekabr']
    # hafta kunlarini  weekday indexsi bo'yicha nomlaymiz
    haftakuni = ["Yakshanba", "Dushanba", "Seshanba", "Chorshanba", "Payshanba", "Juma", "Shanba"]
    # Natijani foydalanuvchiga taqdim etamiz
    print("Siz taxminan shu sanalarda farzand dunyoga keltirasiz")
    print(f"{yil.day}-{oy_nomi[yil.month-1]}{yil.year}-Yil {haftakuni[haftaning_kuni]} Kuni") 
# homiladorlik_davri(input("Homiladorlik sanasini kiriting"))

#  Ustoz 3 tadan deyilgandi idea kelmadi boshqa


