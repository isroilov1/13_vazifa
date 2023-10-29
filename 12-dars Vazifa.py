# class Shape:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
# class Circle(Shape):
#     def __init__(self, r, pi=3.14):
#         self.r = r
#         self.pi = pi
#     def area(self):
#         print("Doira yuzi:", self.pi*(self.r**2))
#     def per(self):
#         print("Aylana uzunligi: l =", 2*self.pi*self.r)
#
# class Rectangle(Shape):
#     def __init__(self, a, b):
#         super().__init__(a, b)
#     def area(self):
#         print("To'rtburchak yuzi:", self.a*self.b)
#     def per(self):
#         print("To'rtburchak perimetri:", (self.a+self.b)*2)
#
# class Triangle(Shape):
#     def __init__(self, a, b, ha, c):
#         self.ha = ha
#         self.c = c
#         super().__init__(a, b)
#     def area(self):
#         print("Uchburchak yuzi:", (self.ha*self.a)/2)
#     def per(self):
#         print("Uchburchak perimetri:", self.a+self.b+self.c)
#
# # shakl = Shape(6, 7)
# cir = Circle(6)
# cir.area()
# cir.per()
# tri = Triangle(6, 4, ha=4, c=5)
# tri.area()
# tri.per()
# rec = Rectangle(6, 7)
# rec.area()
# rec.per()





# class Accaunt:
#     def __init__(self):
#         pass
#
# class SavingsAccaunt(Accaunt):
#     def _interest(self):
#         print("Foiz stavkasi")
#     def _deposits(self):
#         print("Depozitlar")
#     def _withdrawals(self):
#         print("Yechib olish")
#
# class ChekingsAccaunt(Accaunt):
#     def _interest(self):
#         print("Foiz stavkasini tekshirish")
#     def _deposits(self):
#         print("Depozitlarlarni tekshirish")
#     def _withdrawals(self):
#         print("Yechib olishlarni tekshirish")
#
# a = SavingsAccaunt()
# a.interest()              # encapsulation qilingani uchun xatolik beryapti
# a.deposits()
# a.withdrawals()
# b = ChekingsAccaunt()
# b.interest()
# b.deposits()
# b.withdrawals()






# class Employee:
#     def __init__(self, oylik, samaradorligi):
#         self.oylik = oylik
#         self.samaradorligi = samaradorligi
#
#     def mukofot(self):
#         a = self.oylik + self.samaradorligi
#         return a
#
# class Manager(Employee):
#     def __init__(self, oylik, samaradorligi):
#         super().__init__(oylik, samaradorligi)
#         print("Menejer mukofoti:", self.mukofot())
#
# class Engineer(Employee):
#     def __init__(self, oylik, samaradorligi):
#         super().__init__(oylik, samaradorligi)
#         print("Muhandis mukofoti:", self.mukofot())
#
# class Salesperson(Employee):
#     def __init__(self, oylik, samaradorligi):
#         super().__init__(oylik, samaradorligi)
#         print("Sotuvchi mukofoti:", self.mukofot())
#
# a = Manager(510, 190)
# a.mukofot()
# b = Engineer(420, 220)
# b.mukofot()
# c = Salesperson(200, 100)
# c.mukofot()










# class LibraryItem:
#     def __init__(self, title, author):
#         self._title = title
#         self._author = author
# class Book(LibraryItem):
#     def __init__(self, title, author, ISBN):
#         super().init(title, author)
#         self._ISBN = ISBN
#
#     def display(self):
#         info = f"Title: {self._title}\nAuthor: {self._author}\nISBN: {self._ISBN}"
#         return info
#
# class DVD(LibraryItem):
#     def __init__(self, title, author, director):
#         super().init(title, author)
#         self._director = director
#
#     def display(self):
#         info = f"Title: {self._title}\nAuthor: {self._author}\nDirector: {self._director}"
#         return info
#
#
# a = LibraryItem("The Lord of the Rings: The Fellowship of the Ring", "J.R.R. Tolkien")
# b = Book("The Lord of the Rings: The Fellowship of the Ring", "J.R.R. Tolkien", "0-395-19383-8", )
# c = DVD("The Lord of the Rings: The Fellowship of the Ring", "J.R.R. Tolkien", "Fantacy")
# b.display()
# c.display()
# "The Shawshank Redemption", "Frank Darabont", 142








# class Animal:
#     def __init__(self, sound, movement):
#         self._sound = sound
#         self._movement = movement
#
# class Mammmal(Animal):
#     def __init__(self, sound, movement):
#         super().__init__(sound, movement)
# class Bird(Animal):
#     def __init__(self, sound, movement):
#         super().__init__(sound, movement)
# class Fish(Animal):
#     def __init__(self, sound, movement):
#         super().__init__(sound, movement)
#
#
# c1 = Mammmal("Ma Ma Ma Mammal", "tor oyoqlab")
# c1.sound()





# class Vehicle:
#     def __init__(self, speed):
#         self.speed = speed
# class Car(Vehicle):
#     def __init__(self, speed):
#         super().__init__(speed)
# class Bicycle(Vehicle):
#     def __init__(self, speed):
#         super().__init__(speed)
# class Truck(Vehicle):
#     def __init__(self, speed):
#         super().__init__(speed)
# car1 = Car(220)
# print(car1.speed)
# car2 = Bicycle(30)
# print(car2.speed)
# car3 = Truck(80)
# print(car3.speed)






class ShoppingCart:                    # chala
    def __init__(self, olma, anor, behi, fonar, telefon, oq_qora_kitobi, insoniylik, otkan_kunlar, kartoshka):
        self.kartoshka = kartoshka
        self.otkan_kunlar = otkan_kunlar
        self.insoniylik = insoniylik
        self.oq_qora_kitobi = oq_qora_kitobi
        self.telefon = telefon
        self.fonar = fonar
        self.behi = behi
        self.anor = anor
        self.olma = olma
class Product(ShoppingCart):
    def __init__(self):
        super().__init__(self, olma, anor, behi, kartoshka)
        a = self.olma+self.anor+self.behi+self.kartoshka
        return a

class BookProduct(ShoppingCart):
    def __init__(self):
        super().__init__(oq_qora_kitobi, insoniylik, otkan_kunlar)
        a = self.oq_qora_kitobi+self.insoniylik+self.otkan_kunlar
        print(a)

class ElectronicProduct(ShoppingCart):
    def __init__(self):
        super().__init__(fonar, telefon)
        a = self.fonar+self.telefon

a = ShoppingCart(12000, 5000, 7000, 20000, 1500000, 30000, 45000, 100000, 4000)
b = Product()
print(b)