from tkinter import *
from PIL import Image, ImageTk 
import os
from tkinter import messagebox,ttk
import time
import sqlite3



class fournisseur:
    def __init__(self,root):
        self.root=root
        self.root.title("fournisseur")
        self.root.geometry("1000x680+350+0")
        self.root.config(bg="white")
        self.root.focus_force()
        
        # la base de donnée
        
        conn =sqlite3.connect(database=r"C:\Users\USER\Desktop\mon_deuxieme_project\donnee\magasinbase.bd")
        curseur=conn.cursor()
        curseur.execute("CREATE TABLE IF NOT EXISTS founisseur(ID text PRIMARY KEY,nom text,contact text,ville text,description text)")
        conn.commit()
        
        # les variables
        self.var_four_nom = StringVar()
        self.var_recherche_txt = StringVar()
        self.var_four_id = StringVar()
        self.var_four_ville = StringVar()
        self.var_four_contact = StringVar()
        
         # titre
        titre= Label(self.root,text="formulaire Fournisseur",font=("times new roman",20,"bold"),cursor="hand2",bg="blue",fg="white")
        titre.place(x=0,y=0,width=1050)
        
        # option de recherche
        recerch_option=Label(self.root,text="recherche par ID fournisseur",font=("times new roman",15),bg="white")
        recerch_option.place(x=395,y=80)
        
        recher_txt= Entry(self.root,textvariable=self.var_recherche_txt,font=("times new roman",15),bg="lightyellow")
        recher_txt.place(x=627,y=80,height=40,width=150)
       
        recherche_btn=Button(self.root,command=self.recherche,text="Rechercher",font=("times new roman",15,"bold"),bg="blue",cursor="hand2",bd=2,fg="white")
        recherche_btn.place(x=786,y=80)
        
        tous_btn=Button(self.root,command=self.afficher,text="Aficher",font=("times new roman",15,"bold"),bg="green",cursor="hand2",bd=2,fg="white")
        tous_btn.place(x=910,y=80)
        
        # contenu
        # ligne1
        label_fournid=Label(self.root,text="ID fournisseur",font=("goudy old style",15),bg="white")
        label_fournid.place(x=10,y=80)
        
        self.txt_fournid= Entry(self.root,textvariable=self.var_four_id,font=("goudy old style",20),bg="lightyellow")
        self.txt_fournid.place(x=130,y=80,width=170)
         # ligne2
        label_nom=Label(self.root,text="Nom",font=("goudy old style",15),bg="white")
        label_nom.place(x=10,y=130)
        
        txt_nom= Entry(self.root,textvariable=self.var_four_nom,font=("goudy old style",20),bg="lightyellow")
        txt_nom.place(x=130,y=130,width=170)
          # ligne3
        label_contact=Label(self.root,text="Contact",font=("goudy old style",15),bg="white")
        label_contact.place(x=10,y=180)
        
        txt_contact= Entry(self.root,textvariable=self.var_four_contact,font=("goudy old style",20),bg="lightyellow")
        txt_contact.place(x=130,y=180,width=170)
        
           # ligne4
        label_ville=Label(self.root,text="Ville",font=("goudy old style",15),bg="white")
        label_ville.place(x=10,y=230)
        
        txt_ville= Entry(self.root,textvariable=self.var_four_ville,font=("goudy old style",20),bg="lightyellow")
        txt_ville.place(x=130,y=230,width=170)
        
           # ligne5
        label_description=Label(self.root,text="Description",font=("goudy old style",15),bg="white")
        label_description.place(x=10,y=280)
        
        self.txt_description= Text(self.root,font=("goudy old style",20),bg="lightyellow")
        self.txt_description.place(x=130,y=280,width=327,height=100)
        
        # les boutton
        self.ajout_btn=Button(self.root,command=self.ajouter,text="Ajouter",font=("times new roman",20,"bold"),cursor="hand2",bg="GREEN",state="normal",bd=5,fg="white")
        self.ajout_btn.place(x=130,y=400,width=150,height=45)
        
        self.modifier_btn=Button(self.root,command=self.modifier,text="Modifier",font=("times new roman",20,"bold"),cursor="hand2",bg="BLUE",state="disabled",bd=5,fg="white")
        self.modifier_btn.place(x=310,y=400,width=150,height=45)
        
        self.supprimer_btn=Button(self.root,command=self.supprimer,text="Supprimer",font=("times new roman",20,"bold"),cursor="hand2",bg="RED",state="disabled",bd=5,fg="white")
        self.supprimer_btn.place(x=130,y=470,width=150,height=45)
        
        self.renitialiser_btn=Button(self.root,command=self.renitialiser,text="Renitialiser",font=("times new roman",20,"bold"),cursor="hand2",bg="orange",state="normal",bd=5,fg="white")
        self.renitialiser_btn.place(x=310,y=470,width=150,height=45)
        
        
         # liste Fournisseur
        liste_frame=Frame(self.root,bd=3,relief=RIDGE)
        liste_frame.place(x=480,y=125,height=390,width=525)
        
        scroll_y=Scrollbar(liste_frame,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x=Scrollbar(liste_frame,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)
        
        self.fournisseurliste=ttk.Treeview(liste_frame,columns=("ID","nom","contact","ville","description"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.config(command=self.fournisseurliste.xview)
        scroll_y.config(command=self.fournisseurliste.yview)
        
        self.fournisseurliste.heading("ID",text="Identifiant",anchor="w")
        self.fournisseurliste.heading("nom",text="Nom complet",anchor="w")
        self.fournisseurliste.heading("contact",text="Contact",anchor="w")
        self.fournisseurliste.heading("ville",text="ville",anchor="w")
        self.fournisseurliste.heading("description",text="Description",anchor="w")
        
        
        self.fournisseurliste.column("ID",width=90)
        self.fournisseurliste.column("nom",width=200)
        self.fournisseurliste.column("contact",width=90)
        self.fournisseurliste.column("description",width=300)
        
        self.fournisseurliste["show"]="headings"
        self.fournisseurliste.pack(fill=BOTH,expand=1)
        self.fournisseurliste.bind("<ButtonRelease-1>",self.get_donne) 
        
        self.afficher()
        # Fonction ajouter
    def ajouter(self):
            conn =sqlite3.connect(database=r"C:\Users\USER\Desktop\mon_deuxieme_project\donnee\magasinbase.bd")
            curseur=conn.cursor()
            try:
                    if self.var_four_id.get()=="" :
                            messagebox.showerror("erreur","veuillez renseigné l'identifiant du fournisseur")
                    elif self.var_four_nom.get()=="":
                            messagebox.showerror("erreur","veuillez renseigné le nom du fournisseur")
                    elif self.var_four_contact.get()=="":
                            messagebox.showerror("erreur","veuillez le renseigné contact du fournisseur")
                    else:   
                        curseur.execute( "select * from founisseur where ID=?", (self.var_four_id.get(),))
                        row= curseur.fetchone()
                        if row!=None:
                                messagebox.showerror("erreur","l'identifiant fournisseur existe déja")
                        else:  
                          curseur.execute("insert into founisseur (ID,nom,contact,ville,description) values(?,?,?,?,?)",(
                            self.var_four_id.get(),
                            self.var_four_nom.get(),
                            self.var_four_contact.get(),
                            self.var_four_ville.get(),
                            self.txt_description.get("1.0",END)
                          ))
                          conn.commit()
                          self.afficher()
                          messagebox.showinfo("succes","ajouter avec succes")
            except Exception as eror:
                messagebox.showerror("erreur", f" erreurde connection {str(eror)}") 
                
         # fonction afficher             
    #afficher au niveau du Treeview
    def afficher(self):
        conn =sqlite3.connect(database=r"C:\Users\USER\Desktop\mon_deuxieme_project\donnee\magasinbase.bd")
        curseur=conn.cursor()
        try:
                curseur.execute("select * from founisseur")
                rows = curseur.fetchall()
                self.fournisseurliste.delete(*self.fournisseurliste.get_children())
                for row in rows:
                        self.fournisseurliste.insert("",END,values=row)      
        except Exception as eror:
                 messagebox.showerror("erreur", f" erreurde connection {str(eror)}")   
                 
    #   pour recuperer et pouvoir modifier      

    def get_donne (self, ev):
        self.ajout_btn.config(state="disabled")  
        self.modifier_btn.config(state="normal")
        self.supprimer_btn.config(state="normal")  
        self.txt_fournid.config(state="readonly")
        r = self.fournisseurliste.focus()
        contenu=self.fournisseurliste.item(r)
        row = contenu["values"]
                
        self.var_four_id.set(row[0]),
        self.var_four_nom.set(row[1]),
        self.var_four_contact.set(row[2]),
        self.var_four_ville.set(row[3]),
        self.txt_description.delete("1.0",END),
        self.txt_description.insert(END,row[4])
        
   
       # bouton modifier           
    def modifier(self):
        conn =sqlite3.connect(database=r"C:\Users\USER\Desktop\mon_deuxieme_project\donnee\magasinbase.bd")
        curseur=conn.cursor()
        try:
             curseur.execute("update founisseur set nom=?,contact=?,ville=?,description=? WHERE ID=?",(
                     self.var_four_nom.get(),
                     self.var_four_contact.get(),
                     self.var_four_ville.get(),
                     self.txt_description.get("1.0",END),
                     self.var_four_id.get()
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
                        curseur.execute("delete from founisseur where ID=?",(self.var_four_id.get(),))
                        conn.commit()
                        self.afficher()
                        self.renitialiser()
                        messagebox.showinfo("supprimer","suppression effectuer avec succes")
        except Exception as eror:
                 messagebox.showerror("erreur", f" erreurde connection {str(eror)}")  
                 
    def renitialiser(self):
        self.txt_fournid.config(state="normal")  
        self.ajout_btn.config(state="normal")  
        self.modifier_btn.config(state="disabled")
        self.supprimer_btn.config(state="disabled")    
        self.var_four_id.set("")     
        self.var_four_nom.set(""),
        self.var_four_contact.set(""),
        self.var_four_ville.set(""),
        self.var_recherche_txt.set(""),
        self.txt_description.delete("1.0",END)
        
     #  fonction pour recherche   
    def recherche(self):
        conn =sqlite3.connect(database=r"C:\Users\USER\Desktop\mon_deuxieme_project\donnee\magasinbase.bd")
        curseur=conn.cursor()
        try:     
            if self.var_recherche_txt.get()=="":
                   messagebox.showerror("Erreur","Qu'est ce que vous recherchez?")
            else:
                 curseur.execute("select * from founisseur where ID LIKE ?", ('%' + self.var_recherche_txt.get() + '%',))
                 rows = curseur.fetchall()
                 if len(rows) > 0:
                        self.fournisseurliste.delete(*self.fournisseurliste.get_children())
                        for row in rows:
                           self.fournisseurliste.insert("", END, values=row)
                 else:
                    messagebox.showerror("Résultat", "Aucun résultat trouvé")
                   
        except Exception as eror:
                 messagebox.showerror("erreur", f" erreurde connection {str(eror)}")         

if __name__=="__main__":
    root= Tk()
    obj= fournisseur(root)
    root.mainloop()
