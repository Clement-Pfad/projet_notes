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



# 2.1. Fonction pour calculer la moyenne d'une liste de notes
def moyenne(liste_notes):
    """Calcule et retourne la moyenne arithmétique d'une liste de notes."""
    if len(liste_notes) == 0:
        return 0
    return sum(liste_notes) / len(liste_notes)


# 2.3. Fonction pour attribuer une mention selon la moyenne
def mention(moy):
    """Retourne la mention correspondante en fonction de la moyenne."""
    if moy >= 16:
        return "Excellent"
    elif moy >= 14:
        return "Bien"
    elif moy >= 12:
        return "Assez bien"
    elif moy >= 10:
        return "Passable"
    else:
        return "Insuffisant"


# 2.2 & 2.3. Affichage des résultats individuels et mentions
print("2.2 & 2.3. RÉSULTATS INDIVIDUELS ET MENTIONS")
for prenom in etudiants:
    moy_etudiant = moyenne(notes[prenom])
    ment = mention(moy_etudiant)
    print(f"{prenom} — Notes : {notes[prenom][0]}, {notes[prenom][1]}, {notes[prenom][2]} — Moyenne : {moy_etudiant:.2f} — Mention : {ment}")
print("\n" + "\n")


# 2.4. Fonction pour trouver le meilleur étudiant
def meilleur_etudiant(dico_notes):
    """Parcourt le dictionnaire pour trouver l'étudiant avec la meilleure moyenne."""
    meilleur_nom = ""
    meilleure_moy = -1
    
    for prenom, liste_n in dico_notes.items():
        moy = moyenne(liste_n)
        if moy > meilleure_moy:
            meilleure_moy = moy
            meilleur_nom = prenom
            
    return meilleur_nom, meilleure_moy

nom_top, moy_top = meilleur_etudiant(notes)
print("2.4. LE MEILLEUR ÉTUDIANT")
print(f"Le meilleur étudiant est {nom_top} avec une moyenne de {moy_top:.2f}.")
print("\n" + "\n")