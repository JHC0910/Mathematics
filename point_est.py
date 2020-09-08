import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dice = [1, 2, 3, 4, 5, 6]

population = []

for i in range(10000):
    sample = np.random.choice(dice, 100)
    population.append(sample.mean())

print("population average="+ str(sum(population)/10000))


size = [10, 100, 1000]

for s in size:
    samples = np.random.choice(population, s)
    average = samples.mean()
    print(str(s)+"sample average="+ str(average))

