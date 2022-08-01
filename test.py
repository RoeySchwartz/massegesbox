file = input("enter a name of a file: ")

user_name = str(input("enter the username: "))

grade = int(input("enter the grade: "))

try:
    file1 = open(file,"r+")
    file1.write(user_name)
    file1.write("got the grade ")
    file1.write(grade)
except FileNotFoundError:
    print("file not found try another name ")
except ValueError:
    if not grade.isdigit():
        print("syntax error check your grade ")
except TypeError:
    print("you can't write 3 arguments, write 1 only")