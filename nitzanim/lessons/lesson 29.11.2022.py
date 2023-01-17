# import math
#
# # preparations of the variables:
# PAZMAR_TIME = 30
# RACKET_TIME = 60
# BALLOON_TIME = 120
# PAZMAR = 1
# RACKET = 2
# BALLOON = 3
# FALSE_ALARM = 4
# IRON_DOME_X = 0
# IRON_DOME_Y = 0
# GET_TO_THE_THREAT = 13
#
# X_AREA_A = 10
# Y_AREA_A = 10
# X_AREA_B = 10
# Y_AREA_B = 10
# X_AREA_C = 10
# Y_AREA_C = 10
#
# x = int(input("enter the x axis of the threat"))
# y = int(input("enter the y axis of the threat"))
# threat = int(input("enter the type of the threat"))
# area = ""
# distance = math.sqrt(((x - IRON_DOME_X) ** 2) + ((y - IRON_DOME_Y) ** 2))
#
# AREA_A = x > X_AREA_A and y > Y_AREA_A
# AREA_B = x > X_AREA_B and y <= Y_AREA_B
# AREA_C = x <= X_AREA_C and y > Y_AREA_C
# OPEN_AREA = x <= X_AREA_B and y <= Y_AREA_C
#
# # checking the type of the threat and printing appropriate message:
# if x > 20 or x < 1 or y > 20 or y < 1 or threat > 4 or threat < 1:
#     print("invalid input")
# else:
#     if threat == FALSE_ALARM:
#         print("this is false alarm")
#     else:
#         if OPEN_AREA:
#             print("this threat was in open area")
#
#         # AREA_B:
#         elif AREA_B:
#             if threat == PAZMAR:
#                 if distance > GET_TO_THE_THREAT:
#                     print("Citizens of AREA B")
#                     print("you have 30 seconds to get to the protected place")
#                     print("was not intercepted by iron dome")
#                 else:
#                     print("Citizens of AREA B")
#                     print("you have 30 seconds to get to the protected place")
#                     print("was intercepted by iron dome")
#             elif threat == RACKET:
#                 if distance > GET_TO_THE_THREAT:
#                     print("Citizens of AREA B")
#                     print("you have 60 seconds to get to the protected place")
#                     print("was not intercepted by iron dome")
#                 else:
#                     print("Citizens of AREA B")
#                     print("you have 60 seconds to get to the protected place")
#                     print("was intercepted by iron dome")
#             else:
#                 print("Citizens of AREA B")
#                 print("you have 120 seconds to get to the protected place")
#                 print("was not intercepted by iron dome")
#
#         # AREA_A:
#         elif AREA_A:
#             if threat == PAZMAR:
#                 if distance > GET_TO_THE_THREAT:
#                     print("Citizens of AREA A")
#                     print("you have 30 seconds to get to the protected place")
#                     print("was not intercepted by iron dome")
#                 else:
#                     print("Citizens of AREA A")
#                     print("you have 30 seconds to get to the protected place")
#                     print("was intercepted by iron dome")
#             elif threat == RACKET:
#                 if distance > GET_TO_THE_THREAT:
#                     print("Citizens of AREA A")
#                     print("you have 60 seconds to get to the protected place")
#                     print("was not intercepted by iron dome")
#                 else:
#                     print("Citizens of AREA A")
#                     print("you have 60 seconds to get to the protected place")
#                     print("was intercepted by iron dome")
#             else:
#                 print("Citizens of AREA A")
#                 print("you have 120 seconds to get to the protected place")
#                 print("was not intercepted by iron dome")
#
#         # AREA_C:
#         elif AREA_C:
#             if threat == PAZMAR:
#                 if distance > GET_TO_THE_THREAT:
#                     print("Citizens of AREA C")
#                     print("you have 30 seconds to get to the protected place")
#                     print("was not intercepted by iron dome")
#                 else:
#                     print("Citizens of AREA C")
#                     print("you have 30 seconds to get to the protected place")
#                     print("was intercepted by iron dome")
#             elif threat == RACKET:
#                 if distance > GET_TO_THE_THREAT:
#                     print("Citizens of AREA C")
#                     print("you have 60 seconds to get to the protected place")
#                     print("was not intercepted by iron dome")
#                 else:
#                     print("Citizens of AREA C")
#                     print("you have 60 seconds to get to the protected place")
#                     print("was intercepted by iron dome")
#             else:
#                 print("Citizens of AREA C")
#                 print("you have 120 seconds to get to the protected place")
#                 print("was not intercepted by iron dome")
