# import random


# #1
# nums = []
# for i in range(10):
#     nums.append(random.randint(1,10))
#
# sorted_nums = sorted(nums)
# print(f"ყველაზე დიდი რიცხვი - {sorted_nums[0]}")
# print(f"ყველაზე დაბალი რიცხვი - {sorted_nums[-1]}")

# # 2.
# nums = []
# for i in range(10):
#     nums.append(random.randint(1,10))
#
# print(f"სია - {nums}")
#
# reversed_nums = list(reversed(nums))
# print(f"შეტრიალებულის სია - {reversed_nums}")
#
# reversed_nums1 = nums[::-1]
# print(f"შეტრიალებულის სია - {reversed_nums1}")

# 3.

# students = []
#
# while True:
#     print("""
# 1 სტუდენტის დამატება (ასაკიც და ქულები)
#
# 2 სტუდენტის წაშლა
#
# 3 სტუდენტის ძებნა ( აჩვენე ასაკი და ქუელბი და საშვალო ქულა)
#
# 4 ყველა სტუდენტის ნახვა
#
# 5 საშუალო ქულის გამოთვლა
#
# 6 საუკეთესო სტუდენტის პოვნა ( აჩვენე ასაკი და ქულაც)
#
# 7 ყველაზე დაბალი ქულის პოვნა ( აჩვენე ასაკი და ქულაც)
#
# 8 გასვლა
#     """)
#     num = input("შეიყვანეთ რიცხვი: ")
#
#     if num == "1":
#         name = input("შეიყვანეთ სახელი: ").strip().capitalize()
#         age = int(input("შეიყვანეთ ასაკი: "))
#         scores = []
#         for i in range(3):
#             score = float(input(f"შეიყვანეთ {i+1} საგნის ქულა: "))
#             if score < 0 or score > 100:
#                 print("არასწორი ქულა, შეიყვანეთ თავიდან")
#                 score = float(input(f"შეიყვანეთ {i + 1} საგნის ქულა: "))
#             scores.append(score)
#         students.append([name, age, scores])
#         print("სტუდენტი წარმატებით დაემატა!")
#
#     if num == "2":
#         name = input("შეიყვანეთ სახელი: ").strip().capitalize()
#         found = False
#         for student in students:
#             if student[0] == name:
#                 students.remove(student)
#                 found = True
#                 break
#         if not found:
#             print("ასეთი სტუდენტი ვერ მოიძებნა")
#
#     if num == "3":
#         name = input("შეიყვანეთ სახელი: ").strip().capitalize()
#         found = False
#         for student in students:
#             if student[0] == name:
#                 print(f"ასაკი - {student[1]}, ქულები - {student[2]}, საშუალო ქულა - {sum(student[2]) / 3}")
#                 found = True
#                 break
#         if not found:
#             print("ასეთი სტუდენტი ვერ მოიძებნა")
#
#     if num == "4":
#         print("ყველა სტუდენტი:")
#         for student in students:
#             print(student)
#
#     if num == "5":
#         name = input("შეიყვანეთ სტუდენტის სახელი: ").strip().capitalize()
#         found = False
#         for student in students:
#             if student[0] == name:
#                 avg_score = sum(student[2]) / 3
#                 print(f"{name}-ს საშუალო ქულა - {avg_score}")
#                 found = True
#                 break
#         if not found:
#             print("ასეთი სტუდენტი ვერ მოიძებნა")
#
#     if num == "6":
#         if not students:
#             print("სტუდენტები არ არის")
#         else:
#             avg_scores = []
#             for student in students:
#                 avg_score = [sum(student[2]) / 3, student[1], student[0]]
#                 avg_scores.append(avg_score)
#             max_score = 0
#             max_age = 0
#             max_name = ""
#             for score in avg_scores:
#                 if score[0] > max_score:
#                     max_score = score[0]
#                     max_age = score[1]
#                     max_name = score[2]
#             print(f"ყველაზე მაღალქულიანი სტუდენტი - {max_name}, ასაკი - {max_age}, ქულა - {max_score}")
#
#     if num == "7":
#         if not students:
#             print("სტუდენტები არ არის")
#         else:
#             avg_scores = []
#             for student in students:
#                 avg_score = [sum(student[2]) / 3, student[1], student[0]]
#                 avg_scores.append(avg_score)
#             min_score = 100
#             min_age = 0
#             min_name = ""
#             for score in avg_scores:
#                 if score[0] < min_score:
#                     min_score = score[0]
#                     min_age = score[1]
#                     min_name = score[2]
#             print(f"ყველაზე დაბალქულიანი სტუდენტი - {min_name}, ასაკი - {min_age}, ქულა - {min_score}")
#
#     if num == "8":
#         break



