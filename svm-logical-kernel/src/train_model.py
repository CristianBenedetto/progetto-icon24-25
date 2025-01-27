from sklearn.svm import SVC
from logical_kernel import logical_kernel
from data_parser import carica_dati

def addestra_svm(file_training, etichette):
    """
    Addestra un SVM usando un kernel personalizzato.
    Argomenti:
        file_training (str): Percorso al file dei dati di training.
        etichette (list): Lista di etichette corrispondenti ai dati di training.
    Restituisce:
        SVC: Modello SVM addestrato.
    """
    X_train = carica_dati(file_training)
    K_train = logical_kernel(X_train, X_train)
    svc = SVC(kernel='precomputed')
    svc.fit(K_train, etichette)
    return svc
