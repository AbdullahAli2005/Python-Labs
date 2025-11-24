from deap import base, creator, tools, gp
import operator, math, random, numpy as np
from sklearn.metrics import mean_squared_error

# Define the target function: 5x^3 - 6x^2 + 8x = 1
def target_function(x):
    return 5*x**3 - 6*x**2 + 8*x - 1

# Step 1: Define primitive set (functions and terminals)
pset = gp.PrimitiveSet("MAIN", 1)  # one input variable (x)
pset.renameArguments(ARG0='x')

# Basic arithmetic operators
pset.addPrimitive(operator.add, 2)
pset.addPrimitive(operator.sub, 2)
pset.addPrimitive(operator.mul, 2)

# Protected division to avoid division by zero
def protected_div(left, right):
    try:
        return left / right
    except ZeroDivisionError:
        return 1
pset.addPrimitive(protected_div, 2)

# Some useful math functions
pset.addPrimitive(math.sin, 1)
pset.addPrimitive(math.cos, 1)

# Constants and variables
pset.addEphemeralConstant("rand101", lambda: random.uniform(-1, 1))

# Step 2: Define fitness and individual
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", gp.PrimitiveTree, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("expr", gp.genHalfAndHalf, pset=pset, min_=1, max_=3)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.expr)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Step 3: Define evaluation function
def evalSymbReg(individual, points):
    func = toolbox.compile(expr=individual)
    predictions = [func(x) for x in points]
    targets = [target_function(x) for x in points]
    return mean_squared_error(targets, predictions),

toolbox.register("compile", gp.compile, pset=pset)
toolbox.register("evaluate", evalSymbReg, points=[x/10. for x in range(-10, 10)])
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("mate", gp.cxOnePoint)
toolbox.register("expr_mut", gp.genFull, min_=0, max_=2)
toolbox.register("mutate", gp.mutUniform, expr=toolbox.expr_mut, pset=pset)

# Step 4: Evolution parameters
toolbox.decorate("mate", gp.staticLimit(key=len, max_value=17))
toolbox.decorate("mutate", gp.staticLimit(key=len, max_value=17))

def main():
    random.seed(42)
    population = toolbox.population(n=200)
    NGEN, CXPB, MUTPB = 30, 0.5, 0.2

    print("Evolution process starts...")
    for gen in range(NGEN):
        offspring = tools.selTournament(population, len(population), tournsize=3)
        offspring = list(map(toolbox.clone, offspring))

        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < CXPB:
                toolbox.mate(child1, child2)
                del child1.fitness.values, child2.fitness.values

        for mutant in offspring:
            if random.random() < MUTPB:
                toolbox.mutate(mutant)
                del mutant.fitness.values

        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit

        population[:] = offspring

        fits = [ind.fitness.values[0] for ind in population]
        print(f"Generation {gen}: Min = {min(fits):.4f}, Avg = {np.mean(fits):.4f}")

    print("\nEvolution ends.")
    best_ind = tools.selBest(population, 1)[0]
    print("\nBest individual:", best_ind)
    print("Fitness (MSE):", best_ind.fitness.values[0])

if __name__ == "__main__":
    main()
