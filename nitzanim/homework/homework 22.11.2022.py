# challenge ex4:

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

# challenge ex1:

# q1:
# Harmioni = int(input("enter your card "))
# Hari = int(input("enter your card "))
# Ron = int(input("enter your card "))
#
# if Harmioni > Hari and Harmioni > Ron:
#     if Hari + Ron == Harmioni:
#         if Hari > Ron:
#             print("the winner is Ron")
#         elif Ron > Hari:
#             print("The winner is Hari")
#         else:
#             print("there is no winner")
#     else:
#         print("The winner is Harmioni")
#
# elif Hari > Harmioni and Hari > Ron:
#     if Harmioni + Ron == Hari:
#         if Harmioni > Ron:
#             print("The winner is Ron")
#         elif Ron > Harmioni:
#             print("The winner is Harmioni")
#         else:
#             print("there is no winner")
#     else:
#         print("The winner is Hari")
#
# elif Ron > Hari and Ron > Harmioni:
#     if Hari + Harmioni == Ron:
#         if Hari > Harmioni:
#             print("the winner is Harmioni")
#         elif Harmioni > Hari:
#             print("The winner is Hari")
#         else:
#             print("There is no winner")
#     else:
#         print("The winner is Ron")
