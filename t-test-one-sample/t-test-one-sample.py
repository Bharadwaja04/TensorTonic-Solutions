import numpy as np

def t_test_one_sample(x, mu0):
    """
    Compute one-sample t-statistic.
    """
    # Write code here
    x = np.array(x)
    x_mean = np.mean(x)
    s = np.sqrt(np.var(x,ddof=1))

    n = len(x)

    t_stat = (x_mean - mu0)/(s/(np.sqrt(n)))
    return t_stat
    pass