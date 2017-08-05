import numpy as np

Vxf0 = {
    'L': None,
    'd': None,
    'w': 1e-4, #A positive scalar weight regulating the priority between the two objectives of the opitmization. Please refer to the page 7 of the paper for further information.
    'Mu': np.array(()),
    'P': np.array(()),
}

Options = {
    'tol_mat_bias': 1e-1,
    'display': 1,
    'tol_stopping': 1e10,
    'max_iter': 500,
    'optimizePriors': True,
    'upperBoundEigenValue': True,
}