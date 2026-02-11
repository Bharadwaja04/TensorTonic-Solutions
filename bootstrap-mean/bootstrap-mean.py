import numpy as np

def bootstrap_mean(x, n_bootstrap=1000, ci=0.95, rng=None):
    """
    Returns: (boot_means, lower, upper)
    """
    # Write code here
    x = np.array(x)
    
    if rng is None:
        rng = np.random.default_rng()
    
    n = len(x)


    boot_means = np.empty(n_bootstrap)
    for i in range(n_bootstrap):
        sample = rng.choice(x, size=n, replace=True)
        boot_means[i] = sample.mean()

    alpha = (1 - ci) / 2
    lower = np.quantile(boot_means, alpha)
    upper = np.quantile(boot_means, 1 - alpha)

    return (boot_means, lower, upper)
    pass
