# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.__balance = balance
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.balance = self.balance + amount
#             print("თანხა წარმატებით დაემატა.")
#         else:
#             print("თანხა უნდა იყოს დადებითი.")
#
#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance = self.balance - amount
#             print("თანხა წარმატებით გაიტანეთ.")
#         else:
#             print("არასაკმარისი ბალანსი.")
#
#     @property
#     def balance(self):
#         return self.__balance
#
#     @balance.setter
#     def balance(self, value):
#         if value >= 0:
#             self.__balance = value
#         else:
#             print("ბალანსი უარყოფითი ვერ იქნება.")
#
#     def __str__(self):
#         return f"მფლობელი: {self.owner} | ბალანსი: {self.balance} GEL"
#
#
# # გამოყენება
# account = BankAccount("Nika", 1000)
#
# print(account)
#
# account.deposit(500)
#
# print("მიმდინარე ბალანსი:", account.balance)
#
# account.withdraw(200)
#
# print("მიმდინარე ბალანსი:", account.balance)




# 2
# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def speak(self):
#         print("ცხოველი ხმას გამოსცემს.")
#
#
# class Dog(Animal):
#     def speak(self):
#         print("Woof!")
#
#
# class Cat(Animal):
#     def speak(self):
#         print("Meow!")
#
#
# class Cow(Animal):
#     def speak(self):
#         print("Moo!")
#
#
# animals = [
#     Dog("Rex", 3),
#     Cat("Mimi", 2),
#     Cow("Bessie", 5)
# ]
#
#
# for animal in animals:
#     print(f"{animal.name}, ასაკი: {animal.age}")
#     animal.speak()
#
#
# def make_sound(animal):
#     animal.speak()
#
#
# print("\n--- make_sound ფუნქცია ---")
#
# make_sound(Dog("Buddy", 4))
# make_sound(Cat("Kitty", 2))
# make_sound(Cow("Daisy", 6))






# 3
# class User:
#     def __init__(self, username, email):
#         self.username = username
#         self.email = email
#
#     def login(self):
#         print(f"{self.username} წარმატებით შევიდა სისტემაში.")
#
#
# class Admin(User):
#     def delete_user(self):
#         print("მომხმარებელი წაიშალა.")
#
#
# class Logger:
#     def log(self):
#         print("მოქმედება ჩაიწერა ლოგში.")
#
#
# class SuperAdmin(Admin, Logger):
#     pass
# 
#
# # SuperAdmin-ის ობიექტის შექმნა
# admin = SuperAdmin("Nika", "nika@gmail.com")
#
#
# # login() მოდის User-იდან
# admin.login()
#
# # delete_user() მოდის Admin-იდან
# admin.delete_user()
#
# # log() მოდის Logger-იდან
# admin.log()
#
#
# # MRO
# print("\n--- MRO ---")
# print(SuperAdmin.mro())