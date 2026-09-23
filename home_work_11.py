# # 1.
#
# txt = input("შეიყვანეთ ტექსტი: ").strip()
#
# def count_letters(txt):
#     words = txt.split()
#     count = 0
#     for word in words:
#         count += len(word)
#     return count
#
# def count_words(txt):
#     words = txt.split()
#     count = 0
#     for word in words:
#         count += 1
#     return count
#
# def count_digits(txt):
#     words = txt.split()
#     count = 0
#     for word in words:
#         if word.isdigit():
#             count += 1
#     return count
#
# def count_specials(txt):
#     words = txt.split()
#     count = 0
#     for word in words:
#         if not word.isdigit() and not word.isalpha():
#             count += 1
#     return count
#
# def count_vowels(txt):
#     words = txt.split()
#     count = 0
#     vowels = ['a', 'e', 'i', 'o', 'ა', 'ე', 'ი', 'ო', 'უ']
#     for word in words:
#         for letter in word:
#             if letter in vowels:
#                 count += 1
#     return count








# 2.


# students = []
#
# def add_student():
#     name = input("შეიყვანეთ სტუდენტის სახელი: ").strip().capitalize()
#     grades = []
#     for i in range (1, 4):
#         num = int(input(f"შეიყვანეთ რიგით {i} საგნის ქულა: "))
#         while num > 100 or num < 0:
#             print("შეიყვანეთ რიცხვი 0-იდან 100-მდე")
#             num = int(input(f"შეიყვანეთ რიგით {i} საგნის ქულა: "))
#         grades.append(num)
#     student = {"name": name, "grades": grades}
#     students.append(student)
#     print("სტუდენტი წარმატებით დაემატა!")
#
# def show_students():
#     for student in students:
#         print(student)
#
# def calculate_average(students):
#     name = input("შეიყვანეთ სტუდენტის სახელი: ").strip().capitalize()
#     for student in students:
#         if student["name"] == name:
#             print(f"{name}-ის საშუალო ქულა: {round(sum(student['grades'])/3, 2)}")
#
# def best_student(students):
#     grades = []
#     for student in students:
#         grades.append(round(sum(student["grades"])/3, 2))
#     max_grade = max(grades)
#
#     print(f"საუკეთესო სტუდენტი - {students[grades.index(max_grade)]['name']}, საშუალო ქულა - {max_grade}")








# 3.


# 
# students = []
#
#
# def show_menu():
#     print("""
# ==========================
# 1. სტუდენტის დამატება
# 2. სტუდენტის წაშლა
# 3. სტუდენტის ძებნა
# 4. ყველა სტუდენტის ნახვა
# 5. საშუალო ქულის გამოთვლა
# 6. საუკეთესო სტუდენტის ნახვა
# 7. გასვლა
# ==========================
# """)
#
#
# def add_student():
#     name = input("შეიყვანეთ სახელი: ").strip().capitalize()
#     age = int(input("შეიყვანეთ ასაკი: "))
#     faculty = input("შეიყვანეთ ფაკულტეტი: ").strip().capitalize()
#     grades = []
#     for i in range (1, 4):
#         num = int(input(f"შეიყვანეთ რიგით {i} საგნის ქულა: "))
#         while num > 100 or num < 0:
#             print("შეიყვანეთ რიცხვი 0-იდან 100-მდე!")
#             num = int(input(f"შეიყვანეთ რიგით {i} საგნის ქულა: "))
#         grades.append(num)
#
#     student = {"name":name, "age":age, "faculty":faculty, "grades":grades}
#     students.append(student)
#
#     print("სტუდენტი წარმატებით დაემატა!")
#
#
# def delete_student():
#     name = input("შეიყვანეთ სტუდენტის სახელი: ").strip().capitalize()
#     for student in students:
#         if student["name"] == name:
#             students.remove(student)
#             print("სტუდენტის მონაცემები წაიშალა")
#         else:
#             print("ასეთი სტუდნეტი ვერ მოიძებნა")
#
#
# def search_student():
#     name = input("შეიყვანეთ სტუდენტის სახელი: ").strip().capitalize()
#     for student in students:
#         if student["name"] == name:
#             print(student)
#         else:
#             print("ასეთი სტიდენტი ვერ მოიძებნა")
#
# def show_students():
#     for student in students:
#         print(student)
#
# def calculate_average():
#     name = input("შეიყვანეთ სტუდენტის სახელი: ").strip().capitalize()
#     for student in students:
#         if student["name"] == name:
#             print(f"{name}-ის საშუალო ქულა: {round(sum(student['grades'])/3, 2)}")
#
#
# def best_student():
#     grades = []
#     for student in students:
#         grades.append(round(sum(student["grades"])/3, 2))
#     max_grade = max(grades)
#
#     print(f"საუკეთესო სტუდენტი - {students[grades.index(max_grade)]['name']}, საშუალო ქულა - {max_grade}")
#
#
# def exit_program():
#     pass
#
# while True:
#     show_menu()
#
#     choice = input("აირჩიეთ მოქმედება: ")
#
#     if choice == "1":
#         add_student()
#
#     elif choice == "2":
#         delete_student()
#
#     elif choice == "3":
#         search_student()
#
#     elif choice == "4":
#         show_students()
#
#     elif choice == "5":
#         calculate_average()
#
#     elif choice == "6":
#         best_student()
#
#     elif choice == "7":
#         exit_program()
#         break
#
#     else:
#         print("არასწორი არჩევანია!")