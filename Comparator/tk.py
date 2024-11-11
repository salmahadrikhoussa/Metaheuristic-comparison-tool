from tkinter import *
import customtkinter
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from optimizer import run
import csv
import glob
from datetime import datetime
import os



# Paramètres thème et couleurs
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

# root
root = customtkinter.CTk()
root.title('Comparator')
root.attributes('-zoomed', True)


















def combobox_callback(choice):
    print("ComboBox dropdown clicked:", choice)


# Fonction pour basculer entre les modes clair et sombre
def switch_event():
    if switch_var.get() == "on":
        customtkinter.set_appearance_mode("dark")
        update_colors("dark")
    else:
        customtkinter.set_appearance_mode("light")
        update_colors("light")
    print("switch toggled, current value:", switch_var.get())

# Fonction pour mettre à jour les couleurs des widgets
def update_colors(mode):
    if mode == "dark":
        tab_fg_color = "#C8E6C9"
        button_text_color = "white"
        button_hover_color = "#357960"
        label_text_color = "black"
        quitter_button_hover_color = "#E60023"
    else:
        tab_fg_color = "#A5D6A7"
        button_text_color = "white"
        button_hover_color = "#98FB98"
        label_text_color = "#455A64"
        quitter_button_hover_color = "#FF4433"
    
    my_tab.configure(fg_color=tab_fg_color)
    
    my_button.configure(text_color=button_text_color, hover_color=button_hover_color)
    my_label.configure(text_color=label_text_color)
    quitter_button.configure(hover_color=quitter_button_hover_color)

# Ajout de l'interrupteur personnalisé pour changer le mode
switch_var = customtkinter.StringVar(value="on")
switch = customtkinter.CTkSwitch(root,
                                 text="Changer le mode",
                                 command=switch_event,
                                 variable=switch_var,
                                 onvalue="on",
                                 offvalue="off",
                                 width=80,
                                 height=50,
                                 switch_width=50,
                                 switch_height=25,
                                 corner_radius=20,
                                 border_width=2,
                                 fg_color=("lightgray", "gray"),
                                 border_color=("white", "white"),
                                 progress_color=("blue", "white"),
                                 button_color=("white", "grey"),
                                 button_hover_color=("white", "grey"),
                                 text_color=("black", "white"),
                                 font=("Arial", 10))
switch.pack(pady=20)
def my_tab_events():
	print("Segment sélectionné:" )

# Création des Tabs
my_tab = customtkinter.CTkTabview(root, width=1500, height=500, corner_radius=20, fg_color="silver", segmented_button_fg_color="#357960", command = my_tab_events)


	
	
my_tab.pack(pady=18)

tabDebut = my_tab.add("Commandes")
tabFonctions = my_tab.add("Fonctions")
tabMethodes = my_tab.add("Algorithmes")
tabParametres = my_tab.add("Paramètres")
tabCommandes = my_tab.add("Résultats")















# Ajouter des éléments aux Tabs
my_button = customtkinter.CTkButton(tabDebut, text="Bienvenue!", text_color="white", height=50, width=100, hover_color="#357960", font=("Helvetica", 24), border_width=3, border_color="white", corner_radius=60)
my_button.pack(pady=18)

my_label = customtkinter.CTkLabel(tabDebut, font=("Serif", 15), text="Votre outil de comparaison de métaheuristiques sur des problèmes d'optimisation connus.", text_color="#357960")
my_label.pack(pady=30)

# Bouton "Quitter"
def quitter():
    quitter_button.quit()
    
quitter_button = customtkinter.CTkButton(tabDebut, border_color="white", fg_color="red", corner_radius=60, text="Quitter ✖︎", command=quitter)
quitter_button.pack(pady=(0, 10), side=BOTTOM)

    
quitter_button2 = customtkinter.CTkButton(tabFonctions, border_color="white",fg_color="red", corner_radius=60, text="Quitter ✖︎",command=quitter)
quitter_button2.grid(row=99, column=1, pady=10, padx=10, sticky="s")


quitter_button3 = customtkinter.CTkButton(tabMethodes, border_color="white",fg_color="red", corner_radius=60, text="Quitter ✖︎",command=quitter)
quitter_button3.grid(row=99, column=2, pady=20, padx=10, sticky="s")

quitter_button4 = customtkinter.CTkButton(tabParametres, border_color="white",fg_color="red", corner_radius=60, text="Quitter ✖︎",command=quitter)
quitter_button4.pack(pady=(0, 10), side=BOTTOM)

quitter_button5 = customtkinter.CTkButton(tabCommandes, border_color="white",fg_color="red", corner_radius=60, text="Quitter ✖︎",command=quitter)
quitter_button5.pack(pady=(0, 10), side=BOTTOM)

