from collections import defaultdict

company_info = defaultdict(list)
while True:
    command = input()
    if command == 'End':
        break
    company, id = command.split(' -> ')
    if id not in company_info[company]:
        company_info[company].append(id)
for company, id in company_info.items():
    employees = '\n-- '.join(id)
    print(f"{company}\n"
          f"-- "
          f"{employees}")