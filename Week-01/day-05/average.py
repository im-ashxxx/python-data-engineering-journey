def calculate_average(marks):
    if not marks:
        return 0
    sum_marks = 0
    for mark in marks:
        sum_marks += mark
    return sum_marks / len(marks)
