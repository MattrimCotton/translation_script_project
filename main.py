from file_handler import FileHandler
from translator import TextTranslator
import tkinter as tk
from tkinter import filedialog

def main():
    # Créer une fenêtre cachée pour utiliser le sélecteur de fichier
    root = tk.Tk()
    root.withdraw()  # Cache la fenêtre principale

    # Ouvrir une boîte de dialogue pour sélectionner le fichier d'entrée
    input_file = filedialog.askopenfilename(
        title="Sélectionnez le fichier d'entrée",
        filetypes=[("Fichiers texte", "*.txt")]
    )
    
    if not input_file:
        print("Aucun fichier sélectionné. Le programme va s'arrêter.")
        return

    output_file = filedialog.asksaveasfilename(
        title="Enregistrez le fichier traduit sous",
        defaultextension=".txt",
        filetypes=[("Fichiers texte", "*.txt")]
    )

    if not output_file:
        print("Aucun fichier de sortie spécifié. Le programme va s'arrêter.")
        return

    # Créer une instance de FileHandler pour gérer les fichiers
    file_handler = FileHandler(input_file, output_file)
    
    # Lire le contenu du fichier d'entrée
    content = file_handler.read_file()

    # Vérification si le contenu est vide
    if not content:
        print("Aucun contenu lu. Assurez-vous que le fichier existe et n'est pas vide.")
        return

    # Créer une instance de TextTranslator pour traduire le texte
    translator = TextTranslator()

    # Déterminer la direction de la traduction
    language_choice = input("Traduire de l'anglais vers le français (1) ou du français vers l'anglais (2) ? (Entrez 1 ou 2): ").strip()
    if language_choice == '1':
        translated_content = translator.translate_to_french(content)
    elif language_choice == '2':
        translated_content = translator.translate_to_english(content)
    else:
        print("Choix invalide. La traduction par défaut sera de l'anglais vers le français.")
        translated_content = translator.translate_to_french(content)

    # Écrire le contenu traduit dans le fichier de sortie
    file_handler.write_file(translated_content)

    print(f"File '{input_file}' has been translated and saved to '{output_file}'.")

if __name__ == "__main__":
    main()
