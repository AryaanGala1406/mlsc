# f(x) = x^2
# f(x) 2*x^2+1*x+4
import math
import numpy as np
import random

def fitness(x):
    # return ((2*(x**2))+(2*x)+4)
    return x * np.sin(10 * np.pi * x) + 1.0

pop_size = int(input("Enter the population size: "))
generations = int(input("Enter the number of generatiosns: "))
lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))

population = [random.uniform(lower, upper) for _ in range(pop_size)]

for gen in range(generations):
    fitnesses = [max(fitness(x), 0.00000001) for x in population]
    best = max(population, key=fitness)
    print(f"For generation {gen+1} best is : {best}")
    new_pop = []

    for _ in range(pop_size):
        p1, p2 = random.choices(population, weights=fitnesses, k=2)
        child = (p1+p2)/2
        if random.random() < 0.1:
            child += random.uniform(1,-1)*0.1
        child = max(min(child, upper), lower)
        new_pop.append(child)
    population = new_pop

best = max(population, key=fitness)

x = np.linespace(lower, upper, 100)
y = fitness(x)

plt.plot(x,y)
plt.show()
print("Best x: ", best)
print("Best f(x): ", fitness(best))