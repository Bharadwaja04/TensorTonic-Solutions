import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here

    expected_value = 0
    if sum(p) == 1 and len(x) == len(p):
        for i in range(len(x)):
            expected_value+=(x[i]*p[i])
        return expected_value
    raise ValueError("Got a value error")
    pass
