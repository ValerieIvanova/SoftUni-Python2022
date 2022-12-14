def age_assignment(*args, **kwargs):
    people = {}
    for letter, age in kwargs.items():
        for name in args:
            if name.startswith(letter):
                people[name] = age
    sorted_people = sorted(people.items())
    result = ""
    for name, age in sorted_people:
        result += f"{name} is {age} years old." + '\n'
    return result


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))