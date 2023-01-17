# ex-1:
# counter = 0
# for number in range(1, 9):
#     counter += number
# print(counter)

# ex-2:
# for number in range(2, 10, 2):
#     print(number)

# ex-3:
# string = "hello"
# for letter in string:
#     print(letter, end=",")

# ex-4:
# string = "Nitzanim rules!"
# counter_of_i = 0
# for letter in string:
#     if letter == "i":
#         counter_of_i += 1
# print(counter_of_i)

# ex-5:
# counter = 0
# for number in range(5):
#     num = int(input("enter a number: "))
#     if num < 0:
#         break
#     counter += num
# print(counter)

# ex-6:
# STUDENTS = 10
# CLASSES = 5
# were_in_class = 0
# class_number = 0
# student_number = 0
# for class1 in range(1, CLASSES + 1):
#     class_number += 1
#     for student in range(1, STUDENTS + 1):
#         student_number += 1
#         check = int(input("student number " + str(student_number) + " from class " + str(
#             class_number) + " have you been today at school? "))
#         if check == 1:
#             were_in_class += 1
#
#     print("Today were " + str(were_in_class) + " students in class " + str(class_number))
#     were_in_class = 0

# ex-7:
# string = "#"
# counter = 0
# for sulamit in range(10):
#     for sulamit2 in range(10):
#         print(string, end=" ")
#     print("\n")

# ex-8:
# for number in range(100):
#     digit1 = number % 10
#     digit2 = number // 10
#     if number % 7 == 0 or digit2 == 7 or digit1 == 7:
#         print("Boom")
#     else:
#         print(number)

# ex-9:
# sulamit = "#"
# sulamit_counter = 0
# for sulamiot in range(11):
#     for i in range(sulamiot):
#         print(sulamit, end=' ')
#     print()

# ex-10:
# index = 0
# boolean_check = False
# for words in range(10):
#     word = str(input("enter a word: "))
#     for letter in word:
#         if letter == "a":
#             boolean_check = True
#             print(index)
#             break
#         index += 1
#
#     if not boolean_check:
#         print("infinity")
#     index = 0
#     boolean_check = False

# ex-11:
products_input = int(input("enter the number of the products: "))
product = 0
questions = 0
for products in range(1, products_input):
    print("product number: " + str(product))
    if products % 3 == 0:
        questions += 1
    if product == 21 or product == 22 or product == 23 or product == 24:
        products = 1
        print("Shuni interrupted Ramzi")
        product += 1
