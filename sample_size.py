# Load libraries
from statsmodels.stats.power import TTestIndPower

# Set parameters
alpha = 0.05     # significance level
power = 0.8      # power
effect_size = 0.5  # effect size
pop_size = None  # population size (set to None if unknown)
ratio = 1        # ratio of sample sizes for two-sample test

# Create power analysis object
analysis = TTestIndPower()

# Calculate sample size
n = analysis.solve_power(effect_size=effect_size, alpha=alpha, power=power, 
                         nobs1=None, ratio=ratio, 
                         alternative='two-sided', 
                         return_type='samples')

# Print sample size
print("Sample size required:", round(n,0))
