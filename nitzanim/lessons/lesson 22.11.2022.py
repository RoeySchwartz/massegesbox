# ex_1:
# EVEN = "Even"
# ODD = "Odd"
# number = 9
# if number % 2 == 0:
#     print(9, "is", EVEN)
# else:
#     print(9, "is", ODD)
# number = 8
# if number % 2 == 0:
#     print(8, "is", EVEN)
# else:
#     print(8, "is", ODD)

# # ex_2:
# length = int(input("Enter length: "))
# width = int(input("Enter width: "))
# total_fence = 2 * length + 2 * width
# if total_fence < 120:
#     print("Request received")
# else:
#     print("Choose shorter fence")

# ex board:
#
# day = int(input("enter the day: "))
# time = int(input("enter the time: "))
# action = int(input("enter the action that you want to do: "))
# hours = time // 100
# minutes = time % 100

# if 1 <= day <= 7:
#     if day == 6 or day == 7:
#         if 8 <= hours <= 10:
#             if action == 1:
#                 print("you can to get in")
#             else:
#                 print("you can't get in")
#         elif 10 <= hours <= 14:
#             if action == 2:
#                 print("you can get in")
#             else:
#                 print("you can't get in")
#         else:
#             print("you can't get in")
#     elif day == 2:
#         if 7 <= hours <= 11:
#             if action == 1:
#                 print("you can get in")
#             else:
#                 print("you can't get in")
#         elif 11 <= hours <= 23:
#             if action == 2:
#                 print("you can get in")
#             else:
#                 print("you can't get in")
#         else:
#             print("you can't get in")
#     elif day == 4:
#         if 7 <= hours <= 11:
#             if action == 1:
#                 print("you can get in")
#             else:
#                 print("you can't get in")
#         elif 11 <= hours < 15:
#             if action == 2:
#                 print("you can get in")
#             else:
#                 print("you can't get in")
#         elif 16 <= hours <= 21:
#             if action == 2:
#                 print("you can get in")
#             else:
#                 print("you can't get in")
#         else:
#             print("you can't get in")
#     else:
#         if 7 <= hours <= 11:
#             if action == 1:
#                 print("you can get in")
#             else:
#                 print("you can't get in")
#         elif 11 <= hours <= 21:
#             if action == 2:
#                 print("you can get in")
#             else:
#                 print("you can't get in")
#         else:
#             print("you can't get in")
# else:
#     print("you can't get in")
