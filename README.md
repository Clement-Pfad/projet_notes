def creer_readme():
    contenu_readme = """# 📊 Gestionnaire de Notes et Analyse de Classe

Un script en Python simple et modulaire permettant de gérer les notes d'étudiants, de calculer des moyennes, d'attribuer des mentions, d'analyser les performances globales d'une classe et de sauvegarder les résultats dans un fichier texte.

---

## 🛠️ Fonctionnalités du Programme

1. **Enregistrement et Affichage :** Stockage des notes individuelles dans un dictionnaire et affichage formaté pour chaque étudiant.
2. **Calculs et Mentions :** 
   - Calcul automatique de la moyenne arithmétique.
   - Attribution d'une mention selon le barème (Excellent, Bien, Assez bien, Passable, Insuffisant).
   - Identification du meilleur étudiant de la classe.
3. **Analyse Globale :** 
   - Calcul de la moyenne générale de la classe.
   - Comptage des étudiants ayant validé (moyenne $\\ge 10$) ou non.
   - Répartition complète des mentions.
4. **Exportation des Données :** Enregistrement de tous les bilans individuels et globaux dans un fichier texte (`resultats.txt`).
5. **Recherche Intelligente :** Fonction de recherche insensible à la casse pour retrouver rapidement les informations d'un étudiant.

---

## 🚀 Utilisation

1. Assurez-vous d'avoir **Python** installé sur votre machine.
2. Téléchargez ou copiez le script principal (ex: `gestion_notes.py`).
3. Exécutez le script dans votre terminal :
   ```bash
   python gestion_notes.py
