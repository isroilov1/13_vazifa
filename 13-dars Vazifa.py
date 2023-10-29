# from abc import ABC, abstractmethod
# class Universitet(ABC):
#     @abstractmethod
#     def departments(self):
#         pass
#     @abstractmethod
#     def courses(self):
#         pass
#     @abstractmethod
#     def grades(self):
#         pass
#
# class Department(Universitet):
#     def departments(self):
#         print("Kafedrani ichida kafedralar!")
#     def courses(self):
#         print("Kafedrani ichida Kurslar")
#     def grades(self):
#         print("Kafedrani ichida Kurslar")
#
# class Professor(Universitet):
#     def departments(self):
#         print("Professorlarni ichida kafedralar!")
#     def courses(self):
#         print("Professorlarni ichida Kurslar")
#     def grades(self):
#         print("Professorlarni ichida Kurslar")
#
# class Student(Universitet):
#     def departments(self):
#         print("Student ichida kafedralar!")
#     def courses(self):
#         print("Student ichida Kurslar")
#     def grades(self):
#         print("Student ichida Kurslar")
#
# a = Department()
# a.grades()
# a.courses()
# b = Professor()
# b.grades()
# b.departments()
#
# c = Student()
# c.grades()
# c.courses()





# from abc import ABC, abstractmethod

# class Users(ABC):
#     def __init__(self, name, bank_kard, location):
#         self._name = name
#         self._bank_kard = bank_kard
#         self._location = location
#
#     @abstractmethod
#     def Product(self):
#         pass
#     @abstractmethod
#     def ShoppingCard(self):
#         pass
#     @abstractmethod
#     def Order(self):
#         pass
#
# class Sellers(Users):
#     def Product(self):
#         print("Kartoshka -3kg, olma -1kg, piyoz -2kg")
#     def ShoppingCard(self):
#         print("")
#     def
# class Customers(Users):
#     pass


# from abc import ABC, abstractmethod
#
# class Foydalanuvchi(ABC):
#     @abstractmethod
#     def royxatdan_otish(self):
#         pass
#
#     @abstractmethod
#     def kirish_qilish(self):
#         pass
#
# class Mahsulot:
#     def __init__(self, nomi, narxi):
#         self.nomi = nomi
#         self.narxi = narxi
#
# class Savat:
#     def __init__(self):
#         self.buyurtmalar = []
#
#     def buyurtma_qoshish(self, buyurtma):
#         self.buyurtmalar.append(buyurtma)
#         print(f"{buyurtma} - buyurtmalaringizga qo'shildi.")
#
#     def buyurtma_olish(self):
#         print(f"Buyurtmalaringiz ro'yxati: {self.buyurtmalar}")
#         return self.buyurtmalar
#
# class Buyurtma(ABC):
#     def __init__(self, pul=False):
#         self.pul = pul
#     @abstractmethod
#     def tolov_qilish(self):
#         pass
#
# class KartaBuyurtma(Buyurtma):
#     def __init__(self, mahsulot, karta_malumotlari, pul=False):
#         super().__init__(pul)
#         self.mahsulot = mahsulot
#         self._karta_malumotlari = karta_malumotlari
#
#     def tolov_qilish(self):
#         self.pul += True
#         print("Karta orqali to'lov amalga oshdi!")
#
#
#
# class NaqdBuyurtma(Buyurtma):
#     def __init__(self, mahsulot, pul):
#         super().__init__(pul)
#         self.mahsulot = mahsulot
#
#     def tolov_qilish(self):
#         if self.pul==False:
#             print(f"{self.mahsulot} uchun allaqachon naqt to'lov qilindi")
#         else:
#             print(f"{self.mahsulot} uchun to'lovni amalga oshirgansiz!")
#
# # Foydalanuvchi sinfiga oid boshqa foydalanuvchi sinflarini yaratish mumkin, masalan:
# class Xaridor(Foydalanuvchi):
#     def __init__(self, ismi, karta_raqami, manzili):
#         self._ismi = ismi
#         self._karta_raqami = karta_raqami
#         self._manzili = manzili
#     def royxatdan_otish(self):
#         print(f"Xaridor ro'yxatdan o'tdi!\nUning ismi {self._ismi}\nKarta raqami {self._karta_raqami}\nManzili {self._manzili}")
#
#     def kirish_qilish(self):
#         print("Hisobga muvaffaqqiyatli kirildi!")
#
# class Sotuvchi(Foydalanuvchi):
#     def royxatdan_otish(self):
#         print("Sotuvchi sifatida ro'yxatdan o'tdingiz!")
#
#     def kirish_qilish(self):
#         print("Tizimga muvaffaqqiyatli kirdingiz! Endi siz biz bilan hamkorlikda o'z ishingizni sotuvchi sifatida boshlashingiz mumkin!")
#
#
# a = KartaBuyurtma("olma", 1111, False)
# a.tolov_qilish()
# b = NaqdBuyurtma("Olma", False)
# b.tolov_qilish()






