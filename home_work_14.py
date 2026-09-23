# #1
# def add_student():
#     name = input("შეიყვანეთ სტუდენტის სახელი: ")
#
#     scores = []
#
#     for i in range(3):
#         score = float(input(f"შეიყვანეთ {i + 1}-ლი ქულა: "))
#         scores.append(score)
#
#     with open("students.txt", "a") as file:
#         file.write(f"{name},{scores[0]},{scores[1]},{scores[2]}\n")
#
#     print("სტუდენტი წარმატებით დაემატა!")
#
#
# def show_students():
#     try:
#         with open("students.txt", "r") as file:
#             students = file.readlines()
#
#             if not students:
#                 print("სტუდენტები არ მოიძებნა.")
#                 return
#
#             print("\n--- სტუდენტების სია ---")
#
#             for line in students:
#                 data = line.strip().split(",")
#
#                 name = data[0]
#
#                 scores = [
#                     float(data[1]),
#                     float(data[2]),
#                     float(data[3])
#                 ]
#
#                 print(f"სახელი: {name}")
#                 print(f"ქულები: {scores}")
#                 print(f"საშუალო: {calculate_average(scores):.2f}")
#                 print("--------------------")
#
#     except FileNotFoundError:
#         print("students.txt ფაილი არ არსებობს.")
#
#
# def calculate_average(scores):
#     total = 0
#
#     for score in scores:
#         total += score
#
#     return total / len(scores)
#
#
# def find_best_student():
#     try:
#         with open("students.txt", "r") as file:
#             students = file.readlines()
#
#             if not students:
#                 print("სტუდენტები არ მოიძებნა.")
#                 return
#
#             best_student = ""
#             best_average = 0
#
#             for line in students:
#                 data = line.strip().split(",")
#
#                 name = data[0]
#
#                 scores = [
#                     float(data[1]),
#                     float(data[2]),
#                     float(data[3])
#                 ]
#
#                 average = calculate_average(scores)
#
#                 if average > best_average:
#                     best_average = average
#                     best_student = name
#
#             print("\n--- საუკეთესო სტუდენტი ---")
#             print(f"სტუდენტი: {best_student}")
#             print(f"საშუალო ქულა: {best_average:.2f}")
#
#     except FileNotFoundError:
#         print("students.txt ფაილი არ არსებობს.")
#
#
# menu = {
#     1: "სტუდენტის დამატება",
#     2: "სტუდენტების ჩვენება",
#     3: "საუკეთესო სტუდენტის პოვნა",
#     4: "გასვლა"
# }
#
#
# while True:
#     print("\n===== სტუდენტების სისტემა =====")
#
#     for number, option in menu.items():
#         print(f"{number}. {option}")
#
#     try:
#         choice = int(input("აირჩიეთ მოქმედება: "))
#
#         if choice == 1:
#             add_student()
#
#         elif choice == 2:
#             show_students()
#
#         elif choice == 3:
#             find_best_student()
#
#         elif choice == 4:
#             print("პროგრამა დასრულდა.")
#             break
#
#         else:
#             print("არასწორი არჩევანია.")
#
#     except ValueError:
#         print("გთხოვთ, შეიყვანოთ რიცხვი.")



# #2
# def load_products():
#     products = {}
#
#     try:
#         with open("products.csv", "r") as file:
#             for line in file:
#                 data = line.strip().split(",")
#
#                 if len(data) == 2:
#                     name = data[0]
#                     price = float(data[1])
#
#                     products[name] = price
#
#     except FileNotFoundError:
#         print("products.csv ფაილი არ არსებობს.")
#
#     return products
#
#
# def add_product():
#     name = input("შეიყვანეთ პროდუქტის სახელი: ").strip()
#
#     try:
#         price = float(input("შეიყვანეთ პროდუქტის ფასი: "))
#
#         with open("products.csv", "a") as file:
#             file.write(f"{name},{price}\n")
#
#         print("პროდუქტი წარმატებით დაემატა!")
#
#     except ValueError:
#         print("ფასი უნდა იყოს რიცხვი.")
#
#
# def show_products():
#     products = load_products()
#
#     if not products:
#         print("პროდუქტები არ მოიძებნა.")
#         return
#
#     print("\n===== პროდუქტების სია =====")
#
#     for name, price in products.items():
#         print(f"პროდუქტი: {name} | ფასი: {price} ლარი")
#
#
# def search_product():
#     products = load_products()
#
#     search = input("შეიყვანეთ საძებნი პროდუქტი: ").strip().lower()
#
#     found = False
#
#     for name, price in products.items():
#         if search in name.lower():
#             print(f"ნაპოვნია: {name} - {price} ლარი")
#             found = True
#
#     if not found:
#         print("ასეთი პროდუქტი ვერ მოიძებნა.")
#
#
# def buy_product():
#     products = load_products()
#
#     name = input("შეიყვანეთ პროდუქტის სახელი: ").strip()
#
#     found_product = None
#
#     for product_name in products:
#         if product_name.lower() == name.lower():
#             found_product = product_name
#             break
#
#     if found_product is None:
#         print("ასეთი პროდუქტი ვერ მოიძებნა.")
#         return
#
#     print(f"თქვენ იყიდეთ: {found_product}")
#     print(f"ფასი: {products[found_product]} ლარი")
#
#
# def calculate_total():
#     products = load_products()
#
#     if not products:
#         print("პროდუქტები არ არის.")
#         return
#
#     total = 0
#
#     for price in products.values():
#         total += price
#
#     print(f"ყველა პროდუქტის ჯამური ღირებულება: {total} ლარი")
#
#
# menu = {
#     1: "პროდუქტის დამატება",
#     2: "პროდუქტების ჩვენება",
#     3: "პროდუქტის ძებნა",
#     4: "პროდუქტის ყიდვა",
#     5: "ჯამური ღირებულების გამოთვლა",
#     6: "გასვლა"
# }
#
#
# while True:
#     print("\n===== პროდუქტის სისტემა =====")
#
#     for number, option in menu.items():
#         print(f"{number}. {option}")
#
#     try:
#         choice = int(input("აირჩიეთ მოქმედება: "))
#
#         if choice == 1:
#             add_product()
#
#         elif choice == 2:
#             show_products()
#
#         elif choice == 3:
#             search_product()
#
#         elif choice == 4:
#             buy_product()
#
#         elif choice == 5:
#             calculate_total()
#
#         elif choice == 6:
#             print("პროგრამა დასრულდა.")
#             break
#
#         else:
#             print("არასწორი არჩევანია.")
#
#     except ValueError:
#         print("გთხოვთ, შეიყვანოთ რიცხვი.")