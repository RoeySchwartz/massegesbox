# introduction:
# q1:
# full_name = str(input("enter your full name "))
#
# print(f"Hello {full_name} Welcome to our program! ")

# q5:
# MAGIC_NUMBER = 5
# num = int(input("enter a number "))
#
# print(MAGIC_NUMBER, num, MAGIC_NUMBER)

# q6:
# num = int(input("enter a number "))
#
# print(num, end="*")
# print(num, end="*")
# print(num)

# q7:

# Company = str(input("enter your company name "))
# Business_description = str(input("enter the job that you expect for "))
# City = str(input("enter where is the office "))
# Phone_number = int(input("enter your phone number "))
#
# Name = str(input("enter your full name "))
# Role = str(input("enter your role "))
# Mail = str(input("enter your mail "))
#
# print(f"{Company}\n{Business_description}\n{City}\n{Phone_number}\n{Name}\n{Role}\n{Mail}\n")

# Basic:
# q6:
# number1 = int(input("enter a number "))
# number2 = int(input("enter a number "))
# summer = number1+ number2
#
# print(summer)
# print(summer%5)

# q9
# number_of_checks = int(input("enter the number of the checks "))
# number_of_the_positive = int(input("enter the number of the positive checks "))
#
# print((number_of_the_positive*100)/number_of_checks)

# q15
# number_of_the_people = int(input("enter the number of the people "))
# print(f"you need to choose {number_of_the_people//3} tents")

# Advanced:
# q7
# number_of_the_works_hours = int(input("enter the number of your hours work "))
# salary_for_an_hour = int(input("enter your salary "))
# salary_for_a_month = salary_for_an_hour * number_of_the_works_hours
#
# income_tax = salary_for_a_month * 0.1
# socialy_security_tax = salary_for_a_month * 0.05
# health_tax = salary_for_a_month * 0.1
#
# real_salary = salary_for_a_month - income_tax - socialy_security_tax - health_tax
#
# print(f"your salary is {real_salary}")

# q8
# celsius = int(input("enter the degrees in celsius "))
# farenhit = ((celsius * 9) / 5) + 32
#
# print(f"the degrees in farenhit is {farenhit} degrees")

# challenge:
# q1:
# x = int(input("enter a number "))
# x += 1
#
# print(x * x * 50)

# q2:
# student1 = int(input("enter your grade "))
# student2 = int(input("enter your grade "))
# student3 = int(input("enter your grade "))
#
# average = (student1 + student2 + student3) // 3
# check = (average / 100) + 0.44
# average *= int(check)
#
# print(average)
# print("your grade is ",average)


# q3:
# status = int(input("enter your status- if you are youth press 1, if you are adult press 0 "))
# print((status + 1) * -50 + 150)

# q4:
# num = float(input("enter a number "))
# print(int(num + 0.5))

# q5:
# num = int(input("enter a number "))
# x = int(input(" enter the type of the number if it is a binary number enter '2', if it is octal press '8' "))
#
# digit1 = num % 10
# digit2 = num // 10 % 10
# digit3 = num // 100
#
# print((digit1 * (x ** 0)) + (digit2 * (x ** 1)) + (digit3 * (x ** 2)))

print(5 * "friends" // 8)
