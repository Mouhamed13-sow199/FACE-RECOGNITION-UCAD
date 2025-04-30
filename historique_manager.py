import csv
from datetime import datetime

class HistoriqueManager:
    def __init__(self, fichier="historique.csv"):
        self.fichier = fichier
        if not self._fichier_existe():
            self._creer_fichier()

    def _fichier_existe(self):
        try:
            with open(self.fichier, "r", newline='') as f:
                return True
        except FileNotFoundError:
            return False

    def _creer_fichier(self):
        with open(self.fichier, "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Nom", "Date", "Heure"])

    def ajouter_entree(self, nom):
        now = datetime.now()
        date_str = now.strftime("%Y-%m-%d")
        heure_str = now.strftime("%H:%M:%S")
        with open(self.fichier, "a", newline='') as f:
            writer = csv.writer(f)
            writer.writerow([nom, date_str, heure_str])
