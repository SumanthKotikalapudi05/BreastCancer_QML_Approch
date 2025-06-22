from qiskit.algorithms.optimizers import COBYLA, SPSA

def get_op(name='COBYLA'):
    if name=='COBYLA':
        return COBYLA(maxiter=100)
    elif name=='SPSA':
        return SPSA(maxiter=100)
    else:
        raise ValueError("Invalid optimizer name. Please choose from 'COBYLA' or 'SPSA'")
    