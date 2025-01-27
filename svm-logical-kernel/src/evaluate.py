from sklearn.svm import SVC
from logical_kernel import logical_kernel
from data_parser import carica_dati

def valuta_svm(modello, file_test, file_training):
    """
    Valuta un modello SVM utilizzando dati di test.
    Argomenti:
        modello (SVC): Modello SVM addestrato.
        file_test (str): Percorso al file dei dati di test.
        file_training (str): Percorso al file dei dati di training (per il calcolo del kernel).
    Restituisce:
        list: Predizioni sui dati di test.
    """
    X_test = carica_dati(file_test)
    X_train = carica_dati(file_training)
    K_test = logical_kernel(X_test, X_train)
    return modello.predict(K_test)
