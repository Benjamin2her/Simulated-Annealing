from typing import List, Callable
import numpy as np
# import matplotlib.pyplot as plt

Genome = List[int]
Population = List[Genome]
FitnessFunc = Callable[[Genome], int]

def fitnessFunction():
    return 1

# Funcion principal del algoritmo
def genAlgorithm(popsize : int, genome_len : int, ngenerations : int, selCrossover : int, selMutation : int) -> Population:
    population = generatePopulation(popsize, genome_len)

    # Definimos los arreglos auxiliares
    generations =np.array([])
    fit =np.array([])
    f = np.array([])
    f_mean =np.array([])
    x=2

    # Ciclo principal del algoritmo
    for i in range(ngenerations):
        if fitnessFunction(population[0]) == 1:
            break
        
        newGeneration = population[0:2]
        
        for j in range(0, len(population)-2):
            
            # Se hace la seleccion de padres, luego el metodos de cruzamiento y mutacion
            # se seleccionan padres
            parents = parentSelection(population, fitnessFunction, 2) 
            # se hace cruzamiento
            offspring = crossOver(parents[0], parents[1], ...) 
            # se muta posterior al cruzmamiento
            offspring = mutation(offspring)
            offs
            newGeneration += [offspring]
            population = newGeneration
            population = sortPopulation(population, fitnessFunction)

            gens = np.append(gens,i+1)
            fit = np.append(fit,fitnessFunction(population[0]))
        
            for k in range(0,len(population)):
                f = np.append(f,fitnessFunction(population[k]))
        
            f_mean = np.append(f_mean,np.mean(f))
    
    # Impresion de los resultados en pantalla

    print("\n>====| K - Reinas |====<")
    print(">---- Tamaño de Genotipo(K):\t\t", genome_len)
    print(">---- Tamaño de Población:\t\t", popsize)
    print(">---- Máximo de Generaciones:\t\t", ngenerations)
    

    print("\n>====Resultados|====<")
    if fitnessFunction(population[0]) == 1:
        print("Se encontró un óptimo en la generación: ", i+1, "✅")
    else:
        print("No se encontró un óptimo ❌")

    print("\nMejor Resultado")
    print("Genotipo:", population[0], "\nFenotipo:")
    print(genomeToStr(population[0]))
    best = fitnessFunction(population[0])
    if best == 1:
        print("Fitness:", best, "✅\n")
    else:
        print("Fitness:", best, "❌\n")
    
    
    return population