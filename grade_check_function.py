from tabulate import tabulate

grade_table = [['A','B','C','Fail'],['> 70','70-55','54-40','< 40']]

print(tabulate(grade_table))

def grade_check():
    if marks_int == 69:
        print("Nice")
    elif marks_int > 70:
        print("A")
    elif marks_int <= 70 and marks_int >= 55:
        print("B")
    elif marks_int < 55 and marks_int >= 40:
        print("C")
    else:
        print("Fail")

while True:
    marks = input('Marks:')
    marks_int = int(marks)
    grade_check()