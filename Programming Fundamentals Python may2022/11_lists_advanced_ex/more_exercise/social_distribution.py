population = list(map(int, input().split(', ')))
minimum_wealth = int(input())
not_possible = False
if sum(population) < len(population) * minimum_wealth:
    not_possible = True
else:
    for i in range(len(population)):
        wealthiest = population.index(max(population))
        if population[i] < minimum_wealth:
            to_add = minimum_wealth - population[i]
            population[wealthiest] -= to_add
            population[i] += to_add

if not_possible:
    print('No equal distribution possible')
else:
    print(population)