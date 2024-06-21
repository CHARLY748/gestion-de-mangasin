from tkinter import *
from PIL import Image, ImageTk 
import os
from tkinter import messagebox,ttk
import time
import sqlite3


class cathegorie:
    def __init__(self,root):
        self.root=root
        self.root.title("cathegorie")
        self.root.geometry("1000x680+350+0")
        self.root.config(bg="white")
        self.root.focus_force()
        
         # la base de donnée
        
        conn =sqlite3.connect(database=r"C:\Users\USER\Desktop\mon_deuxieme_project\donnee\magasinbase.bd")
        curseur=conn.cursor()
        curseur.execute("CREATE TABLE IF NOT EXISTS cathegorie(ID INTEGER PRIMARY KEY AUTOINCREMENT,nom text)")
        conn.commit()
        
         # les variables
        self.var_cath_nom = StringVar()
        self.var_cath_id = StringVar()
        
          # titre
        titre= Label(self.root,text="Gestion Cathegorie Produit",font=("goudy old style",20,"bold"),bg="blue",fg="white",bd=3 ,relief=RIDGE)
        titre.pack(side=TOP,fill=X,padx=5,pady=5)
        
          # contenu
        # ligne1
        label_cathegorie=Label(self.root,text="Saisir Cathegorie Produit",font=("times new roman",15),bg="white")
        label_cathegorie.place(x=50,y=150)
        txt_cathegorie= Entry(self.root,textvariable=self.var_cath_nom,font=("times new roman",30),bg="lightyellow")
        txt_cathegorie.place(x=50,y=190,width=205,height=42)
        # les boutton
        ajout_btn=Button(self.root,command=self.ajouter,text="Ajouter",font=("times new roman",20,"bold"),cursor="hand2",bg="GREEN",state="normal",bd=2,fg="white")
        ajout_btn.place(x=263,y=190,width=130,height=42)
        
        supprimer_btn=Button(self.root,command=self.supprimer,text="Supprimer",font=("times new roman",20,"bold"),cursor="hand2",bg="RED",state="normal",bd=2,fg="white")
        supprimer_btn.place(x=400,y=190,width=135,height=42)
        
        # LISTE CATHEGORIE
        liste_frame=Frame(self.root,bd=3,relief=RIDGE)
        liste_frame.place(x=545,y=70,height=160,width=450)
        
        scroll_y=Scrollbar(liste_frame,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x=Scrollbar(liste_frame,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)
        
        self.cathegarieliste=ttk.Treeview(liste_frame,columns=("ID","Nom"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.config(command=self.cathegarieliste.xview)
        scroll_y.config(command=self.cathegarieliste.yview)
        
        self.cathegarieliste.heading("ID",text="Identifiant",anchor="w")
        self.cathegarieliste.heading("Nom", text="Nom Cathégorie",anchor="w")
        self.cathegarieliste["show"]="headings"
        
        self.cathegarieliste.pack(fill=BOTH,expand=1)
        self.cathegarieliste.bind("<ButtonRelease-1>",self.get_donne) 
        self.afficher()
        
        self.image1= Image.open(r"C:\Users\USER\Desktop\mon_deuxieme_project\image\cath1.jpg")
        self.image1=self.image1.resize((470,350))
        self.image1=ImageTk.PhotoImage(self.image1)
        
        self.label_image1=Label(self.root,bd=7,relief=RAISED,image=self.image1)
        self.label_image1.place(x=45,y=240)
        
        self.image2= Image.open(r"C:\Users\USER\Desktop\mon_deuxieme_project\image\cath2.jpg")
        self.image2=self.image2.resize((450,350))
        self.image2=ImageTk.PhotoImage(self.image2)
        
        self.label_image2=Label(self.root,bd=7,relief=RAISED,image=self.image2)
        self.label_image2.place(x=530,y=240)
        
    def ajouter(self):
            conn =sqlite3.connect(database=r"C:\Users\USER\Desktop\mon_deuxieme_project\donnee\magasinbase.bd")
            curseur=conn.cursor()
            try:
                    if self.var_cath_nom.get()=="" :
                            messagebox.showerror("erreur","veuillez renseigné le nom de la cathégorie produit")
                    else:
                        curseur.execute("select * from cathegorie where nom=?",(self.var_cath_nom.get(),))  
                        row=curseur.fetchone()
                        if row!=None:
                                messagebox.showerror("erreur","la cathégorie existe déja")
                        else: 
                            curseur.execute("insert into cathegorie (nom) values(?)",(self.var_cath_nom.get(),))  
                            conn.commit()
                            self.var_cath_id.set("")
                            self.var_cath_nom.set("")
                            self.afficher()  
                            messagebox.showinfo("succes","Enregistrement éffectué")   
            except Exception as eror:
                messagebox.showerror("erreur", f" erreurde connection {str(eror)}") 
                
    def afficher(self):
        conn =sqlite3.connect(database=r"C:\Users\USER\Desktop\mon_deuxieme_project\donnee\magasinbase.bd")
        curseur=conn.cursor()
        try:
                curseur.execute("select * from cathegorie")
                rows = curseur.fetchall()
                self.cathegarieliste.delete(*self.cathegarieliste.get_children())
                for row in rows:
                                self.cathegarieliste.insert("",END,values=row)      
                        
        except Exception as eror:
                 messagebox.showerror("erreur", f" erreurde connection {str(eror)}")   
                 
                 
     #   pour recuperer et pouvoir modifier      

    def get_donne (self, ev):
        r = self.cathegarieliste.focus()
        contenu=self.cathegarieliste.item(r)
        row = contenu["values"]
                
        self.var_cath_id.set(row[0]),
        self.var_cath_nom.set(row[1])
        
     #  fonction pour supprimer  
    def supprimer(self):
        conn =sqlite3.connect(database=r"C:\Users\USER\Desktop\mon_deuxieme_project\donnee\magasinbase.bd")
        curseur=conn.cursor()
        try: 
                comfirmer = messagebox.askyesno("comfirmer","voulez-vous vraiment suprimer?")
                if comfirmer==TRUE:
                        curseur.execute("delete from cathegorie where ID=?",(self.var_cath_id.get(),))
                        conn.commit()
                        self.var_cath_id.set("")
                        self.var_cath_nom.set("")
                        self.afficher()
                        messagebox.showinfo("supprimer","suppression effectuer avec succes")
        except Exception as eror:
                 messagebox.showerror("erreur", f" erreurde connection {str(eror)}")  
                     
        
                    
                       
                


if __name__=="__main__":
    root= Tk()
    obj= cathegorie(root)
    root.mainloop()
