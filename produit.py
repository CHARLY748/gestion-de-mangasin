from tkinter import *
from PIL import Image, ImageTk 
import os
from tkinter import messagebox,ttk
import time
import sqlite3


class produit:
    def __init__(self,root):
        self.root=root
        self.root.title("produit")
        self.root.geometry("1000x680+350+0")
        self.root.config(bg="white")
        self.root.focus_force()

         # la base de donnée
        
        conn =sqlite3.connect(database=r"C:\Users\USER\Desktop\mon_deuxieme_project\donnee\magasinbase.bd")
        curseur=conn.cursor()
        curseur.execute("CREATE TABLE IF NOT EXISTS produit(ID INTEGER PRIMARY KEY,cathegorie text,fournisseur text,nom text,prix text,quantite text,status text)")
        conn.commit()

         # la base de donnée pour enregistrer la vente
        
        conn =sqlite3.connect(database=r"C:\Users\USER\Desktop\mon_deuxieme_project\donnee\magasinbase.bd")
        curseur=conn.cursor()
        curseur.execute("CREATE TABLE IF NOT EXISTS vente(ID INTEGER PRIMARY KEY AUTOINCREMENT,client_nom text,client_contact text,montant_total text,remise text,montant_paye text,date_vente text)")
        conn.commit()

         # la base de donnée pour enregistrer la vente
        
        conn =sqlite3.connect(database=r"C:\Users\USER\Desktop\mon_deuxieme_project\donnee\magasinbase.bd")
        curseur=conn.cursor()
        curseur.execute("CREATE TABLE IF NOT EXISTS vente_produit(ID INTEGER PRIMARY KEY AUTOINCREMENT,vente_id text,produit_id text,quantite_vendue text)")
        conn.commit()

        product_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        product_frame.place(x=10,y=10,width=480,height=650)


        # les variables
        self.var_prod_nom = StringVar()
        self.var_recherche_txt = StringVar()
        self.var_recherche_type = StringVar()
        self.var_prod_id = StringVar()
        self.var_prod_cat = StringVar()
        self.var_prod_four = StringVar()
        self.var_prod_status = StringVar()
        self.var_prod_prix = StringVar()
        self.var_prod_qte = StringVar() 

        self.four_liste=[]
        self.liste_four()
                
        # titre
        titre= Label(product_frame,text="Details Produit",font=("goudy old style",30,"bold"),bg="blue",fg="white")
        titre.pack(side=TOP,fill=X)

         # ligne1
        label_cathegorie=Label(product_frame,text="Cathegorie",font=("goudy old style",20),bg="white")
        label_cathegorie.place(x=30,y=80)

        label_fournisseur=Label(product_frame,text="Fourniseur",font=("goudy old style",20),bg="white")
        label_fournisseur.place(x=30,y=150)

        label_Nom=Label(product_frame,text="Nom(Marque)",font=("goudy old style",20),bg="white")
        label_Nom.place(x=30,y=220)


        label_prix=Label(product_frame,text="Prix",font=("goudy old style",20),bg="white")
        label_prix.place(x=30,y=290)

        label_Quantité=Label(product_frame,text="Quantité",font=("goudy old style",20),bg="white")
        label_Quantité.place(x=30,y=360)

        label_status=Label(product_frame,text="Status",font=("goudy old style",20),bg="white")
        label_status.place(x=30,y=430)


        # la base de données pour recuperer les donnees dans le combobox pour cathegorie
        conn =sqlite3.connect(database=r"C:\Users\USER\Desktop\mon_deuxieme_project\donnee\magasinbase.bd")
        curseur=conn.cursor()
        curseur.execute("select nom from cathegorie")
        rows=curseur.fetchall()
        conn.commit()


        txt_cathegorie=ttk.Combobox(product_frame,textvariable=self.var_prod_cat,values=rows,state="r",justify=CENTER,font=("goudy old style",20))
        txt_cathegorie.place(x=210,y=80,width=250)  
        txt_cathegorie.set("select")

        txt_fourniseur=ttk.Combobox(product_frame,textvariable=self.var_prod_four,values=self.four_liste,state="r",justify=CENTER,font=("goudy old style",20))
        txt_fourniseur.place(x=210,y=150,width=250)
        txt_fourniseur.set("select")

        txt_nom=Entry(product_frame,textvariable=self.var_prod_nom,font=("goudy old style",20),bg="lightyellow")
        txt_nom.place(x=210,y=230,width=250)

        txt_prix=Entry(product_frame,textvariable=self.var_prod_prix,font=("goudy old style",20),bg="lightyellow")
        txt_prix.place(x=210,y=300,width=250)

        txt_Quantité=Entry(product_frame,textvariable=self.var_prod_qte,font=("goudy old style",20),bg="lightyellow")
        txt_Quantité.place(x=210,y=370,width=250)

        txt_status=ttk.Combobox(product_frame,textvariable=self.var_prod_status,values=["Active","Inactive"],state="r",justify=CENTER,font=("goudy old style",20))
        txt_status.place(x=210,y=430,width=250)
        txt_status.current(0)

        # les boutton

        self.ajout_btn=Button(product_frame,command=self.ajouter,text="Ajouter",font=("times new roman",15,"bold"),cursor="hand2",bg="GREEN",state="normal",bd=3,)
        self.ajout_btn.place(x=10,y=500,width=110,height=50)
        
        self.modifier_btn=Button(product_frame,command=self.modifier,text="Modifier",font=("times new roman",15,"bold"),cursor="hand2",bg="BLUE",state="disabled",bd=3)
        self.modifier_btn.place(x=125,y=500,width=110,height=50)
        
        self.supprimer_btn=Button(product_frame,command=self.supprimer,text="Supprimer",font=("times new roman",15,"bold"),cursor="hand2",bg="RED",state="disabled",bd=3,)
        self.supprimer_btn.place(x=240,y=500,width=110,height=50)
        
        self.renitialiser_btn=Button(product_frame,command=self.renitialiser,text="Renitialiser",font=("times new roman",15,"bold"),cursor="hand2",bg="orange",state="normal",bd=3)
        self.renitialiser_btn.place(x=355,y=500,width=110,height=50)

        # frame recherche
        recher_frame=LabelFrame(self.root,text="Recherche Produits",font=( "times new roman",20),bd=2,relief=RIDGE,bg="white")
        recher_frame.place(x=500,y=10,width=495,height=80)

        txt_recherche_option=ttk.Combobox(recher_frame,textvariable=self.var_recherche_type,values=["cathegorie","fournisseur","nom"],state="r",justify=CENTER,font=("goudy old style",20))
        txt_recherche_option.place(x=5,y=5,width=150)
        txt_recherche_option.current(0)

        txt_recherche=Entry(recher_frame,textvariable=self.var_recherche_txt,font=("goudy old style",20),bg="lightyellow")
        txt_recherche.place(x=160,y=5,width=140)

        recherche=Button(recher_frame,command=self.recherche,text="Recherche",font=("times new roman",15,"bold"),cursor="hand2",bg="blue",state="normal",bd=3,fg="white")
        recherche.place(x=305,y=5,width=100,height=35)

        Aficher=Button(recher_frame,command=self.afficher,text="Aficher",font=("times new roman",15,"bold"),cursor="hand2",bg="green",state="normal",bd=3,fg="white")
        Aficher.place(x=410,y=5,width=80,height=35)

         # liste des produits
        liste_frame=Frame(self.root,bd=3,relief=RIDGE)
        liste_frame.place(x=500,y=90,height=570,width=500)
        
        scroll_y=Scrollbar(liste_frame,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x=Scrollbar(liste_frame,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)
        
        self.produitliste=ttk.Treeview(liste_frame,columns=("ID","cathegorie","fourniseur","nom","prix","quantite","status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.config(command=self.produitliste.xview)
        scroll_y.config(command=self.produitliste.yview)
        
        self.produitliste.heading("ID",text="ID",anchor="w")
        self.produitliste.heading("cathegorie",text="Cathegorie",anchor="w")
        self.produitliste.heading("fourniseur",text="Fourniseur",anchor="w")
        self.produitliste.heading("nom",text="Nom Produit",anchor="w")
        self.produitliste.heading("prix",text="Prix",anchor="w")
        self.produitliste.heading("quantite",text="Quantite")
        self.produitliste.heading("status",text="status")
        
        
        self.produitliste.column("ID",width=60)
        self.produitliste.column("quantite",width=120)
        self.produitliste.column("cathegorie",width=150)
        self.produitliste.column("status",width=100)
        self.produitliste.column("fourniseur",width=150)
        self.produitliste.column("nom",width=140)


        
        self.produitliste["show"]="headings"
        self.produitliste.pack(fill=BOTH,expand=1)
        self.produitliste.bind("<ButtonRelease-1>",self.get_donne) 
        self.afficher()


# cette fonction permet de recuperer des informations sur la table fournisseur et les
# afficher dans le combobox
    def liste_four(self):
        self.four_liste.append("vide")
        conn =sqlite3.connect(database=r"C:\Users\USER\Desktop\mon_deuxieme_project\donnee\magasinbase.bd")
        curseur=conn.cursor()

        try:
                curseur.execute("select nom from founisseur")
                four=curseur.fetchall()
                if len(four)>0:
                    del self.four_liste[:]
                    self.four_liste.append("select")
                    for i in four:
                            self.four_liste.append(i[0])

        except Exception as eror:
                messagebox.showerror("erreur", f" erreurde connection {str(eror)}") 

  # Fonction ajouter
    def ajouter(self):
            conn =sqlite3.connect(database=r"C:\Users\USER\Desktop\mon_deuxieme_project\donnee\magasinbase.bd")
            curseur=conn.cursor()
            try:
                    if self.var_prod_nom.get()=="":
                            messagebox.showerror("erreur","veuillez renseigné le nom du produit")
                    elif self.var_prod_cat.get()=="select":
                            messagebox.showerror("erreur","veuillez renseigné la cathégorie du produit")
                    elif self.var_prod_four.get()=="select":
                            messagebox.showerror("erreur","veuillez renseigné le nom du fournisseur")        
                    else:   
                        curseur.execute( "select * from produit where nom=?", (self.var_prod_nom.get(),))
                        row= curseur.fetchone()
                        if row!=None:
                                messagebox.showerror("erreur","l'identifiant produit existe déja")
                        else:  
                          curseur.execute("insert into produit (cathegorie ,fournisseur ,nom ,prix ,quantite ,status ) values(?,?,?,?,?,?)",(
                            self.var_prod_cat.get(),
                            self.var_prod_four.get(),
                            self.var_prod_nom.get(),
                            self.var_prod_prix.get(),
                            self.var_prod_qte.get(),
                            self.var_prod_status.get()
                          ))
                          conn.commit()
                          self.afficher()
                          self.renitialiser()
                          messagebox.showinfo("succes","ajouter avec succes")
            except Exception as eror:
                messagebox.showerror("erreur", f" erreurde connection {str(eror)}") 

  # fonction afficher             
         #afficher au niveau du Treeview
    def afficher(self):
        conn =sqlite3.connect(database=r"C:\Users\USER\Desktop\mon_deuxieme_project\donnee\magasinbase.bd")
        curseur=conn.cursor()
        try:
                curseur.execute("select * from produit")
                rowss = curseur.fetchall()
                self.produitliste.delete(*self.produitliste.get_children())
                for row in rowss:
                        self.produitliste.insert("",END,values=row)      
        except Exception as eror:
                 messagebox.showerror("erreur", f" erreurde connection {str(eror)}")  


    def get_donne (self, ev):
            self.ajout_btn.config(state="disabled")  
            self.modifier_btn.config(state="normal")
            self.supprimer_btn.config(state="normal")  
            r = self.produitliste.focus()
            contenu=self.produitliste.item(r)
            row = contenu["values"]

            self.var_prod_id.set(row[0]),        
            self.var_prod_cat.set(row[1]),
            self.var_prod_four.set(row[2]),
            self.var_prod_nom.set(row[3]),
            self.var_prod_prix.set(row[4]),
            self.var_prod_qte.set(row[5]),
            self.var_prod_status.set(row[6])

 # bouton modifier           
    def modifier(self):
        conn =sqlite3.connect(database=r"C:\Users\USER\Desktop\mon_deuxieme_project\donnee\magasinbase.bd")
        curseur=conn.cursor()
        try:
             if self.var_prod_id.get()=="":
                   messagebox.showerror("erreur","veuillez entré l'indentifiant")
             else:
                   curseur.execute("select * from produit where ID=?",(self.var_prod_id.get(),)) 
                   row=curseur.fetchone() 
                   if row==None:
                      messagebox.showerror("erreur","veuillez selectionnez un produit")  
                   else:        
                     curseur.execute("update produit set cathegorie=?,fournisseur=?,nom=?,prix=?,quantite=?,status=? WHERE ID=?",(
                     self.var_prod_cat.get(),
                     self.var_prod_four.get(),
                     self.var_prod_nom.get(),
                     self.var_prod_prix.get(),
                     self.var_prod_qte.get(),
                     self.var_prod_status.get(),
                     self.var_prod_id.get()
             ))
             conn.commit()
             self.afficher()
             self.renitialiser()
             messagebox.showinfo("succes","modification effectuer avec succes")
        except Exception as eror:
                 messagebox.showerror("erreur", f" erreurde connection {str(eror)}") 

  #  fonction pour supprimer  
    def supprimer(self):
        conn =sqlite3.connect(database=r"C:\Users\USER\Desktop\mon_deuxieme_project\donnee\magasinbase.bd")
        curseur=conn.cursor()
        try: 
               
                comfirmer = messagebox.askyesno("comfirmer","voulez-vous vraiment suprimer?")
                if comfirmer==TRUE:
                         curseur.execute("DELETE FROM produit WHERE ID=?", (self.var_prod_id.get(),))
                         conn.commit()
                         conn.close()
                         self.afficher()
                         self.renitialiser()
                         messagebox.showinfo("supprimer","suppression effectuer avec succes")
                elif self.var_prod_id.get()=="":
                        messagebox.showerror("erreur","vous n'avez pas selectionnée ")
        except Exception as eror:
                 messagebox.showerror("erreur", f" erreurde connection {str(eror)}")  

    def renitialiser(self):
            self.ajout_btn.config(state="normal")  
            self.modifier_btn.config(state="disabled")
            self.supprimer_btn.config(state="disabled")    
            self.var_prod_id.set("")     
            self.var_prod_nom.set(""),
            self.var_prod_cat.set("select"),
            self.var_prod_four.set("select"),
            self.var_prod_prix.set(""),
            self.var_prod_qte.set(""),
            self.var_prod_status.set("Active"),
            self.var_recherche_txt.set(""),
       #  fonction pour recherche   
    def recherche(self):
        conn =sqlite3.connect(database=r"C:\Users\USER\Desktop\mon_deuxieme_project\donnee\magasinbase.bd")
        curseur=conn.cursor()
        try:     
            if self.var_recherche_txt.get()=="":
                   messagebox.showerror("Erreur","Qu'est ce que vous recherchez?")
            else:
                 curseur.execute("select * from produit where "+self.var_recherche_type.get()+" LIKE '%"+self.var_recherche_txt.get()+"%'") 
                 rows=curseur.fetchall()
                 if len(rows)!=0:
                         self.produitliste.delete(*self.produitliste.get_children())
                         for row in rows: 
                                self.produitliste.insert("",END,values=row)
                 else:
                        messagebox.showerror("Resultat","aucun resultat trouvé")                 
                   
                   
        except Exception as eror:
                 messagebox.showerror("erreur", f" erreurde connection {str(eror)}")         


if __name__=="__main__":
    root= Tk()
    obj= produit(root)
    root.mainloop()
