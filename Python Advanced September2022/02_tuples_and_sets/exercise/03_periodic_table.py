lines = int(input())
unique_chemical_elements = set()

for _ in range(lines):
    element = input().split()
    [unique_chemical_elements.add(el) for el in element]
print(*unique_chemical_elements, sep='\n')