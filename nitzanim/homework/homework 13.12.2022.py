# ex-1:
# for number in range(0, 101):
#     if number > 1:
#         for rishoni in range(2, number):
#             if number % rishoni == 0:
#                 break
#         else:
#             print(number)


# ex-3:
# sum_length = 0
# for long in range(44):
#     name = str(input("enter the name of the road: "))
#     length = int(input("enter the length of the road: "))
#     if length > 15:
#         print(name, length)
#     sum_length += length
# print("the length of the whole road is: ",sum_length)

# Challenge:

# ex-1:
# start1 = 0
# start2 = 1
# fibonacci: int = 0
# number = int(input("enter a number: "))
# if number == 1:
#     print(start1)
# elif number == 2:
#     print(start2)
# else:
#     for fibo in range(2, number):
#         fibonacci = start1 + start2
#         start1 = start2
#         start2 = fibonacci
#     print(fibonacci)

# ex-2:
# num = int(input("enter a number: "))
# counter = 1
# for number in range(2, num):
#     if num % number == 0:
#         counter += number
#
# if num % counter == 0:
#     print(True)
# else:
#     print(False)

# ex-3:
# for cohavit in range(6):
#     print("* " * cohavit)
# counter = 4
# for i in range(4):
#     print("* " * counter)
#     counter -= 1

# ex-4:
# side_size = int(input("enter the size that you want: "))
# enter_side_size = side_size
# counter_of_cohavit = 1
# print(" " * enter_side_size, "*" * counter_of_cohavit)
# print()
# for size in range(side_size - 1):
#     counter_of_cohavit += 2
#     enter_side_size -= 1
#     print(" " * enter_side_size,"*" * counter_of_cohavit)
#     print()
# enter_side_size = 2
# for size2 in range(counter_of_cohavit - 1):
#     counter_of_cohavit -= 2
#     if counter_of_cohavit == 1:
#         print(" " * enter_side_size, "*" * counter_of_cohavit)
#     else:
#         print(" " * enter_side_size,"*" * counter_of_cohavit)
#         print()
#         enter_side_size += 1


# Shefa isashar Question:
# products_today = int(input("enter the number of the products today: "))
# counter_of_question = 0
# for shuni in range(20, 25):
#     for counting in range(1, shuni):
#         print(counting)
#         if counting % 3 == 0:
#             counter_of_question += 1
# for countering in range(1, products_today + 1):
#     print(countering)
#     if countering % 3 == 0:
#         counter_of_question += 1
# print("today Ramzi asked ", counter_of_question, " questions")
