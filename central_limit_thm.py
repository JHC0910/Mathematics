import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def Sample_means(a):
    dice = [1, 2, 3, 4, 5, 6]

    sample_means = []

    for times in range(1,101):
        r = np.random.choice(dice, a)
        sample_means.append(r.mean())
    return sample_means
    
samples = 100000

df = pd.DataFrame(Sample_means(samples))
df.plot(kind = "density")

plt.title(str(samples) + "times")

plt.show()
