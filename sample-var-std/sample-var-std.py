import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    # Write code here
    x = np.array(x)
    mean = np.mean(x)
    dev = 0
    for i in range(len(x)):
        dev+=((x[i] - mean)**2)
    var = dev/(len(x) - 1)
    return (var,var**0.5)
    pass