import random
from typing import List, Tuple

Genome = List[float]

def fitness_function(genome: Genome) -> float:
    return sum(genome)

def init_population(population_size: int, genome_len: int) -> List[Genome]:
    return [
        [random.randint(0, 1) for _ in range(genome_len)] \
        for _ in range(population_size)
    ]

def selection(population: List[List[int]], fitness_fn) -> List[List[int]]:
    return sorted(population, 
                  key = fitness_fn, 
                  reverse = True)[:len(population)//2]

def crossover(parent_a: Genome, parent_b: Genome) -> Tuple[Genome, Genome]:
    point = random.randint(1, len(parent_a) - 1)
    return  parent_a[:point] + parent_b[point:], \
            parent_b[:point] + parent_a[point:]

def mutation(genome: Genome, p: float) -> Genome:
    return [1 - g if random.random() < p else g for g in genome]

def gen_algorithm(  population_size:   int,
                    genome_len:        int, 
                    num_generations:   int,
                    sel_crossover:   float,
                    sel_mutation:    float
                ) -> List[Genome]:
    
    population = init_population(population_size, genome_len)

    for _ in range(num_generations):
        parents = selection(population, fitness_function)

        for _ in range(num_generations):
        # Select parents
            parents = selection(population, fitness_function)
            # Create new offspring
            offspring = []
            for _ in range(population_size // 2):
                parent_a = random.choice(parents)
                parent_b = random.choice(parents)
                offspring_a, offspring_b = crossover(parent_a, parent_b)
                offspring_a = mutation(offspring_a, sel_mutation)
                offspring_b = mutation(offspring_b, sel_mutation)
                offspring.append(offspring_a)
                offspring.append(offspring_b)
            # Replace the old population with the new offspring
            population = offspring
    # Return the final population
    return population




def main():
    print("Hola")

if __name__ == '__main__':
    main()