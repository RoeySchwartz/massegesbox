# Basic
# q1:
# plant = str(input("enter the type of the plant: "))
# height = int(input("enter the height of the plant: "))
#
# if plant == "flower" and height > 30:
#     print("it costs 25 shekels ")
# elif plant == "flower" and height != 30:
#     print("it costs 15 shekels ")
# elif plant == "bush" and height > 60:
#     print("it costs 95 shekels ")
# elif plant == "bush" and height != 60:
#     print("it costs 70 shekels ")

# q2:
# option = int(input("enter your option "))
# string = str(input("enter a string "))
#
# match option:
#     case 1:
#         print(string+string)
#     case 2:
#         print("*"+string+"*")
#     case 3:
#         string2 = str(input("enter another string "))
#         print(string2+string+string2)
#     case other:
#         print("wrong option")

# q4:
# number = int(input("enter a number: "))
#
# if number % 2 == 0:
#     if number % 3 == 0:
#         print("this number is divisible by 2 and 3")

# q7:
# carbonated_drink = str(input("Do you want to drink carbonated drink? "))
# sugary_drink = str(input("do you want to drink sugary drink? "))
#
# if carbonated_drink == "yes" and sugary_drink == "yes":
#     print("i'll give you cola")
# elif carbonated_drink == "yes":
#     print("i'll give you soda")
# elif sugary_drink == "yes":
#     print("i'll give you raspberry")
# else:
#     print("i'll give you water")

# carbonated_drink = str(input("Do you want to drink carbonated drink?"))
# sugary_drink = str(input("Do you want to drink sugary drink? "))
#
# match carbonated_drink:
#     case "yes":
#         if sugary_drink == "yes":
#             print ("i'll give you cola")
#         else:
#             print("i'll give you soda")
#     case "no":
#         if sugary_drink == "yes":
#             print("i'll give you raspberry")
#         else:
#             print("i'll give you water")

# Advanced:
# q3:
# gender = str(input("are you male or female? "))
#
# if gender == "male":
#     married = str(input("Are you married to one of your friend? "))
#     kid = str(input("Do you have a kid with one of your friends? "))
#     if married == "yes":
#         print("you are chandler ")
#     elif kid == "yes":
#         print("you are rose ")
#     else:
#         print("you are joey ")
# else:
#     married = str(input("Are you married with one of your friends? "))
#     kid = str(input("Do you have a kid with one of your friends? "))
#     if married == "yes":
#         print("you are monika ")
#     elif kid == "yes":
#         print("you are rachel ")
#     else:
#         print("you are fibi ")

# q5:
# budget = int(input(" Enter a budget for your pet food: "))
# pet = str(input("Do you have cat or dog? "))
#
# if pet == "dog":
#     if 20 <= budget < 40:
#         print("You should choose the basic dog food ")
#     elif budget >= 40:
#         print("You should choose the expensive dog food ")
# else:
#     if 50 <= budget < 100:
#         print("You should choose the basic cat food ")
#     elif budget >= 100:
#         print("You should choose the expensive cat food ")

# Challenge:
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

# q2:
# number = int(input("enter a number "))
# counter = 0
#
# if number % 2 != 0 and number % 3 != 0 and number % 5 != 0 and number % 7 != 0 and 10 <= number <= 100:
#     print("this number is prime number ")
# elif number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number % 7 == 0:
#     if number % 2 == 0:
#         counter += 1
#     if number % 3 == 0:
#         counter += 1
#     if number % 5 == 0:
#         counter += 1
#     if number % 7 == 0:
#         counter += 1
#     print("this number is divisible in" , counter, "of the special numbers ")
# else:
#     print("the number is not in the range")

# q3:
# long_of_your_call = int(input("enter the long of your call"))
#
# if long_of_your_call <= 10:
#     long_of_your_call *= 3
#     print("you have to pay", long_of_your_call)
# elif 10 < long_of_your_call <= 30:
#     ten_minutes = 30
#     long_of_your_call -= 10
#     long_of_your_call *= 2
#     print("you have to pay", long_of_your_call + ten_minutes)
# else:
#     ten_minutes = 10 * 3
#     twenty_minutes = 20 * 2
#     long_of_your_call -= 30
#     print("you have to pay", ten_minutes + twenty_minutes+ long_of_your_call)

# q4:
# first_name_A_person = str(input("enter your first name "))
# last_name_A_person = str(input("enter your last name "))
#
# first_name_B_person = str(input("enter your first name "))
# last_name_B_person = str(input("enter your last name "))
#
# if last_name_A_person == last_name_B_person:
#     if first_name_B_person == first_name_A_person:
#         print("not family members")
#     else:
#         print("family members")
# else:
#     last_name_parent_b_personA = str(input("enter your family name "))
#     last_name_parent_b_personB = str(input("enter your family name "))
#     if last_name_parent_b_personA == last_name_parent_b_personB:
#         first_name_b_personA = str(input("enter your first name "))
#         first_name_b_personB = str(input("enter your first name "))
#         if first_name_b_personA == first_name_b_personB:
#             print("not family members")
#         else:
#             print("family members")
#     elif last_name_parent_b_personA == last_name_B_person:
#         first_name_parent_b_personA = str(input("enter your first name "))
#         first_name_parent_a_personB = str(input("enter your first name "))
#         if first_name_parent_a_personB == first_name_parent_b_personA:
#             print("not family members ")
#         else:
#             print("family members")
#     elif last_name_parent_b_personB == last_name_A_person:
#         first_name_parentB_personB = str(input("enter your first name "))
#         first_name_parentA_personA = str(input("enter your first name "))
#         if first_name_parentA_personA == first_name_parentB_personB:
#             print("not family members")
#         else:
#             print("family members")
#     else:
#         print("not family members")