# Mise à jour initiale des couleurs
update_colors("dark")

	
# Ajout des fonctions dans tabFonctions
functions = [
    "F1: Σᵢ₌₁ⁿ xᵢ²",
    "F2: Σᵢ₌₁ⁿ |xᵢ| + Πᵢ₌₁ⁿ |xᵢ|",
    "F3: Σᵢ₌₁ᵈⁱᵐ (Σⱼ₌₁ⁱ xⱼ)²",
    "F4: max(|x|)",
    "F5: Σᵢ₌₂ᵈⁱᵐ [100(xᵢ - xᵢ₋₁²)² + (xᵢ₋₁ - 1)²]",
    "F6: Σ |x + 0.5|²",
    "F7: Σᵢ₌₁ᵈⁱᵐ ixᵢ⁴ + Uniform(0,1)",
    "F8: Σ -xᵢ sin(√(|xᵢ|))",
    "F9: Σ [xᵢ² - 10cos(2πxᵢ)] + 10dim",
    "F10: -20exp(-0.2√(Σxᵢ²/dim)) - exp(Σcos(2πxᵢ)/dim) + 20 + exp(1)",
    "F11: (Σxᵢ²/4000) - Πcos(xᵢ/√i) + 1",
    "F12: (π/dim) [10(sin(π(1+(x₁+1)/4))² + Σᵢ₌₁ᵈⁱᵐ [(xᵢ+1)/4]²",
    "F13: 0.1 [sin(3πx₁)² + Σᵢ₌₁ᵈⁱᵐ (xᵢ - 1)² (1 + sin²(3πxᵢ₊₁))",
    "F14: ((1/500) + Σ(1/(i + Σ(xⱼ - aᵢⱼ)⁶)))⁻¹",
    "F15: Σ[aᵢ - (L₁(bᵢ² + L₂bᵢ)/(bᵢ² + L₃bᵢ + L₄))]²",
    "F16: 4L₁² - 2.1L₁⁴ + L₁⁶/3 + L₁L₂ - 4L₂² + 4L₂⁴",
    "F17: (L₂ - (L₁²) * 5.1 / (4π²) + 5 / π * L₁ - 6)² + 10 (1 - 1/(8π))cos(L₁) + 10",
    "F18: [1 + (L₁ + L₂ + 1)² * (19 - 14L₁ + 3L₁² - 14L₂ + 6L₁L₂",
    "F19: Σ [-c1ᵢ exp(-(Σ(aᵢⱼ(L - pᵢⱼ)²)))]",
    "F20: Σ [-c2ᵢ exp(-(Σ(aᵢⱼ(L - pᵢⱼ)²)))]",
    "F21: Σ[-1/((L - a1ᵢ)ᵀ(L - aᵢ) + cᵢ)]",
    "F22: Σ[-1/((L - a2ᵢ)ᵀ(L - aᵢ) + cᵢ)]",
    "F23: Σ[-1/((L - a3ᵢ)ᵀ(L - aᵢ) + cᵢ)]"
]

Allfunctions = ["F1","F2","F3","F4","F5","F6","F7","F8","F9","F10","F11","F12","F13","F14","F15","F16","F17","F18","F19","F20","F21","F22","F23"]
 
my_check = []
variables = [] 

# Fonction pour afficher l'état des checkboxes
def print_states():
    global mes_fonctions
    mes_fonctions = []
    for i, var in enumerate(variables):
    	if var.get():  # Correction de l'indentation ici
            mes_fonctions.append(Allfunctions[i])
            print(Allfunctions[i],f": {'Checked' if var.get() else 'Unchecked'}")
    print(mes_fonctions)



