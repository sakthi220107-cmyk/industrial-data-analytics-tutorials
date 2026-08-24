import numpy as np
import matplotlib.pyplot as plt
import scipy as sc

np.random.seed(42)

population = np.array([15, 17, 11, 15, 13, 12, 17, 9, 12, 14, 15, 12, 13, 10, 16, 15, 16, 15, 14, 19,
14, 18, 10, 16, 17, 15, 17, 17, 19, 12, 16, 11, 14, 19, 15, 14, 15, 13, 14, 14,
14, 15, 17, 17, 17, 10])

pop_mean = population.mean()
pop_std = population.std()
print('population_mean = ', pop_mean)
print('population_std = ', pop_std)

samples = 1000
sample_size = [5,10]
results = {}

for i in sample_size :
    sample_mean = np.array([
        np.random.choice(population,size = i, replace=True).mean()
        for j in range(samples)
    ])

    experimental_std = sample_mean.std(ddof=1)
    theoretical_std = pop_std/np.sqrt(i)
    results[i] = {
        "means": sample_mean,
        "empirical_se": experimental_std,
        "theoretical_std": theoretical_std,
    }

    print(f"Sample size n = {i}")
    print(f"  Empirical SE   (std of 1,000 sample means): {experimental_std:.4f}")
    print(f"  Theoretical SE (population_std / sqrt(n))  : {theoretical_std:.4f}")

fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))

for ax, n in zip(axes, sample_size):
    means = results[n]["means"]
    theoretical_se = results[n]["theoretical_std"]

    ax.hist(means, bins=30, density=True, alpha=0.6,edgecolor="black", label="Sample means")

    x = np.linspace(means.min(), means.max(), 300)
    pdf = sc.stats.norm.pdf(x, loc=pop_mean, scale=theoretical_std)
    ax.plot(x, pdf, "r-", lw=2, label="Theoretical normal PDF")

    ax.axvline(pop_mean, color="green", linestyle="--", lw=2,label=f"Population mean = {pop_mean:.2f}")

    ax.set_title(f"Sampling distribution of the mean (n = {n})")
    ax.set_xlabel("Sample mean")
    ax.set_ylabel("Density")
    ax.legend(fontsize=9)

plt.tight_layout()
plt.savefig("sampling_distribution.png", dpi=150)
plt.show()
    
