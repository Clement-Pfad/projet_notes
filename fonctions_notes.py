etudiants = ["Samba", "Evan", "Princia Celeste", "Noam", "Jean", "Alexandre", "Clement"]

notes = {
    "Samba": [12, 15, 14],
    "Evan": [16, 14, 17],
    "Princia Celeste": [10, 12, 11],
    "Noam": [8, 9, 10],
    "Jean": [14, 13, 15],
    "Alexandre": [18, 17, 19],
    "Clement": [9, 11, 10]
}

# 1.3. Affichage des notes de chaque etudiant a l'aide d'une boucle
print("--- 1.3. NOTES DE CHAQUE ETUDIANT ---")
for prenom in etudiants:
    print(f"{prenom} : {notes[prenom][0]}, {notes[prenom][1]}, {notes[prenom][2]}")