num_columns = 3  # Number of columns for the grid
for i,function in enumerate(functions):
	var = customtkinter.BooleanVar()
	my_check = customtkinter.CTkCheckBox(tabFonctions, text=function, variable=var,text_color="black", command=print_states)
	my_check.grid(row=i // num_columns, column=i % num_columns, padx=10, pady=10, sticky="w",)
	variables.append(var) 








# Ajout de méthodes dans tabMethodes
methods=["Essaim de salpes (SSA)","Essaim particules (PSO)", "Algorithme génétique (GA)", "Chauve-souris (BAT)", "Lucioles (FFA)", "Loup gris (GWO)", "Baleine (WOA)", "Multi-Verse Optimiseur (MVO)", " Flamme des papillons (MFO)", "Recherche du coucou (CS)", "Faucon-pèlerin (HHO)", "Chenille spirale (SCA)", "Meilleure amélioration(JAYA)", "Différenciation évolutionnaire DE"]

Allmethods=["SSA","PSO","GA","BAT","FFA","GWO","WOA","MVO","MFO","CS","HHO","SCA","JAYA","DE"]
my_check2 = []
variables2 = []
mes_methodes =[]
mes_fonctions =[]
# Fonction pour afficher l'état des checkboxes
def print_states():
    global mes_methodes 
    mes_methodes = []
    for i, var in enumerate(variables2): 
        if var.get():  # Correction de l'indentation ici
            mes_methodes.append(Allmethods[i])
    print(len(mes_methodes))
#        print(Allfunctions[i],f": {'Checked' if var.get() else 'Unchecked'}")


num_columns = 4  # Number of columns for the grid
for i,method in enumerate(methods):
	var = customtkinter.BooleanVar()
	my_check2 = customtkinter.CTkCheckBox(tabMethodes, text=method, variable=var,text_color="black", command=print_states)
	my_check2.grid(row=i // num_columns, column=i % num_columns, padx=30, pady=30, sticky="w",)
	variables2.append(var) 
    
 # Function to close the help window
def close_help_window(window):
    window.destroy()

# Function to display custom help message
def help_me():
    # Create a custom Tkinter window for displaying the help message
    help_window = tk.Toplevel()
    help_window.title("Aide ⓘ")

    # Customize the appearance of the help window
    help_window.configure(bg="#357960")  # Set background color

    # Add a label with the help message
    help_label = tk.Label(help_window, text="Voici les étapes à suivre :\n\n1 : Choisissez une ou plusieurs fonctions selon vos besoins. \n\n2 : Sélectionnez les méthodes souhaitées pour votre analyse.\n\n3 : Cliquez sur Exécuter pour lancer vos tests.", font=("Helvetica", 12), bg="#357960", fg="white")
    help_label.pack(pady=20, padx=20)

    # Add an "OK" button to close the help window
    ok_button = ttk.Button(help_window, text="Ok", command=lambda: close_help_window(help_window))
    ok_button.pack(pady=10)

    # Adjust window size to fit content
    help_window.geometry(f"+{help_window.winfo_screenwidth() // 2 - 200}+{help_window.winfo_screenheight() // 2 - 100}")

help_button = customtkinter.CTkButton(tabDebut, text="Aide ?", command=help_me, corner_radius=60)
help_button.pack(pady=100)

#BOUTON J'AI FINI
def finish_me():
    # Create a custom Tkinter window for displaying the help message
    finish_window = tk.Toplevel()
    finish_window.title("ⓘ")

    # Customize the appearance of the finish window
    finish_window.configure(bg="#357960")  # Set background color

    # Add a label with the help message
    finish_label = tk.Label(finish_window, text="Exécution réussie! consulter le répertoir /Comparator", font=("Sérif", 12), bg="#357960", fg="white")
    finish_label.pack(pady=20, padx=20)

    # Add an "OK" button to close the finish window
    ok_button = ttk.Button(finish_window, text="Ok", command=lambda: close_help_window(finish_window))
    ok_button.pack(pady=10)




# Fonction pour afficher le message d'erreur personnalisé
def error_message():
    error_window = tk.Toplevel()
    error_window.title("Erreur ⚠︎")
    error_window.configure(bg="#FFD700")
    
    error_label = tk.Label(error_window, text="Une erreur est survenue. Veuillez vérifier vos sélections et réessayer.", font=("Arial", 12), bg="#FFD700", fg="black")
    error_label.pack(pady=20, padx=20)
    
    ok_button = ttk.Button(error_window, text="Ok!", command=error_window.destroy)
    ok_button.pack(pady=10)
    
    error_window.geometry(f"+{error_window.winfo_screenwidth() // 2 - 200}+{error_window.winfo_screenheight() // 2 - 100}")


# Variables globales pour stocker les valeurs
NumOfRuns = 2
params = {"PopulationSize": 30, "Iterations": 3}

# Fonction pour récupérer les valeurs saisies par l'utilisateur
def get_values():
    global NumOfRuns, params
    NumOfRuns = int(name_entry3.get())
    params["PopulationSize"] = int(name_entry.get())
    params["Iterations"] = int(name_entry2.get())
    print("Valeurs mises à jour:", NumOfRuns, params)

# Ajout des labels et des entrées avec des valeurs numériques
label1 = customtkinter.CTkLabel(tabParametres, text="Taille de la population", text_color="#357960")
label1.place(relx=0.4, rely=0.2, anchor=customtkinter.CENTER)
name_entry = customtkinter.CTkEntry(tabParametres, width=150, height=30, border_width=2, corner_radius=10)
name_entry.place(relx=0.6, rely=0.2, anchor=customtkinter.CENTER)

label2 = customtkinter.CTkLabel(tabParametres, text="Nombre d'itérations", text_color="#357960")
label2.place(relx=0.4, rely=0.3, anchor=customtkinter.CENTER)
name_entry2 = customtkinter.CTkEntry(tabParametres, width=150, height=30, border_width=2, corner_radius=10)
name_entry2.place(relx=0.6, rely=0.3, anchor=customtkinter.CENTER)

label3 = customtkinter.CTkLabel(tabParametres, text="Nombre de tours", text_color="#357960")
label3.place(relx=0.4, rely=0.4, anchor=customtkinter.CENTER)
name_entry3 = customtkinter.CTkEntry(tabParametres, width=150, height=30, border_width=2, corner_radius=10)
name_entry3.place(relx=0.6, rely=0.4, anchor=customtkinter.CENTER)

# Bouton "OK" pour récupérer les valeurs
ok_button = customtkinter.CTkButton(tabParametres, text="OK", command=get_values)
ok_button.place(relx=0.6, rely=0.5, anchor=customtkinter.CENTER)

# Autres paramètres
export_flags = {
    "Export_avg": True,
    "Export_details": True,
    "Export_convergence": True,
    "Export_boxplot": True,
}

# Fonction execute
def execute():
    global NumOfRuns, params
    print("Méthodes et fonctions: ", mes_methodes, mes_fonctions)
    print("NumOfRuns: ", NumOfRuns)
    print("Params: ", params)
    print("Export flags: ", export_flags)
    if len(mes_methodes) * len(mes_fonctions) != 0:
        run(mes_methodes, mes_fonctions, NumOfRuns, params, export_flags)
        finish_me()
        print("Terminé avec succès !")
    else:
        print("Erreur")
        error_message()

# Bouton pour lancer la comparaison
comparer_button = customtkinter.CTkButton(tabParametres, border_color="white", text_color="white", font=("", 15), corner_radius=90, text="Lancer la comparaison", hover_color="light green", command=execute)
comparer_button.pack(pady=(200, 100), side="bottom")


def find_latest_csv(directory):
    # Trouver tous les fichiers CSV dans le répertoire spécifié
    list_of_files = glob.glob(os.path.join(directory, "*.csv"))
    if not list_of_files:
        raise FileNotFoundError("Aucun fichier CSV trouvé dans le répertoire spécifié.")
    
    # Trouver le fichier le plus récent en se basant sur la date de modification
    latest_file = max(list_of_files, key=os.path.getmtime)
    return latest_file

def load_csv_data(filename):
    with open(filename, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader)  # Skip the header row
        data = [row for row in csvreader]
    return data

# Chemin vers le répertoire où sont stockés les fichiers CSV et PNG
csv_directory = '/home/selma/Bureau/pfe/Comparator'

# Localisation du fichier CSV le plus récent
try:
    latest_csv = find_latest_csv(csv_directory)
    print("Chemin du fichier CSV le plus récent :", latest_csv)
except FileNotFoundError as e:
    print(e)
    exit()

# Chargement des données à partir du fichier CSV le plus récent
data = load_csv_data(latest_csv)
print("Données du fichier CSV le plus récent :", data)


# Localisation du fichier CSV le plus récent
try:
    latest_csv = find_latest_csv(csv_directory)
    print("Chemin du fichier CSV le plus récent :", latest_csv)
except FileNotFoundError as e:
    print(e)
    exit()

# Chargement des données à partir du fichier CSV le plus récent
data = load_csv_data(latest_csv)
print("Données du fichier CSV le plus récent :", data)








# Définition des colonnes pour les deux tableaux
result_columns1 = ("Méthode", "Fonction", "Temps CPU")
result_columns2 = ("Méthode", "Fonction", "Coût", "Erreur Minimale")

# Création des tableaux
tree_result1 = ttk.Treeview(tabCommandes, columns=result_columns1, show='headings')
tree_result2 = ttk.Treeview(tabCommandes, columns=result_columns2, show='headings')

# Définition des en-têtes des colonnes pour le premier tableau
for col in result_columns1:
    tree_result1.heading(col, text=col)
    tree_result1.column(col, minwidth=0, width=100)

# Définition des en-têtes des colonnes pour le second tableau
for col in result_columns2:
    tree_result2.heading(col, text=col)
    tree_result2.column(col, minwidth=0, width=100)

# Positionnement des tableaux dans l'onglet "Résultats"
tree_result1.pack(side="top", fill="both", expand=True, padx=10, pady=10)
tree_result2.pack(side="top", fill="both", expand=True, padx=10, pady=10)
# Définition des colonnes pour le tableau
result_columns = ("Optimizer", "objfname", "ExecutionTime", "Iter")

# Création du tableau
tree_result = ttk.Treeview(tabCommandes, columns=result_columns, show='headings')

# Définition des en-têtes des colonnes
for col in result_columns:
    tree_result.heading(col, text=col)
    tree_result.column(col, minwidth=0, width=100)

# Positionnement du tableau dans l'onglet "Résultats"
tree_result.pack(side="top", fill="both", expand=True, padx=10, pady=10)

# Insertion des données dans le tableau
for row in data:
    tree_result.insert("", tk.END, values=row)

root.mainloop()
