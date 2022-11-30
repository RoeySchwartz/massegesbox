# # PREPARATIONS:
#
# DEFAULT_QUARANTINE_DAYS = 7
# RED_COUNTRY = "guatemala"
# UPDATED_SICK_COVID_NUMBERS = 673
# NUMBER_OF_NEGATIVE_TESTS = 2
# ADHESION_COEFFICIENT = 0
#
# name = str(input("enter traveler name: "))
# country = str(input("enter the country that you want to come from: "))
# flight = int(input("enter the length of the flight: "))
# quaratine = DEFAULT_QUARANTINE_DAYS
# family_number = int(input("enter the number of the family members the were with you: "))
# family_sick_member = str(input("Does someone in your family has covid? "))
# negative_tests = str(input("do you have " + str(NUMBER_OF_NEGATIVE_TESTS) + " negative tests? "))
#
# # CODE:
# if family_sick_member == "y":
#     days_until_tests_of_family_member = int(input("after how many days of isolation he was tested?"))
#     quaratine += days_until_tests_of_family_member
#     if days_until_tests_of_family_member < 0 or days_until_tests_of_family_member > 7:
#         print("invalid value. Stay in quaratine for " + str(DEFAULT_QUARANTINE_DAYS) + " days!")
# if flight <= 0 or flight > 24 or family_number <= 0 or family_sick_member != "y" and family_sick_member != "n" or negative_tests != "y" and negative_tests != "n":
#     print("invalid value. Stay in quaratine for " + str(DEFAULT_QUARANTINE_DAYS) + " days!")
# elif country == RED_COUNTRY:
#     print("you can't get in israel.")
# elif country == "israel":
#     print(name + " you don't need to be in quarantine after in-state flight")
# else:
#     if negative_tests == "y":
#         quaratine = 1
#     ADHESION_COEFFICIENT = ((quaratine * flight * family_number) / UPDATED_SICK_COVID_NUMBERS)
#     if ADHESION_COEFFICIENT > 1.5:
#         quaratine += 2
#     print("the adhesion coefficient now is ", ADHESION_COEFFICIENT)
#     print(name, "must stay in quaratine for ", quaratine, " days")
