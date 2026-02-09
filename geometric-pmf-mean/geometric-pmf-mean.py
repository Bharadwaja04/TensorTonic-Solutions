import numpy as np

def geometric_pmf_mean(k, p):
    """
    Compute Geometric PMF and Mean.
    """
    # Write code here
    pmf = []
    for i in range(len(k)):
        pmf.append(((1-p)**(k[i]-1))*p)

    pmf_arr = np.array(pmf)
    mean = 1/p
    return (pmf_arr,mean)
    pass