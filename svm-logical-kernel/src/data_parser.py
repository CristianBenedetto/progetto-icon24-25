import json

def carica_dati(percorso_file):
    """
    Carica dati logici da un file JSON.
    Argomenti:
        percorso_file (str): Percorso del file JSON contenente rappresentazioni logiche.
    Restituisce:
        list: Una lista di rappresentazioni logiche (insiemi di fatti).
    """
    with open(percorso_file, 'r') as f:
        dati = json.load(f)
    return [set(item) for item in dati]
