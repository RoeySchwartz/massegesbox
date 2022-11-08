# basic:
# question2:
# num = int(input("enter a number "))
#
# if num % 2 == 0:
#     print("Even ")
# else:
#     print("Odd ")


# question4:
# length = int(input("enter the lengh of a square "))
# width = int(input("enter the width of a square "))
#
# if length == width:
#     print("it's a square ")
# else:
#     print("it's not a square ")


# question8:
# angle1 = int(input("enter the size of the angle "))
# angle2 = int(input("enter the size of the angle "))
#
# if angle1 + angle2 >= 180:
#     print("Triangle's angles add up to 180 degrees. ")
# else:
#     print(180 - angle1 - angle2)

# Advanced:
# question3:
# num = int(input("enter a number "))
# digit = int(input("enter a digit "))
# counter = 0
#
# if num % 10 == digit:
#     counter += 1
# if num // 10 == digit:
#     counter += 1
# print("in the number", num, "there are", counter, "times", digit)


# question5:
# a = int(input("enter the length of the rib "))
# b = int(input("enter the length of the rib "))
# c = int(input("enter the length of the rib "))
#
# if a + b > c and a + c > b and b + c > a:
#     print("it's a triangle ")
# else:
#     print("it's not a triangle ")


# question6:
# city = str(input("enter the name of the city "))
#
# if city == "delhi" or city == "DELHI":
#     print("Red Ford")
# elif city == "agra" or city == "AGRA":
#     print("Taj Mahal")
# elif city == "jaipur" or city == "JAIPUR":
#     print("Jal Mahal")


# question8:
# grade = int(input("enter your grade: "))
#
# if grade < 25:
#     print("F")
# elif 25 <= grade < 45:
#     print("E")
# elif 45 <= grade < 50:
#     print("D")
# elif 50 <= grade < 60:
#     print("C")
# elif 60 <= grade < 80:
#     print("B")
# else:
#     print("A")

# Challenge:
# question1:
# correct1 = 10
# correct2 = 7
# correct3 = 99
# correct4 = 3.14
# final_grade = 0
# counter = 0
#
# answer_for_question1 = int(input("enter your answer "))
# answer_for_question2 = int(input("enter your answer "))
# answer_for_question3 = int(input("enter your answer "))
# answer_for_question4 = float(input("enter your answer "))
#
# if answer_for_question1 == correct1:
#     final_grade += 25
# elif correct1 - 4 <= answer_for_question1 < correct1:
#     final_grade += 12.5
#     counter += 1
# elif answer_for_question1 == correct1 - 10:
#     final_grade += 2
# else:
#     final_grade += 0
#
# if answer_for_question2 == correct2:
#     final_grade += 25
# elif correct2 - 4 <= answer_for_question2 < correct2:
#     final_grade += 12.5
#     counter += 1
# elif answer_for_question2 == correct2 - 10:
#     final_grade += 2
# else:
#     final_grade += 0
#
# if answer_for_question3 == correct3:
#     final_grade += 25
# elif correct3 - 4 <= answer_for_question3 < correct3:
#     if counter <= 1:
#         final_grade += 12.5
#         counter += 1
#         print(counter)
#     else:
#         final_grade += 0
# elif answer_for_question3 == correct3 - 10:
#     final_grade += 2
# else:
#     final_grade += 0
#
# if answer_for_question4 == correct4:
#     final_grade += 25
# elif correct4 - 4 <= answer_for_question4 < correct4:
#     if counter <= 1:
#         final_grade += 12.5
#         counter += 1
#         print(counter)
#     else:
#         final_grade += 0
# elif answer_for_question4 == correct4 - 10:
#     final_grade += 2
# else:
#     final_grade += 0
#
# print("your final grade is ", final_grade)


# question2:
# num = int(input("enter a number "))
#
# if int(num // 1000000) == 0:
#     if num % 2 == 0:
#         if ((num // 10 % 10) % 2) == 0:
#             if ((num // 1000 % 10) % 3) == 0:
#                 print("Your number is a jubilee number")
# else:
#     print("wrong number ")


# question3:
# num1 = int(input("enter a number "))
# num2 = int(input("enter a number "))
#
# if (num1 % 10) % 2 == 0 and (num2 % 10) % 2 != 0 or (num1 % 10) % 2 != 0 and (num2 % 10) % 2 == 0:
#   if (num1 // 10 % 10) % 2 == 0 and (num2 // 10 % 10) % 2 != 0 or
#   (num1 // 10 % 10) % 2 != 0 and (num2 //10 % 10) % 2 == 0:

#         if (num1 // 100) % 2 == 0 and (num2 // 100) % 2 != 0 or (num1 // 100) % 2 != 0 and (num2 // 100) % 2 == 0:
#             print("these numbers are zigzag numbers ")
#         else:
#             print("these numbers are not zigzag numbers ")
#     else:
#         print("these numbers are not zigzag numbers ")
# else:
#     print("these numbers are not zigzag numbers ")


# question4:
# num1 = int(input("enter a number "))
# num2 = int(input("enter a number "))
# num3 = int(input("enter a number "))
# num4 = int(input("enter a number "))
# num5 = int(input("enter a number "))
#
# if num1 > 10:
#     if num2 > 10:
#         if num3 > 10:
#             if num4 > 10:
#                 if num5 > 10:
#                     print("the average is ", (num1 + num2 + num3 + num4 + num5) / 5)


# question5:
# num = float(input("enter a number "))
#
# if num // 1 == int(num % 1 * 1000):
#     print(True)
# else:
#     print(False)
