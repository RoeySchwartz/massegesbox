# Basic:
# ex-2:
# counter = 1
# while counter != 10:
#     print(2 ** counter)

# ex-3:
# pizza_slices = int(input("enter the number of the slices that you want: "))
# counter_slices = 0
# while pizza_slices != 0:
#     counter_slices += pizza_slices
#     pizza_slices = int(input("enter the number of the slices that you want: "))
# if counter_slices % 8 != 0:
#     print("you need: ", counter_slices // 8 + 1)
# else:
#     print("you need: ", counter_slices // 8)

# ex-5:
# name = str(input("enter your name: "))
# weight = int(input("enter your weight: "))
# counter = weight
# while counter < 200:
#     counter += weight
#     name = str(input("enter your name: "))
#     weight = int(input("enter your weight: "))
# print(name, "get out of the elevator please")

# ex-6:
# line = str(input("enter the next line: "))
# counter = ""
#
# while line != "Hallas":
#     counter += line + "\n"
#     print(counter)
#     line = str(input("enter the next line: "))

# ex-9:
# liters = str(input("enter the number of the liters: "))
# counter = 0
#
# while liters != "Done":
#     counter += int(liters)
#     liters = str(input("enter the number of the liters: "))
# print("you have paid in the past months ", counter / 6.3, " dollars")

# Advanced:
# ex-1:
# number = int(input("enter a number: "))
# i = 1
#
# while i != number:
#     if number % i != 0:
#         print(i)
#         break
#     else:
#         i += 1

# ex-3:
# number = int(input("enter a number: "))
# i = 2
# check = 0
#
# while i != number:
#     if number % i == 0:
#         i = 2
#         number = int(input("enter a number: "))
#         pass
#     else:
#         i += 1
#         check += 1
# print("the number", number, "is a prime number")

# ex-6:
# number = str(input("enter a number: "))
# i = 2
# biggest = 0
#
# while number != "END":
#     while i != int(number):
#         if int(number) % i == 0:
#             biggest = i
#         i += 1
#     print("the biggest divisor of", number ,"is:", biggest)
#     number = str(input("enter a number: "))

# ex-8:
# pages = int(input("enter the number of the pages: "))
#
# words_counter = 0
# lines_counter = 0
# pages_counter = 0
#
# while pages_counter != pages:
#     pages_counter += 1
#     lines = int(input("enter the number of the lines in every page: "))
#     lines_counter = 0
#     while lines_counter != lines:
#         words = int(input("enter the number of the words in every line: "))
#         words_counter += words
#         lines_counter += 1
#
# print("there are in the notebook", words_counter ,"words")
