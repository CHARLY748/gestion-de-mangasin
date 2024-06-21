from datetime import datetime, timedelta
import sqlite3
from tkinter import messagebox,ttk

class caisse:
    # ... (votre code existant)

    def nombre_ventes_par_jour(self, date_vente):
        conn = sqlite3.connect(database=r"C:\Users\USER\Desktop\mon_deuxieme_project\donnee\magasinbase.bd")
        curseur = conn.cursor()
        try:
            curseur.execute("SELECT COUNT(*) FROM nom_de_votre_table WHERE date_vente = ?", (date_vente,))
            nombre_ventes = curseur.fetchone()[0]
            conn.commit()
            return nombre_ventes
        except Exception as error:
            messagebox.showerror("Erreur", f"Erreur de connexion: {str(error)}")
        finally:
            conn.close()

    def nombre_ventes_par_semaine(self, date_debut_semaine):
        conn = sqlite3.connect(database=r"C:\Users\USER\Desktop\mon_deuxieme_project\donnee\magasinbase.bd")
        curseur = conn.cursor()
        try:
            date_fin_semaine = date_debut_semaine + timedelta(days=6)
            curseur.execute("SELECT COUNT(*) FROM nom_de_votre_table WHERE date_vente BETWEEN ? AND ?", (date_debut_semaine, date_fin_semaine))
            nombre_ventes = curseur.fetchone()[0]
            conn.commit()
            return nombre_ventes
        except Exception as error:
            messagebox.showerror("Erreur", f"Erreur de connexion: {str(error)}")
        finally:
            conn.close()

    # ... (le reste de votre code)