# from abc import ABC, abstractmethod
#
# class Aviakompaniya:
#     def __init__(self, nom):
#         self.nom = nom
#         self.parvozlar = []
#
#     def parvoz_qoshish(self, parvoz):
#         self.parvozlar.append(parvoz)
#
#     def parvozlarni_korish(self):
#         print(f"{self.nom} aviakompaniyasi quyidagi parvozlarni taklif qiladi:")
#         for parvoz in self.parvozlar:
#             print(parvoz)
#
# class Parvoz(ABC):
#     def __init__(self, nom, joylar_soni):
#         self.nom = nom
#         self.joylar_soni = joylar_soni
#         self.bronlar = []
#
#     def bron_qilish(self, yolovchi):
#         if len(self.bronlar) < self.joylar_soni:
#             self.bronlar.append(yolovchi)
#             print(f"{self.nom} parvoziga {yolovchi.ism} ismli yolovchini bron qildi.")
#         else:
#             print(f"{self.nom} parvozi to'ldi. Yana joylar mavjud emas.")
#
#     def bronlarni_korish(self):
#         print(f"{self.nom} parvozining bronlar ro'yxati:")
#         for yolovchi in self.bronlar:
#             print(yolovchi)
#
#     @abstractmethod
#     def orindiq_tanlash(self):
#         pass
#
# class Yolovchi:
#     def __init__(self, ism, pasport):
#         self.ism = ism
#         self.pasport = pasport
#
# class Bronlash:
#     def __init__(self):
#         self.aviakompaniyalar = []
#
#     def aviakompaniya_qoshish(self, aviakompaniya):
#         self.aviakompaniyalar.append(aviakompaniya)
#
#     def aviakompaniyalarni_korish(self):
#         print("Bronlash uchun mavjud aviakompaniyalar:")
#         for aviakompaniya in self.aviakompaniyalar:
#             print(aviakompaniya.nom)
#
# # Tartiblar bo'yicha Polimorfizm
# class Tartib1Parvoz(Parvoz):
#     def orindiq_tanlash(self):
#         print(f"{self.nom} parvozi uchun tartib 1 bilan orindiqlar tanlanadi.")
#
# class Tartib2Parvoz(Parvoz):
#     def orindiq_tanlash(self):
#         print(f"{self.nom} parvozi uchun tartib 2 bilan orindiqlar tanlanadi.")
#
#
# # Bronlash tizimini test qilish
# bronlash = Bronlash()
#
# # Aviakompaniyalar yaratish
# uzairways = Aviakompaniya("UzAirways")
# airbaltic = Aviakompaniya("AirBaltic")
#
# # Aviakompaniyalarni bronlash tizimiga qoshish
# bronlash.aviakompaniya_qoshish(uzairways)
# bronlash.aviakompaniya_qoshish(airbaltic)
#
# # Parvozlarni yaratish
# parvoz1 = Tartib1Parvoz("Toshkent - Moskva", 200)
# parvoz2 = Tartib2Parvoz("Riga - Toshkent", 150)
#
# # Parvozlarni aviakompaniyalarga qoshish
# uzairways.parvoz_qoshish(parvoz1)
# airbaltic.parvoz_qoshish(parvoz2)
#
# # Yolovchilar yaratish
# yolovchi1 = Yolovchi("Qunduzbobo", "AB123456")
# yolovchi2 = Yolovchi("Qodirali", "CD789012")
#
# # Parvozlarga yolovchilarni bron qilish
# parvoz1.bron_qilish(yolovchi1)
# parvoz1.bron_qilish(yolovchi2)
#
# # Parvozlar va bronlar ro'yxatini korish
# uzairways.parvozlarni_korish()
# parvoz1.bronlarni_korish()
# parvoz2.bronlarni_korish()
#
# # Polimorfizmni test qilish
# parvoz1.orindiq_tanlash()
# parvoz2.orindiq_tanlash()







from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.inventory = []

    def take_item(self, item):
        self.inventory.append(item)
        print(f"{self.name} {item}ni inventariga oladi.")

    def use_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            print(f"{self.name} {item}ni ishlatadi.")
        else:
            print(f"{self.name}ning inventarida {item} mavjud emas.")

    @abstractmethod
    def harakatlar(self):
        pass

class PlayerCharacter(Character):
    def __init__(self, name, health):
        super().__init__(name, health)

    def harakatlar(self):
        print(f"{self.name} o'yinchisi xatti-harakatlarni bajaydi.")

    def interact(self, character):
        print(f"{self.name} {character.name} bilan o'zaro ta'sirga kiradi.")

class NonPlayerCharacter(Character):
    def __init__(self, name, health):
        super().__init__(name, health)

    def harakatlar(self):
        print(f"{self.name} boti o'z xatti-harakatlarini bajaydi.")

# O'yinda qo'llaniladigan boshqa sinflar
class Quest:
    def __init__(self, name):
        self.name = name

    def start(self):
        print(f"{self.name} kvesti boshlandi.")

    def complete(self):
        print(f"{self.name} kvesti yakunlandi.")

class Item:
    def __init__(self, name):
        self.name = name

player = PlayerCharacter("John", 100)
npc = NonPlayerCharacter("NPC", 100)

item1 = Item("Sword")
item2 = Item("Health Potion")

player.take_item(item1)
player.take_item(item2)

player.use_item(item1)
player.use_item(item2)
player.use_item(item2)

player.harakatlar()
npc.harakatlar()

player.interact(npc)
npc.harakatlar()

quest = Quest("Save the Princess")
quest.start()
quest.complete()