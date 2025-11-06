import random

POPULATION_SIZE = 100
GENES = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890, .-;:_!"#%&/()=?@${[]}'''
TARGET = "Hello World!"

class Individual:
    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = self.calc_fitness()

    @classmethod
    def create_gnome(cls):
        return ''.join(random.choice(GENES) for _ in range(len(TARGET)))

    def mate(self, par2):
        child = ""
        for gp1, gp2 in zip(self.chromosome, par2.chromosome):
            prob = random.random()
            if prob < 0.45:
                child += gp1
            elif prob < 0.90:
                child += gp2
            else:
                child += random.choice(GENES)
        return Individual(child)

    def calc_fitness(self):
        return sum(abs(ord(a) - ord(b)) for a, b in zip(self.chromosome, TARGET))

def genetic_algorithm():
    generation = 0
    population = [Individual(Individual.create_gnome()) for _ in range(POPULATION_SIZE)]

    while True:
        population = sorted(population, key=lambda x: x.fitness)
        if population[0].fitness == 0:
            print(f"Generation: {generation}, String: {population[0].chromosome}, Fitness: {population[0].fitness}")
            break
        new_generation = population[:10]  # Elitism: 10% fittest preserved
        s = 90
        for _ in range(s):
            parent1 = random.choice(population[:50])
            parent2 = random.choice(population[:50])
            child = parent1.mate(parent2)
            new_generation.append(child)
        population = new_generation
        print(f"Generation: {generation}, String: {population[0].chromosome}, Fitness: {population[0].fitness}")
        generation += 1

if __name__ == "__main__":
    genetic_algorithm()
