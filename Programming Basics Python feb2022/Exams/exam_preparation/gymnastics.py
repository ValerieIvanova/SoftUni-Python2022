country = input()
tool = input()
difficulty_grade = 0
performance_grade = 0
if tool == 'ribbon':
    if country == 'Russia':
        difficulty_grade = 9.1
        performance_grade = 9.4
    elif country == 'Bulgaria':
        difficulty_grade = 9.6
        performance_grade = 9.4
    elif country == 'Italy':
        difficulty_grade = 9.2
        performance_grade = 9.5
elif tool == 'hoop':
    if country == 'Russia':
        difficulty_grade = 9.3
        performance_grade = 9.8
    elif country == 'Bulgaria':
        difficulty_grade = 9.55
        performance_grade = 9.75
    elif country == 'Italy':
        difficulty_grade = 9.45
        performance_grade = 9.35
elif tool == 'rope':
    if country == 'Russia':
        difficulty_grade = 9.6
        performance_grade = 9
    elif country == 'Bulgaria':
        difficulty_grade = 9.5
        performance_grade = 9.4
    elif country == 'Italy':
        difficulty_grade = 9.7
        performance_grade = 9.15
total_grade = difficulty_grade + performance_grade
diff = 20 - total_grade
percent_diff = (diff / 20) * 100
print(f"The team of {country} get {total_grade:.3f} on {tool}.")
print(f"{percent_diff:.2f}%")