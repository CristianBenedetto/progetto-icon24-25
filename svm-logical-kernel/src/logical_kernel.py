import numpy as np

def logical_kernel(X, Y):
    """
    Funzione kernel personalizzata per rappresentazioni logiche.
    X, Y: Array di rappresentazioni logiche (es. fatti in Datalog).
    """
    def similarita(x, y):
        return len(set(x) & set(y))

    matrice_kernel = np.zeros((len(X), len(Y)))
    for i, x in enumerate(X):
        for j, y in enumerate(Y):
            matrice_kernel[i, j] = similarita(x, y)

    return matrice_kernel
