marks = int(input("what is your marks in programing:"))

def show_grade(grade):
    print(f"you got: {grade}")


if marks > 80:
    show_grade('A+')
elif marks <80 and marks > 70:
    show_grade('A')
elif marks<70 and marks > 60:
    show_grade('A-')
