import math
import random
DIGITS_AFTER_DOT = 2

training_area_length_input = float(input("enter the length of the training area: "))
TRAINING_AREA_LENGTH = int(training_area_length_input)
TRAINING_AREA = TRAINING_AREA_LENGTH ** 2

X_plain_location = TRAINING_AREA_LENGTH // 2
Y_plain_location = TRAINING_AREA_LENGTH // 2
print(X_plain_location)

targets = int(input("enter the number of the targets that the pilot have: "))
FUEL_PER_KM = 5
fuel_calculate = targets * TRAINING_AREA_LENGTH * FUEL_PER_KM * 0.6
fuel_of_train = int(fuel_calculate)
print(fuel_of_train)
number_of_bombed_targets = 0

print("You need to bomb", targets, "targets. The amount of fuel you get is", fuel_of_train, "liters.")
print("Navigation keys:")
print("N for North")
print("S for South")
print("E for East")
print("w for West")

coach = str(input("Do you want to be the present on the flight? "))
if coach == "Y":
    X_target_location = int(input("enter the loc x: "))
    Y_target_location = int(input("enter the loc y: "))
else:
    X_target_location = random.randint(0, TRAINING_AREA_LENGTH)
    Y_target_location = random.randint(0, TRAINING_AREA_LENGTH)
X_calculate = (X_plain_location - X_target_location) ** 2
Y_calculate = (Y_plain_location - Y_target_location) ** 2
distance = math.sqrt(X_calculate + Y_calculate)
distance = round(distance, DIGITS_AFTER_DOT)
while number_of_bombed_targets != targets:
    if fuel_of_train == 0:
        break
    if coach != "YES":
        X_target_location = random.randint(0, TRAINING_AREA_LENGTH)
        Y_target_location = random.randint(0, TRAINING_AREA_LENGTH)
    else:
        X_target_location = int(input("enter the x loc: "))
        Y_target_location = int(input("enter the y loc: "))
    while 0 <= X_target_location <= TRAINING_AREA_LENGTH and 0 <= Y_target_location <= TRAINING_AREA_LENGTH:
        direction = ""
        while X_target_location != X_plain_location or Y_target_location != Y_plain_location or fuel_of_train == 0:
            ask_for_fuel = str(input("Do you want that i tell you GPS information? "))
            if ask_for_fuel == "YES":
                print("AIRLINE DISTANCE:", distance)
                if X_plain_location > X_target_location and Y_plain_location > Y_target_location:
                    print("the target is on the SOUTH-WEST side")
                elif X_plain_location < X_target_location and Y_plain_location > Y_target_location:
                    print("the target is on the SOUTH-EAST side")
                elif X_plain_location > X_target_location and Y_plain_location < Y_target_location:
                    print("the target is on the NORTH-WEST side")
                elif X_plain_location < X_target_location and Y_plain_location < Y_target_location:
                    print("the target is on the NORTH-EAST side")
                elif X_plain_location > X_target_location:
                    print("the target is on the WEST side")
                elif X_plain_location < X_target_location:
                    print("the target is on the EAST side")
                elif Y_plain_location > Y_target_location:
                    print("the target is on the SOUTH side")
                elif Y_plain_location < Y_target_location:
                    print("the target is on the NORTH side")
                fuel_of_train -= 3
                print("FUEL LEFT: ", fuel_of_train)
            direction = str(input("enter the direction that you fly to: "))
            if direction == "N":
                Y_plain_location += 1
                fuel_of_train -= 5
                if fuel_of_train == 0:
                    print("CRASH - GAME OVER")
                    break
            elif direction == "NE" or direction == "EN":
                X_plain_location += 1
                Y_plain_location += 1
                fuel_of_train -= 5
                if fuel_of_train == 0:
                    print("CRASH - GAME OVER")
                    break
            elif direction == "NW" or direction == "WN":
                X_plain_location -= 1
                Y_plain_location += 1
                fuel_of_train -= 5
                if fuel_of_train == 0:
                    print("CRASH - GAME OVER")
                    break
            elif direction == "S":
                Y_plain_location -= 1
                fuel_of_train -= 5
                if fuel_of_train == 0:
                    print("CRASH - GAME OVER")
                    break
            elif direction == "SE" or direction == "ES":
                X_plain_location -= 1
                Y_plain_location -= 1
                fuel_of_train -= 5
                if fuel_of_train == 0:
                    print("CRASH - GAME OVER")
                    break
            elif direction == "SW" or direction == "WS":
                X_plain_location -= 1
                Y_plain_location -= 1
                fuel_of_train -= 5
                if fuel_of_train == 0:
                    print("CRASH - GAME OVER")
                    break
            elif direction == "E":
                X_plain_location += 1
                fuel_of_train -= 5
                if fuel_of_train == 0:
                    print("CRASH - GAME OVER")
                    break
            elif direction == "W":
                X_plain_location -= 1
                fuel_of_train -= 5
                if fuel_of_train == 0:
                    print("CRASH - GAME OVER")
                    break
        else:
            print("Target Bombed!")
            number_of_bombed_targets += 1
        if number_of_bombed_targets == targets:
            break
        else:
            if fuel_of_train == 0:
                break
            else:
                X_target_location = int(input("enter the target location on the X axis: "))
                Y_target_location = int(input("enter the target location on the Y axis: "))
    else:
        print("Error. the target is out of area!")
else:
    if number_of_bombed_targets == targets:
        print("Great Job! All targets are bombed!")
    else:
        print("CRASH - GAME OVER")