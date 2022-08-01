def fun():
    grades = []
    for i in range(8):
        grade = int(input("enter your grade "))
        grades.append(grade)

    average = 0
    for i in grades:
        average += i

    average1 = average / 8
    print("the average is", average1)

    index_x = []

    for o in grades:
        if o > average1:
            index_x.append(o)

    print("the grades that over the average", index_x)
    over_60 = []

    for r in grades:
        if r >= 60:
            over_60.append(r)
    print("the grade that is 60 or over 60 are ", over_60)

    if average1 > 90:
        print("A+")


fun()

