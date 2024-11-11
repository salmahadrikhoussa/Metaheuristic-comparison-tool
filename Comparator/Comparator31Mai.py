import sys
from tkinter import *
import customtkinter
from CTkSpinbox import *
import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
from tkinter import ttk
from optimizer import run
from PIL import Image, ImageTk
from tkinter import scrolledtext
import csv
from tabulate import tabulate

# Paramètres thème et couleurs
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

# root
root = customtkinter.CTk()
root.title('Comparator')
root.attributes('-zoomed', True)

def redirect_print(output_widget):
    class StdoutRedirector:
        def __init__(self, widget):
            self.widget = widget

        def write(self, string):
            self.widget.insert(tk.END, string)
            self.widget.see(tk.END)

        def flush(self):
            pass  # Nécessaire pour les compatibilités avec certaines fonctions

    return StdoutRedirector(output_widget)

#def load_csv(file_path):
#    try:
#        # Lire le fichier CSV avec le module csv
#        with open(file_path, newline='', encoding='utf-8') as csvfile:
#            reader = csv.reader(csvfile)
#            # Convertir les lignes du CSV en chaîne de caractères
#            csv_content = "\n".join([", ".join(row) for row in reader])
#            # Effacer le contenu actuel du widget Text
#            text_widget2.delete(1.0, tk.END)
#            # Insérer le contenu du CSV dans le widget Text
#            text_widget2.insert(tk.END, csv_content)
#    except Exception as e:
#        # Afficher un message d'erreur en cas de problème
#        text_widget2.delete(1.0, tk.END)
#        text_widget2.insert(tk.END, f"Erreur lors du chargement du fichier CSV:\n{e}")

#def load_csv(file_path):
#    try:
#        # Lire le fichier CSV avec le module csv
#        with open(file_path, newline='', encoding='utf-8') as csvfile:
#            reader = csv.reader(csvfile)
#            headers = next(reader)  # Lire les en-têtes
#            rows = [row for row in reader]
#            # Utiliser tabulate pour créer un tableau formaté
#            table = tabulate(rows, headers, tablefmt='grid')
#            # Effacer le contenu actuel du widget Text
#            text_widget2.delete(1.0, tk.END)
#            # Insérer le contenu du tableau dans le widget Text
#            text_widget2.insert(tk.END, table)
#    except Exception as e:
#        # Afficher un message d'erreur en cas de problème
#        text_widget2.delete(1.0, tk.END)
#        text_widget2.insert(tk.END, f"Erreur lors du chargement du fichier CSV:\n{e}")

def load_csv(file_path):
    try:
        # Lire le fichier CSV avec le module csv
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)  # Lire les en-têtes
            # Extraire les index des colonnes à afficher
            col_indexes = [0, 1, 2, -1]  # Index des trois premières colonnes et de la dernière colonne
            # Créer une liste de lignes contenant uniquement les colonnes spécifiées
            rows = [[row[i] for i in col_indexes] for row in reader]
            # Utiliser tabulate pour créer un tableau formaté
            table = tabulate(rows, [headers[i] for i in col_indexes], tablefmt='grid')
            # Effacer le contenu actuel du widget Text
            text_widget2.delete(1.0, tk.END)
            # Insérer le contenu du tableau dans le widget Text
            text_widget2.insert(tk.END, table)
    except Exception as e:
        # Afficher un message d'erreur en cas de problème
        text_widget2.delete(1.0, tk.END)
        text_widget2.insert(tk.END, f"Erreur lors du chargement du fichier CSV:\n{e}")

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
        tab_fg_color = "#00FA9A"
        button_text_color = "white"
        button_hover_color = "#98FB98"
        label_text_color = "white"
        quitter_button_hover_color = "#FF4433"
    
    my_tab.configure(fg_color=tab_fg_color)
    
#    my_button.configure(text_color=button_text_color, hover_color=button_hover_color)
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
switch.pack(side="bottom")
def my_tab_events():
	print("Segment sélectionné:" )

# Création des Tabs
my_tab = customtkinter.CTkTabview(root, width=1600, height=800, corner_radius=20, fg_color="silver", segmented_button_fg_color="#357960", command = my_tab_events)
	
	
my_tab.pack(pady=18)

tabDebut = my_tab.add("Accueil")
tabFonctions = my_tab.add("Fonctions")
tabMethodes = my_tab.add("Algorithmes")
tabParametres = my_tab.add("Paramètres")
tabPlots = my_tab.add("Graphes")
tabResultats = my_tab.add("Résultats")

text_widget = scrolledtext.ScrolledText(tabDebut, wrap=tk.WORD, width=80, height=10)
text_widget.pack(padx=10, pady=10)
sys.stdout = redirect_print(text_widget)

text_widget2 = scrolledtext.ScrolledText(tabResultats, wrap=tk.WORD, width=80, height=20)
text_widget2.pack(padx=10, pady=10)


# Ajouter des éléments aux Tabs
#my_button = customtkinter.CTkButton(tabDebut, text="Bienvenue!", text_color="white", height=50, width=100, hover_color="#357960", #font=("Helvetica", 24), border_width=3, border_color="white", corner_radius=60)
#my_button.pack(pady=18)

my_label = customtkinter.CTkLabel(root, font=("Serif", 15), text="Votre outil de comparaison de métaheuristiques sur des problèmes d'optimisation connus.", text_color="white")
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

