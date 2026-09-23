from functools import reduce
import random


#1
# accounts = [
#     {"name": "Nika", "balance": 1500},
#     {"name": "Ana", "balance": 3000}
# ]
#
# def find_account(name):
#     for acc in accounts:
#         if acc["name"] == name:
#             return acc
#     raise ValueError("ანგარიში ვერ მოიძებნა!")
#
# def deposit(name, amount):
#     try:
#         acc = find_account(name)
#         if not isinstance(amount, (int, float)):
#             raise TypeError("თანხა უნდა იყოს რიცხვი")
#         acc["balance"] += amount
#     except (ValueError, TypeError) as e:
#         print("error:", e)
#     else:
#         print(f"დეპოზიტი წარმატებით შესრულდა! ახალი ბალანსი: {acc['balance']}")
#     finally:
#         print("ტრანზაქცია დასრულდა.")
#
# def withdraw(name, amount):
#     try:
#         acc = find_account(name)
#         if not isinstance(amount, (int, float)):
#             raise TypeError("თანხა უნდა იყოს რიცხვი")
#         if acc["balance"] < amount:
#             raise ValueError("ბალანსი არასაკმარისია!")
#         acc["balance"] -= amount
#     except (ValueError, TypeError) as e:
#         print("error:", e)
#     else:
#         print(f"გატანა წარმატებით შესრულდა! ახალი ბალანსი: {acc['balance']}")
#     finally:
#         print("ტრანზაქცია დასრულდა.")
#
# def show_balance(name):
#     try:
#         acc = find_account(name)
#         print(f"{acc['name']}-ის ბალანსი: {acc['balance']}")
#     except ValueError as e:
#         print("error:", e)


#2

# numbers = [1,2,3,4,5,6,7,8,9,10]
#
# evens = list(filter(lambda x: x % 2 == 0, numbers))
# print("ლუწები:", evens)
#
# multiplied = list(map(lambda x: x * 3, evens))
# print("გამრავლებული:", multiplied)
#
# total = reduce(lambda a,b: a+b, multiplied)
# print("საბოლოო ჯამი:", total)


#3

# questions = [
#     {"question": "რა არის Python?", "answer": "პროგრამირების ენა"},
#     {"question": "2 + 2?", "answer": "4"},
#     {"question": "რა არის საფრანგეთის დედაქალაქი?", "answer": "პარიზი"},
#     {"question": "5 * 5?", "answer": "25"},
# ]
#
# def show_question(q, num):
#     print(f"\nკითხვა {num}:")
#     print(q["question"])
#
# def check_answer(q, user_answer):
#     try:
#         if not isinstance(user_answer, str):
#             raise TypeError("პასუხი უნდა იყოს ტექსტი!")
#         return q["answer"].lower() == user_answer.lower()
#     except Exception as e:
#         print("შეცდომა:", e)
#         return False
#
# def calculate_score(results):
#     return sum(results)
#
# def show_result(score, total):
#     percent = (score / total) * 100
#     print("\n========================")
#     print(f"ქულა: {score} / {total}")
#     print(f"შედეგი: {percent:.0f}%")
#     print("========================")
#
# def start_quiz(*args, **kwargs):
#     random.shuffle(questions)
#     results = []
#     for i, q in enumerate(questions, start=1):
#         show_question(q, i)
#         try:
#             ans = input("თქვენი პასუხი: ")
#         except Exception:
#             ans = ""
#         if check_answer(q, ans):
#             print("სწორია!")
#             results.append(1)
#         else:
#             print("არასწორია!")
#             results.append(0)
#     score = calculate_score(results)
#     show_result(score, len(questions))


##start_quiz()






