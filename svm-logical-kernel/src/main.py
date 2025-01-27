from train_model import addestra_svm
from evaluate import valuta_svm
from data_parser import carica_dati
import os
import json

FILE_TRAINING = "data/train_data.json"
FILE_TEST = "data/test_data.json"
LOG_PREDIZIONI = "logs/predictions.log"
ETICHETTE = [1, 0, 1]

if __name__ == "__main__":
    if not os.path.exists("logs"):
        os.makedirs("logs")

    modello = addestra_svm(FILE_TRAINING, ETICHETTE)
    predizioni = valuta_svm(modello, FILE_TEST, FILE_TRAINING)

    with open(LOG_PREDIZIONI, "w") as log:
        log.write(json.dumps(predizioni, indent=4))

    print("Predizioni salvate in 'logs/predictions.log'.")
