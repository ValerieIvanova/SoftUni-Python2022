def grade_text(grade):
    result = None
    if grade < 3:
        result = 'Fail'
    elif grade <= 3.49:
        result = 'Poor'
    elif grade <= 4.49:
        result = 'Good'
    elif grade <= 5.49:
        result = 'Very Good'
    elif grade <= 6.00:
        result = 'Excellent'
    return result


current_grade = float(input())
print(grade_text(current_grade))