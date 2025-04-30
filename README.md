# FACE-RECOGNITION-UCAD

📷 Système de Reconnaissance Faciale pour la Gestion des Étudiants - UCAD
Ce projet consiste en une application Tkinter utilisant OpenCV et face_recognition pour permettre l’enregistrement des étudiants et leur reconnaissance faciale. 
Il est destiné à renforcer la sécurité et à suivre les entrées dans un environnement académique (ex: examens, accès aux salles, etc.).

🧰 Fonctionnalités
📸 Enregistrement des étudiants avec capture photo via webcam

🧑‍🎓 Stockage local des visages dans un dossier dédié (face-detect)

🤖 Reconnaissance faciale en temps réel avec affichage du nom

📊 Historique des reconnaissances sauvegardé dans un fichier CSV (historique.csv)

📂 Interface utilisateur moderne et intuitive avec Tkinter

🔍 Affichage de l’historique des entrées dans une fenêtre dédiée

📦 Structure du Projet

.
├── face-detect/             # Dossier où les images des étudiants sont stockées
├── historique.csv           # Historique des reconnaissances
├── logo_ucad.JPEG           # Logo UCAD affiché dans les interfaces
├── historique_manager.py    # Module pour gérer l’historique
├── enregistrement.py        # Interface d’ajout d’étudiants
├── reconnaissance.py        # Interface de reconnaissance faciale
└── README.md
🖥️ Prérequis
Assure-toi d'avoir les bibliothèques suivantes installées :


pip install opencv-python
pip install face_recognition
pip install Pillow
Remarque : face_recognition nécessite dlib. Si tu rencontres des erreurs lors de l’installation, consulte la documentation officielle.

🚀 Lancer l’application
🎓 Enregistrer un étudiant

python enregistrement.py
Remplis les champs (Numéro étudiant, prénom, nom)

Appuie sur S pour capturer l'image via webcam

L'image sera sauvegardée dans face-detect/

🧠 Lancer la reconnaissance

python reconnaissance.py
Appuie sur Q pour quitter la reconnaissance

Appuie sur "Consulter l'historique" pour voir les entrées détectées

📑 Fichier historique.csv
Ce fichier contient les entrées suivantes :


Nom complet	Date	Heure
1234_Mamadou_Diop	2025-04-30	10:15:45
5678_Awa_Ndiaye	2025-04-30	10:16:07
🛡️ Sécurité et Confidentialité
Les données faciales sont stockées localement et ne sont pas partagées en ligne. Il est recommandé de :

Protéger le dossier face-detect

Ne pas diffuser historique.csv sans anonymisation

👨‍💻 Auteur
Mouhamed Sow
Étudiant en Master 2 Business Intelligence
Université Cheikh Anta Diop de Dakar (UCAD)

Encadreur : Dr Modou Gueye

📃 Licence
Ce projet est open-source et peut être adapté librement à des fins académiques.
