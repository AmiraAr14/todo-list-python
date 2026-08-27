import json
import tkinter


# =========================
# CHARGER LES TÂCHES
# =========================

try:
    with open("tasks.json", "r") as fichier:
        tasks = json.load(fichier)
except (ValueError, FileNotFoundError):
    tasks = []


# =========================
# SAUVEGARDER
# =========================

def sauvegarder_taches():
    with open("tasks.json", "w") as fichier:
        json.dump(tasks, fichier, indent=4)


# =========================
# AFFICHER LES TÂCHES
# =========================

def afficher_taches():
    liste.delete(0, tkinter.END)

    for index, task in enumerate(tasks, 1):
        if task["terminee"]:
            symbole = "✅"
        else:
            symbole = "❌"

        liste.insert(
            tkinter.END,
            f"{index}. {task['texte']} {symbole}"
        )


# =========================
# AJOUTER
# =========================

def ajouter():
    texte = champ.get().strip()

    if texte:
        task = {
            "texte": texte,
            "terminee": False
        }

        tasks.append(task)

        sauvegarder_taches()
        afficher_taches()

        champ.delete(0, tkinter.END)


# =========================
# SUPPRIMER
# =========================

def supprimer():
    selection = liste.curselection()

    if selection:
        index = selection[0]

        tasks.pop(index)

        sauvegarder_taches()
        afficher_taches()


# =========================
# MODIFIER
# =========================

def modifier():
    selection = liste.curselection()

    if selection:
        index = selection[0]

        texte = tasks[index]["texte"]

        champ.delete(0, tkinter.END)
        champ.insert(0, texte)


# =========================
# ENREGISTRER MODIFICATION
# =========================

def enregistrer_modification():
    selection = liste.curselection()

    if selection:
        index = selection[0]
        nouveau_texte = champ.get().strip()

        if nouveau_texte:
            tasks[index]["texte"] = nouveau_texte

            sauvegarder_taches()
            afficher_taches()

            champ.delete(0, tkinter.END)


# =========================
# TERMINER
# =========================

def terminer():
    selection = liste.curselection()

    if selection:
        index = selection[0]

        tasks[index]["terminee"] = True

        sauvegarder_taches()
        afficher_taches()


# =========================
# FENÊTRE
# =========================

fenetre = tkinter.Tk()

fenetre.title("Ma To-Do List")
fenetre.geometry("600x700")
fenetre.configure(bg="#dbeafe")


# =========================
# CONTENEUR
# =========================

conteneur = tkinter.Frame(
    fenetre,
    bg="#dbeafe"
)

conteneur.pack(
    fill="both",
    expand=True,
    padx=30,
    pady=25
)


# =========================
# TITRE
# =========================

titre = tkinter.Label(
    conteneur,
    text="MA TO-DO LIST",
    font=("Arial", 26, "bold"),
    bg="#dbeafe"
)

titre.pack(pady=(0, 5))


sous_titre = tkinter.Label(
    conteneur,
    text="Organise tes tâches simplement",
    font=("Arial", 11),
    bg="#dbeafe"
)

sous_titre.pack(pady=(0, 20))


# =========================
# CHAMP
# =========================

champ = tkinter.Entry(
    conteneur,
    font=("Arial", 13),
    width=40
)

champ.pack(
    ipady=8,
    pady=(0, 10)
)


# =========================
# BOUTON AJOUTER
# =========================

bouton_ajouter = tkinter.Button(
    conteneur,
    text="＋ Ajouter",
    font=("Arial", 11, "bold"),
    command=ajouter,
    padx=15,
    pady=6
)

bouton_ajouter.pack(pady=(0, 20))


# =========================
# LISTE
# =========================

liste = tkinter.Listbox(
    conteneur,
    font=("Arial", 12),
    width=50,
    height=12,
    selectmode=tkinter.SINGLE
)

liste.pack(
    fill="both",
    expand=True,
    pady=(0, 15)
)


# =========================
# CADRE DES BOUTONS
# =========================

cadre_boutons = tkinter.Frame(
    conteneur,
    bg="#dbeafe"
)

cadre_boutons.pack(pady=5)


# =========================
# BOUTON MODIFIER
# =========================

bouton_modifier = tkinter.Button(
    cadre_boutons,
    text="Modifier",
    command=modifier,
    width=15,
    pady=5
)

bouton_modifier.grid(
    row=0,
    column=0,
    padx=5,
    pady=5
)


# =========================
# BOUTON ENREGISTRER
# =========================

bouton_enregistrer = tkinter.Button(
    cadre_boutons,
    text="Enregistrer",
    command=enregistrer_modification,
    width=15,
    pady=5
)

bouton_enregistrer.grid(
    row=0,
    column=1,
    padx=5,
    pady=5
)


# =========================
# BOUTON SUPPRIMER
# =========================

bouton_supprimer = tkinter.Button(
    cadre_boutons,
    text="Supprimer",
    command=supprimer,
    width=15,
    pady=5
)

bouton_supprimer.grid(
    row=1,
    column=0,
    padx=5,
    pady=5
)


# =========================
# BOUTON TERMINER
# =========================

bouton_terminer = tkinter.Button(
    cadre_boutons,
    text="✓ Terminer",
    command=terminer,
    width=15,
    pady=5
)

bouton_terminer.grid(
    row=1,
    column=1,
    padx=5,
    pady=5
)


# =========================
# AFFICHER LES TÂCHES
# =========================

afficher_taches()


# =========================
# LANCER L'APPLICATION
# =========================

fenetre.mainloop()