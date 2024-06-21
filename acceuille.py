from tkinter import *
from PIL import Image, ImageTk 
import os
import pygetwindow as gw
from tkinter import messagebox,ttk
import time
import sqlite3
from tkinter import simpledialog
import datetime

from tkinter import Tk, Button
# from caisse import somme_ventes_par_date as caisse_somme_ventes_par_date

# import customtkinter



class acceuil:
    def __init__(self,root):
        self.root=root
        self.root.title("acceuil")
        self.root.geometry("1360x690+0+0")
        self.root.config(bg="white")

         #les variables
        self.var_recherche=StringVar()
        self.var_clnom=StringVar()
        self.var_clcontact=StringVar()
        self.date_saisie=StringVar()
        self.cart_list=[]
        self.ck_print=0
        self.date_saisie = StringVar()

        self.var_id = StringVar()
        self.var_nom = StringVar()
        self.var_montant = StringVar()
        self.var_date = StringVar()
        self.var_total= StringVar()
        self.var_remise = StringVar()



        
        
        titre = Label(self.root,text="Magasin charly Design",font=( "times new roman",40,"bold"),fg="white", bg="BLUE",anchor="w",
                      padx=20,compound=LEFT).place(x=0, y=0 ,relwidth=1, height=100 )
        # Boutton deconecté
        btn_decon= Button(self.root,command=self.deconecté, fg="white",text="Déconnecté",font=( "times new roman",20,"bold"),
                          cursor="hand2",bg="red").place(x=1205,y=25)
        # HEURE
        self.label_heure=Label(self.root,text="Bienvenue chez charly Design\t\t Date:DO-MM-YYYY\t\t Heure:HH:MM:SS",
                               font=( "times new roman",15,"bold"),bg="black",fg="white")
        self.label_heure.place(x=0, y=100 ,relwidth=1, height=40 )

        # menu
        self.menulogo= Image.open(r"C:\Users\USER\Desktop\mon_deuxieme_project\image\10.png")
        self.menulogo=self.menulogo.resize((340 ,165))
        self.menulogo=ImageTk.PhotoImage(self.menulogo)
        
        menu_frame= Frame(self.root ,bd=2,relief=RIDGE,bg="white")
        menu_frame.place(x=0 ,y=140,width=345,height=525) 
        label_menulogo=Label(menu_frame,image=self.menulogo)
        label_menulogo.pack(side=TOP,fill=X)
        
        self.icon_menu= Image.open(r"C:\Users\USER\Desktop\mon_deuxieme_project\image\i2.jpg")
        self.icon_menu=self.icon_menu.resize((100 ,30))
        self.icon_menu=ImageTk.PhotoImage(self.icon_menu)

        label_menu=Label(menu_frame,text="Menu",font=( "times new roman",20,"bold"),fg="white", bg="blue").pack(side=TOP,fill=X)
        btn_employé=Button(menu_frame,activebackground="blue",command=self.employe,image=self.icon_menu,text="Employé",font=( "times new roman",20,"bold"),anchor="w",compound=LEFT,padx=10,cursor="hand2",bg="white",).pack(side=TOP,fill=X) 
        btn_fournisseur=Button(menu_frame,activebackground="blue",command=self.fournisseur,image=self.icon_menu,text="Fournisseur",font=( "times new roman",20,"bold"),anchor="w",compound=LEFT,padx=10,cursor="hand2",bg="white",).pack(side=TOP,fill=X) 
        btn_cathegorie=Button(menu_frame,activebackground="blue",command=self.Cathegorie,image=self.icon_menu,text="Cathegorie",font=( "times new roman",20,"bold"),anchor="w",compound=LEFT,padx=10,cursor="hand2",bg="white",).pack(side=TOP,fill=X) 
        btn_produit=Button(menu_frame,activebackground="blue",command=self.produit,image=self.icon_menu,text="Produit",font=( "times new roman",20,"bold"),anchor="w",compound=LEFT,padx=10,cursor="hand2",bg="white",).pack(side=TOP,fill=X) 
        btn_vente=Button(menu_frame,activebackground="blue",command=self.vente,image=self.icon_menu,text="Vente",font=( "times new roman",20,"bold"),anchor="w",compound=LEFT,padx=10,cursor="hand2",bg="white",).pack(side=TOP,fill=X) 
        btn_quitter=Button(menu_frame,activebackground="blue",command=self.quitter,image=self.icon_menu,text="Quitter",font=( "times new roman",20,"bold"),anchor="w",compound=LEFT,padx=10,cursor="hand2",bg="white",).pack(side=TOP,fill=X) 
        
        # contenue du menu
        self.label_total_base=Label(self.root,text="Les Enregistrement",bg="blue",relief=RAISED,fg="white",font=( "time new roman",20,"bold"))
        self.label_total_base.place(x=345,y=310,width=400)

        self.label_total_employe=Label(self.root,text="Total Employé[0]",bg="white",bd=5,relief=RAISED,fg="BLACK",font=( "goudy old style",20,"bold"))
        self.label_total_employe.place(x=345,y=410,width=400,height=61)
        
        self.label_total_fournisseur=Label(self.root,text="Total Fourniseur[0]",bg="white",bd=5,relief=RAISED,fg="BLACK",font=( "goudy old style",20,"bold"))
        self.label_total_fournisseur.place(x=345,y=348,width=400,height=61)
        
        self.label_total_cathegorie=Label(self.root,text="Total Cathogorie[0]",bg="white",bd=5,relief=RAISED,fg="BLACK",font=( "goudy old style",20,"bold"))
        self.label_total_cathegorie.place(x=345,y=472,width=400,height=61)
        
        self.label_total_produit=Label(self.root,text="Total Produit[0]",bg="white",bd=5,relief=RAISED,fg="BLACK",font=( "goudy old style",20,"bold"))
        self.label_total_produit.place(x=345,y=535,width=400,height=61)
        
        self.label_total_vente=Label(self.root,text="Total Vente[0]",bg="white",bd=5,relief=RAISED,fg="BLACK",font=( "goudy old style",20,"bold"))
        self.label_total_vente.place(x=345,y=598,width=400,height=61)

        ## label pour affficher la somme par date et les dans la page acceuille
        label_somme= Label(self.root,text="Consulter le Total des Ventes ",bg="blue",fg="white",font=("times new roman",20,"bold"),bd=5)
        label_somme.place(x=345,y=140,width=400,height=30)

        label_date= Label(self.root,text="Entrez la date (YYYY-MM-DD) ",bg="white",font=("goudy old style",20,"bold"),bd=5)
        label_date.place(x=345,y=180,width=400,height=30)

        self.entry_somme= Entry(self.root,bg="lightgray",textvariable=self.date_saisie,font=("goudy old style",20,"bold"),bd=2)
        self.entry_somme.place(x=345,y=220,width=190,height=40)

        entry_button= Button(self.root,text="Valider",command=self.somme_ventes_par_date,fg="white",cursor="hand2",bg="green",font=("goudy old style",20,"bold"),bd=5)
        entry_button.place(x=540,y=220,width=100,height=40)

        renit_button= Button(self.root,text="Delete",command=self.renill,fg="white",bg="red",cursor="hand2",font=("goudy old style",20,"bold"),bd=5)
        renit_button.place(x=645,y=220,width=100,height=40)

        self.label_date= Label(self.root,text="Somme Total du jour:[0]",bg="lightyellow",font=("goudy old style",20,"bold"),bd=5,relief=RAISED,fg="BLACK")
        self.label_date.place(x=345,y=260,width=400,height=50)

        frameDroit=Frame(self.root,bg="white",bd=5,relief=RIDGE)
        frameDroit.place(x=745,y=140,width=612,height=520)

        self.label__vente=Label(frameDroit,text="Le Prix de vente Total de la caisse du jour\n\n[000000000.000]",font=("goudy old style",20,"bold"),fg="black",bg="lightgray")
        self.label__vente.pack(side=TOP,fill=X)

        affich_button= Button(frameDroit,text="Cliquez ici",cursor="hand2",command=self.somme,fg="black",bg="lightgray",bd=0,font=("times new roman",20,"bold"))
        affich_button.place(x=0,y=60,width=200,height=40)

        donne_button= Label(frameDroit,text="voir toutes les ventes",cursor="hand2",fg="white",bg="black",bd=5,font=("times new roman",20,"bold"))
        donne_button.place(x=0,y=160,width=602,height=40)

        
        liste_frame=Frame(frameDroit,background="blue",bd=3,relief=RIDGE)
        liste_frame.place(x=0,y=200,height=310,relwidth=1)
        scroll_y=Scrollbar(liste_frame,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x=Scrollbar(liste_frame,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)

        self.venteliste=ttk.Treeview(liste_frame,columns=("ID","client_nom" ,"client_contact", "montant_total", "remise", "montant_paye", "date_vente"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.config(command=self.venteliste.xview)
        scroll_y.config(command=self.venteliste.yview)
        
        self.venteliste.heading("ID",text="ID",anchor="w")
        self.venteliste.heading("client_nom", text="client_nom",anchor="w")
        self.venteliste.heading("montant_total",text="montant_total",anchor="w")
        self.venteliste.heading("remise",text="remise",anchor="w")
        self.venteliste.heading("montant_paye",text="montant_paye",anchor="w")     
        self.venteliste.heading("date_vente",text="date_vente",anchor="w")        

       
        self.venteliste["show"]="headings" 
        self.venteliste.bind("<ButtonRelease-1>",self.get_donne)                         
        self.afficherr()
        self.venteliste.pack(fill=BOTH,expand=1)
        
        self.modifier()
        ## la
        # pied de page ou flooter
        label_footer=Label(self.root,text="Developper par charles kagambega\t\tcharleskagambega5@gmail.com\t\t+22664150340\t\tcopyright 2024",
        font=( "times new roman",16,"bold"),bg="black",fg="white").pack(side=BOTTOM,fill=X)
    #   fonction pour les boutton
        
    def afficherr(self):
        conn =sqlite3.connect(database=r"C:\Users\USER\Desktop\mon_deuxieme_project\donnee\magasinbase.bd")
        curseur=conn.cursor()
        try:
                curseur.execute("select * from vente")
                rowss = curseur.fetchall()
                self.venteliste.delete(*self.venteliste.get_children())
                for row in rowss:
                        self.venteliste.insert("",END,values=row)      
        except Exception as eror:
                 messagebox.showerror("erreur", f" erreurde connection {str(eror)}")  



    def get_donne (self, ev):
        r = self.venteliste.focus()
        contenu=self.venteliste.item(r)
        row = contenu["values"]
                
        self.var_id.set(row[0]),
        self.var_nom.set(row[1]),
        self.var_total.set(row[2]),
        self.var_remise.set(row[3]),
        self.var_montant.set(row[4]),
        self.var_date.set(row[5]),
        

    def employe(self):
        self.obj=os.system("python3.11.exe c:/Users/USER/Desktop/mon_deuxieme_project/employe.py")  
        
    def Cathegorie(self):
        self.obj=os.system("python3.11.exe c:/Users/USER/Desktop/mon_deuxieme_project/cathegorie.py")  
   
    def fournisseur(self):
        self.obj=os.system("python3.11.exe c:/Users/USER/Desktop/mon_deuxieme_project/fournisseur.py")  
        
    def produit(self):
        self.obj=os.system("python3.11.exe c:/Users/USER/Desktop/mon_deuxieme_project/produit.py")  
        
    def vente(self):
        self.obj=os.system("python3.11.exe c:/Users/USER/Desktop/mon_deuxieme_project/vente.py")  
        
    def quitter(self): 
        self.root.destroy() 
        
    def deconecté(self):
        self.root.destroy()
        self.obj=os.system("python3.11.exe c:/Users/USER/Desktop/mon_deuxieme_project/login.py")  
             
    def modifier(self):
        conn =sqlite3.connect(database=r"C:\Users\USER\Desktop\mon_deuxieme_project\donnee\magasinbase.bd")
        curseur=conn.cursor()
        try:
            curseur.execute("select * from produit")
            produit= curseur.fetchall()
            self.label_total_produit.config(text=f"Total Produit[{str(len(produit))}]")
            
            curseur.execute("select * from cathegorie")
            cathegorie= curseur.fetchall()
            self.label_total_cathegorie.config(text=f"Total Cathogorie[{str(len(cathegorie))}]")

            curseur.execute("select * from founisseur")
            founisseur= curseur.fetchall()
            self.label_total_fournisseur.config(text=f"Total Fourniseur[{str(len(founisseur))}]")

            curseur.execute("select * from employe")
            employe= curseur.fetchall()
            self.label_total_employe.config(text=f"Total Employé[{str(len(employe))}]")

            nombreFacture=len(os.listdir(r"C:\Users\USER\Desktop\mon_deuxieme_project\facture"))
            self.label_total_vente.config(text=f"Total Vente[{str(nombreFacture)}]")


            heure=(time.strftime("%H:%M:%S")) 
            date=(time.strftime("%d-%m-%Y"))
            self.label_heure.config(text=f"Bienvenue chez charly Design\t\t Date:{str(date)}\t\t Heure:{str(heure)}") 
            self.label_heure.after(200,self.modifier)

        except Exception as eror:
                 messagebox.showerror("erreur", f" erreurde connection {str(eror)}")  
           
           
            

    def somme_ventes_par_date(self):
    # Demander à l'utilisateur de saisir la date
       if self.date_saisie.get()=="":
                messagebox.showerror("erreur","veuillez entrer la date")
       else:
        # Effectuer la somme des ventes pour la date spécifiée
        conn = sqlite3.connect(database=r"C:\Users\USER\Desktop\mon_deuxieme_project\donnee\magasinbase.bd")
        curseur = conn.cursor()

        try:
            
            date_specifiee = self.date_saisie.get()
            date_specifiee_partie = date_specifiee.split()[0]  # Obtenir la partie "YYYY-MM-DD"

            print(f"Date spécifiée : {date_specifiee}")

            curseur.execute("SELECT SUM(montant_paye) FROM vente WHERE DATE(date_vente) = ?", (date_specifiee_partie,))
            total_ventes = curseur.fetchone()[0]
            self.label_date.config(text=f"Somme Total du jour:{str(total_ventes)}")

            print(f"Total des ventes pour la date {date_specifiee} : {total_ventes}")

            if total_ventes=="":
                # self.label_date.config(text=f"Somme Total du jour:[{str(total_ventes)}]")
                messagebox.showinfo("Somme des ventes", f"La somme des ventes pour {date_specifiee} est : {total_ventes}")

                # Mettre à jour le texte du label avec la somme
            # else:
            #     messagebox.showinfo("Somme des ventes", f"Aucune vente enregistrée pour {date_specifiee}")

        except Exception as error:
            messagebox.showerror("Erreur", f"Erreur de connexion : {str(error)}")
        finally:
            conn.close()
        # self.renill()    
       
           
    def renill(self):
        self.date_saisie.set("") 
        self.label__vente.config(text="Le Prix de vente Total de la caisse du jour\n\n[000000000.000]") 
        self.label_date.config(text="Somme Total du jour:[0]")

    def somme(self):

        try:
             
            # Obtenir la date du jour
            date_du_jour = datetime.date.today()
               
            conn = sqlite3.connect(database=r"C:\Users\USER\Desktop\mon_deuxieme_project\donnee\magasinbase.bd")
            curseur = conn.cursor()
                # Exécuter la requête SQL en utilisant la date du jour
            curseur.execute("SELECT SUM(montant_paye) FROM vente WHERE DATE(date_vente) = ?", (date_du_jour,))
            total_ventees = curseur.fetchone()[0]
            if (curseur.fetchone()==None):
                messagebox.showinfo ("pas de vente","vous n'avez pas vendu aujourd'hui") 
            
                # Mettre à jour l'étiquette avec le résultat
            self.label__vente.config(text=f"Le Prix de vente Total de la caisse du jour\n\n[{str(total_ventees)}]")
          
        except Exception as e:
             messagebox.showerror("erreur",f"error de connection {str(e)}")  
        
if __name__=="__main__":
    root= Tk()
    obj= acceuil(root)
    root.mainloop()
        
     
        
        