quitter_button5 = customtkinter.CTkButton(tabPlots, border_color="white",fg_color="red", corner_radius=60, text="Quitter ✖︎",command=quitter)
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
    finish_label = tk.Label(finish_window, text="Exécution réussie!", font=("Helvetica", 12), bg="#357960", fg="white")
    finish_label.pack(pady=90, padx=100)

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
pop_count = 10
pop_iter= 3
params = {"PopulationSize": pop_count, "Iterations": pop_iter}
results_directory= " "
image_tk = None
image_label = None

image_label = ctk.CTkLabel(tabPlots)
image_label.pack(pady=20)

# Autres paramètres
Export_avg = True
Export_details = True
Export_convergence = True
Export_boxplot = True
export_flags = {
    "Export_avg": Export_avg,
    "Export_details": Export_details,
    "Export_convergence": Export_convergence,
    "Export_boxplot": Export_boxplot,
}

def plotg (jj):
	global image_label, image_tk
	nom=results_directory+"boxplot-"+mes_fonctions[jj]+".png"
	print(nom)
	image = Image.open(nom)
	image_tk = ImageTk.PhotoImage(image)
	image_label.configure(image=image_tk)
	image_label.pack(side="right")
		
def plotc (jj):
	global image_label, image_tk
	nom=results_directory+"convergence-"+mes_fonctions[jj]+".png"
	print(nom)
	image = Image.open(nom)
	image_tk = ImageTk.PhotoImage(image)
	image_label.configure(image=image_tk)
	image_label.pack(side="right")
	

# Fonction execute
def execute():
    global NumOfRuns, params, results_directory
    print("Méthodes et fonctions: ", mes_methodes, )
    print("NumOfRuns: ", NumOfRuns)
    print("Params: ", params)
    print("Export flags: ", export_flags)
    result_button1=[]
    result_button2=[]
	
    if len(mes_methodes) * len(mes_fonctions) != 0:
        results_directory = run(mes_methodes, mes_fonctions, NumOfRuns, params, export_flags)
        finish_me()
        print("Terminé avec succès !")
        print("Repertoire: ",results_directory)
        load_csv(results_directory+"experiment.csv")
        for j in range(0, len(mes_fonctions)):
        	result_button1.append(customtkinter.CTkButton(tabPlots, border_color="white", text_color="white", font=("", 15), corner_radius=90,text="Boxplot_"+mes_fonctions[j],hover_color="light green", command= lambda  jtemp=j: plotg(jtemp)))
        	result_button1[j].pack(pady=(200, 100))
        	result_button1[j].place(relx=0.025, rely=0.2+0.1*j)
        	result_button2.append(customtkinter.CTkButton(tabPlots, border_color="white", text_color="white", font=("", 15), corner_radius=90,text="Converg_"+mes_fonctions[j],hover_color="light green", command= lambda jtemp=j: plotc(jtemp)))
        	result_button2[j].pack(pady=(200, 100))
        	result_button2[j].place(relx=0.15, rely=0.2+0.1*j)

    else:
        print("Erreur")
        error_message()

# Bouton pour lancer la comparaison
comparer_button = customtkinter.CTkButton(tabParametres, border_color="white", text_color="white", font=("", 15), corner_radius=90, text="Lancer la comparaison", hover_color="light green", command=execute)
comparer_button.pack(pady=(200, 100), side="bottom")

def print_pop(pop_count):
	global params,pop_iter
	params = {"PopulationSize": pop_count, "Iterations": pop_iter}
	print(params)
spin_pop = ctk.IntVar()
spinboxpop = CTkSpinbox(tabParametres,
          start_value = 10,
          min_value = 1,
          max_value = 100,
          scroll_value = 1,
          variable = spin_pop,
          command = print_pop)
spinboxpop.pack(expand = True)
spinboxpop.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)
labelpop = customtkinter.CTkLabel(tabParametres, font =("Arial",16), text="Taille de la population", text_color="#357960")
labelpop.place(relx=0.4, rely=0.2, anchor=customtkinter.E)

def print_iter(pop_iter):
	global params,pop_count
	params = {"PopulationSize": pop_count, "Iterations": pop_iter}
	print(params)
spin_iter = ctk.IntVar()
spinboxiter = CTkSpinbox(tabParametres,
          start_value = 3,
          min_value = 1,
          max_value = 100,
          scroll_value = 1,
          variable = spin_iter,
          command = print_iter)
spinboxiter.pack(expand = True)
spinboxiter.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)
labeliter = customtkinter.CTkLabel(tabParametres, font =("Arial",16), text="Nombre d'itérations", text_color="#357960")
labeliter.place(relx=0.4, rely=0.3, anchor=customtkinter.E)

def print_run(pop_run):
	global NumOfRuns
	NumOfRuns=pop_run
	print("Nombre de tours:",NumOfRuns)
spin_run = ctk.IntVar()
spinboxrun = CTkSpinbox(tabParametres,
          start_value = 2,
          min_value = 1,
          max_value = 100,
          scroll_value = 10,
          variable = spin_run,
          command = print_run)
spinboxrun.pack(expand = True)
spinboxrun.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)
labelrun = customtkinter.CTkLabel(tabParametres, font =("Arial",16), text="Nombre de tours", text_color="#357960")
labelrun.place(relx=0.4, rely=0.4, anchor=customtkinter.E)


root.mainloop()
