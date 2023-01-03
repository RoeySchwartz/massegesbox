countries = int(input("enter the number of the countries: "))
while countries <= 0:
    countries = int(input("enter the number of the countries: "))
for country in range(countries):
    budget = int(input("enter the budget for this country: "))
    people_counter = 0
    people_pouch_counter = 0
    sum_money = 0
    people = int(input("enter the number of the people in this show: "))
    while people != -999:
        people_pouch_counter = 3
        counter = 0
        for the_people in range(2, people):
            for prime in range(2, people):
                if the_people % prime != 0:
                    counter += 1
            if counter != people - 3:
                people_pouch_counter += 1
            counter = 0
        if people > 0:
            people_counter += people
            people = int(input("enter the number of the people in this show: "))
        else:
            people = -999

    if not people_counter == 0:
        sum_money = budget // people_pouch_counter
        sum_money += 1
        if sum_money >= 50:
            print("you can give the pouch with the sentence. ")
        elif sum_money >= 30:
            sum_money = 50 - sum_money
            print("you can give the pouch with the dedication. ")
            budget = sum_money * people_pouch_counter
            print("the money that you need to complete to the best pouch is: ", budget)
        elif sum_money >= 20:
            sum_money = 50 - sum_money
            print("you can give the standard pouch. ")
            budget = sum_money * people_pouch_counter
            print("the money that you need to complete to the best pouch is: ", budget)
        else:
            sum_money = 50 - sum_money
            print("you can't give any pouch. ")
            budget = sum_money * people_counter
            print("the money that you need to complete to the best pouch is: ", budget)
        print("the number of the people that will get the pouch is: ", people_pouch_counter - 1)