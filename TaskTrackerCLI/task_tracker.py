import json
import os

# Affiche le menu principal
def afficher_menu():
    print("Bienvenue dans le Task Tracker CLI!")
    print("1. Ajouter une tâche")
    print("2. Lister les tâches")
    print("3. Marquer une tâche")
    print("4. Quitter")

# Fonction pour ajouter une tâche
def ajouter_tache():
    titre = input("Entrez le titre de la tâche : ")
    description = input("Entrez la description de la tâche : ")
    tache = {
        "titre": titre,
        "description": description,
        "status": "à faire"
    }

    # Vérification du fichier JSON avant d'ajouter
    if not os.path.exists("taches.json"):
        with open("taches.json", "w") as fichier:
            json.dump([], fichier)

    # Ajout de la tâche
    with open("taches.json", "r") as fichier:
        taches = json.load(fichier)
    taches.append(tache)

    with open("taches.json", "w") as fichier:
        json.dump(taches, fichier, indent=4)
    
    print("Tâche ajoutée avec succès!")

# Fonction pour lister les tâches
def lister_taches():
    if not os.path.exists("taches.json"):
        print("Aucune tâche à afficher.")
        return

    with open("taches.json", "r") as fichier:
        taches = json.load(fichier)

    if not taches:
        print("Aucune tâche à afficher.")
    else:
        for index, tache in enumerate(taches):
            print(f"{index}. {tache['titre']} - {tache['status']}")

# Fonction pour marquer une tâche
def marquer_tache():
    tache_id = int(input("Entrez l'ID de la tâche à modifier : "))
    with open("taches.json", "r") as fichier:
        taches = json.load(fichier)
    
    if tache_id < 0 or tache_id >= len(taches):
        print("ID de tâche invalide.")
        return

    tache = taches[tache_id]
    tache['status'] = input("Entrez le nouveau statut (à faire/en cours/terminée) : ")

    with open("taches.json", "w") as fichier:
        json.dump(taches, fichier, indent=4)
    
    print("Tâche mise à jour avec succès!")

# Fonction principale pour gérer les options
def main():
    while True:
        afficher_menu()
        choix = input("Choisissez une option (1/2/3/4) : ")
        if choix == '1':
            ajouter_tache()
        elif choix == '2':
            lister_taches()
        elif choix == '3':
            marquer_tache()
        elif choix == '4':
            print("Merci d'avoir utilisé Task Tracker!")
            break
        else:
            print("Option invalide, veuillez essayer à nouveau.")

if __name__ == "__main__":
    main()
