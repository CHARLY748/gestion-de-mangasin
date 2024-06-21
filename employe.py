from tkinter import *
from PIL import Image, ImageTk 
import os
from tkinter import messagebox,ttk
import time
import sqlite3


class employe:
    def __init__(self,root):
        self.root=root
        self.root.title("employe")
        self.root.geometry("1000x680+350+0")
        self.root.config(bg="white")
        self.root.focus_force()
        
        

        # la base de donnée
        
        conn =sqlite3.connect(database=r"C:\Users\USER\Desktop\mon_deuxieme_project\donnee\magasinbase.bd")
        curseur=conn.cursor()
        curseur.execute("""CREATE TABLE IF NOT EXISTS employe(ID text INTEGER PRIMARY KEY,Nom text,Email text,
                           Sexe text,contact text,Naissance text,Adhésion text,password text,Type text,Adresse text,Salaire text,Fonction text)""")
        conn.commit()
        
        # les variable
        self.var_recherche_type = StringVar()
        self.var_recherche_txt = StringVar()
        self.var_emplo_id = StringVar()
        self.var_sexe= StringVar()
        self.var_contact= StringVar()
        self.var_nom_complet= StringVar()
        self.var_naissance= StringVar()
        self.var_adhesion= StringVar()
        self.var_email= StringVar()
        self.var_pasword= StringVar()
        self.var_type= StringVar()
        self.var_salaire= StringVar()
        self.var_fonction= StringVar()
        
        
        # frame du boutton recherche
        rech_frame= LabelFrame(self.root, text="Rechercher Employé",font=("goudy old style",20,"bold"),bd=2,relief=RIDGE,bg="white")
        rech_frame.place(x=150,y=20,width=700,height=90)
        
        # OPTION DE RECHERCHE
        rech_option=ttk.Combobox(rech_frame,textvariable=self.var_recherche_type,values=("Nom","Email","contact","Adresse"),font=("times new roman",20,"bold"),state="r",justify=CENTER)
        rech_option.current(0)
        rech_option.place(x=10,y=10,width=180)
        
        rech_txt=Entry(rech_frame,textvariable=self.var_recherche_txt,font=("times new roman",20,"bold"),bg="lightyellow")
        rech_txt.place(x=210,y=10,width=150)
       
        recherche = Button(rech_frame,text="rechercher",command=self.recherche,font=("times new roman",20,"bold"),cursor="hand2",bg="blue",fg="white")
        recherche.place(x=380,y=5,height=40)
       
        tous= Button(rech_frame,command=self.afficher,text="afficher",font=("times new roman",20,"bold"),cursor="hand2",bg="green",fg="white")
        tous.place(x=560,y=5,height=40)
        
        # tittre
        titre= Label(self.root,text="formulaire employé",font=("times new roman",20,"bold"),cursor="hand2",bg="blue",fg="white")
        titre.place(x=0,y=120,width=1000)
        
        label_empid=Label(self.root,text="ID Employé",font=("goudy old style",15,"bold"),bg="white").place(x=0,y=175,width=160)
        label_empsexe=Label(self.root,text="Sexe",font=("goudy old style",15,"bold"),bg="white").place(x=320,y=175,width=160)
        label_empcontact=Label(self.root,text="Contact",font=("goudy old style",16,"bold"),bg="white").place(x=630,y=175,width=160)
        
        self.txt_empid=Entry(self.root,textvariable=self.var_emplo_id,font=("times new roman",15,"bold"),bg="lightyellow")
        self.txt_empid.place(x=150,y=175,width=180,height=30)
        txt_empsexe=ttk.Combobox(self.root,textvariable=self.var_sexe,values=("Homme","Femme"),font=("goudy old style",15,"bold"),state="r",justify=CENTER)
        txt_empsexe.current(0)
        txt_empsexe.place(x=455,y=175,width=190,height=30)
        txt_empcontact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=785,y=175,width=180,height=30)

# dexieme ligne
        label_empnom=Label(self.root,text="Nom Complet",font=("goudy old style",15,"bold"),bg="white").place(x=-15,y=220,width=200)
        label_empnaisance=Label(self.root,text="Date Naissance",font=("goudy old style",15,"bold"),bg="white").place(x=295,y=220,width=200)
        label_empadhesion=Label(self.root,text="Date Adhesion",font=("goudy old style",15,"bold"),bg="white").place(x=620,y=220,width=200)

        txt_empnom=Entry(self.root,textvariable=self.var_nom_complet,font=("times new roman",15,"bold"),bg="lightyellow").place(x=150,y=220,width=180,height=30)
        txt_empadhesion=Entry(self.root,textvariable=self.var_naissance,font=("times new roman",15,"bold"),bg="lightyellow").place(x=458,y=220,width=187,height=30)
        txt_empadhesion=Entry(self.root,textvariable=self.var_adhesion,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=785,y=220,width=180,height=30)


# troixieme ligne
        label_empemail=Label(self.root,text="Email",font=("goudy old style",15,"bold"),bg="white").place(x=-15,y=265,width=200)
        label_emppassord=Label(self.root,text="Mot de passe",font=("goudy old style",15,"bold"),bg="white").place(x=295,y=265,width=200)
        label_emptype=Label(self.root,text="Type",font=("goudy old style",15,"bold"),bg="white").place(x=620,y=265,width=200)

        txt_empemail=Entry(self.root,textvariable=self.var_email,font=("times new roman",15,"bold"),bg="lightyellow").place(x=150,y=265,width=180,height=30)
        txt_emppassord=Entry(self.root,textvariable=self.var_pasword,font=("times new roman",15,"bold"),bg="lightyellow").place(x=458,y=265,width=187,height=30)
        txt_emptype=ttk.Combobox(self.root,textvariable=self.var_type,values=("Admin","Employé"),font=("goudy old style",15,"bold"),state="r",justify=CENTER)
        txt_emptype.current(0)
        txt_emptype.place(x=780,y=265,width=190,height=30)
        
# quatrieme ligne
        label_empadresse=Label(self.root,text="Adresse",font=("goudy old style",15,"bold"),bg="white").place(x=-15,y=310,width=200)
        label_empsalaire=Label(self.root,text="Salaire",font=("goudy old style",15,"bold"),bg="white").place(x=295,y=310,width=200)
        label_empfonction=Label(self.root,text="Fonction",font=("goudy old style",15,"bold"),bg="white").place(x=620,y=310,width=200)
       
        self.txt_empadresse=Text(self.root,font=("times new roman",15,"bold"),bg="lightyellow")
        self.txt_empadresse.place(x=150,y=310,width=180,height=90)
        txt_empsalaire=Entry(self.root,textvariable=self.var_salaire,font=("times new roman",15,"bold"),bg="lightyellow").place(x=458,y=310,width=187,height=30)
        txt_empfonction=Entry(self.root,textvariable=self.var_fonction,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=785,y=310,width=180,height=30)
    #  les boutton   
        self.btn_ajouter=Button(self.root,command=self.ajouter,state="normal",text="Ajouter",font=("times new roman",20,"bold"),cursor="hand2",bg="BLUE",fg="white")
        self.btn_ajouter.place(x=345,y=360,height=40)
        self.btn_Modifier=Button(self.root,command=self.modifier,text="Modifier",state="disabled",font=("times new roman",20,"bold"),cursor="hand2",bg="green",fg="white")
        self.btn_Modifier.place(x=480,y=360,height=40)
        self.btn_Supprimer=Button(self.root,command=self.supprimer,text="Supprimer",state="disabled",font=("times new roman",20,"bold"),cursor="hand2",bg="red",fg="white")
        self.btn_Supprimer.place(x=630,y=360,height=40)
        btn_Renitialiser=Button(self.root,command=self.renitialiser,text="Renitialiser",font=("times new roman",20,"bold"),cursor="hand2",bg="orange",fg="white").place(x=802,y=360,height=40)
        
        # liste empoyé
        liste_frame=Frame(self.root,bd=3,relief=RIDGE)
        liste_frame.place(x=-2,y=400,height=280,relwidth=1)
        
        scroll_y=Scrollbar(liste_frame,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x=Scrollbar(liste_frame,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)
        
        self.employeliste=ttk.Treeview(liste_frame,columns=("ID","Nom complet","Email","Sexe","contact","Naissance","Adhésion","password","Type","Adresse","Salaire","Fonction"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.config(command=self.employeliste.xview)
        scroll_y.config(command=self.employeliste.yview)
        
        self.employeliste.heading("ID",text="ID",anchor="w")
        self.employeliste.heading("Nom complet", text="Nom et Prenom",anchor="w")
        self.employeliste.heading("Email",text="Email",anchor="w")
        self.employeliste.heading("Sexe",text="Sexe",anchor="w")
        self.employeliste.heading("contact",text="Contact",anchor="w")        
        self.employeliste.heading("Naissance",text="Naissance",anchor="w")
        self.employeliste.heading("Adhésion",text="Adhésion",anchor="w")
        self.employeliste.heading("password",text="password",anchor="w")
        self.employeliste.heading("Type",text="Type",anchor="w")
        self.employeliste.heading("Adresse",text="Adresse",anchor="w")
        self.employeliste.heading("Salaire",text="Salaire",anchor="w")
        self.employeliste.heading("Fonction",text="Fonction",anchor="w")
       
        self.employeliste["show"]="headings" 
        self.employeliste.bind("<ButtonRelease-1>",self.get_donne)                         
       
        self.employeliste.pack(fill=BOTH,expand=1)
        
        self.employeliste.column("ID",width=70)
        self.employeliste.column("Sexe",width=70)
        self.employeliste.column("Email",width=230)
        self.employeliste.column("contact",width=70)
        self.employeliste.column("Naissance",width=70)
        self.employeliste.column("Adhésion",width=70)
        self.employeliste.column("Type",width=70)
        self.employeliste.column("password",width=70)
        self.employeliste.column("Nom complet",width=150)
        self.employeliste.column("Fonction",width=70)
        self.employeliste.column("Salaire",width=70)
        self.employeliste.column("Adresse",width=150)
        self.afficher()
        # self.renitialiser()
# fonction ajouter
    def ajouter(self):
        conn =sqlite3.connect(database=r"C:\Users\USER\Desktop\mon_deuxieme_project\donnee\magasinbase.bd")
        curseur=conn.cursor()
        try:
                if self.var_emplo_id.get()=="" :
                        messagebox.showerror("erreur","veuillez renseigné l'identifiant")
                elif self.var_pasword.get()=="":
                        messagebox.showerror("erreur","veuillez renseigné le mot de passe")
                elif self.var_type.get()=="":
                        messagebox.showerror("erreur","veuillez le type")
                else:
                        curseur.execute( "select * FROM employe where ID=?", (self.var_emplo_id.get(),))
                        row= curseur.fetchone()
                        if row!=None:
                                messagebox.showerror("erreur","l'identifiant existe déja")
                        else:  
                                curseur.execute("insert into employe(ID,Nom,Email,Sexe,contact , Naissance , Adhésion ,password,Type ,Adresse,Salaire ,Fonction )values(?,?,?,?,?,?,?,?,?,?,?,?)",(
                                      self.var_emplo_id.get(),
                                      self.var_nom_complet.get(),
                                      self.var_email.get(),
                                      self.var_sexe.get(),
                                      self.var_contact.get(),
                                      self.var_naissance.get(),
                                      self.var_adhesion.get(),
                                      self.var_pasword.get(),
                                      self.var_type.get(),
                                      self.txt_empadresse.get("1.0",END),
                                      self.var_salaire.get(),
                                      self.var_fonction.get()  
                                ))  
                                conn.commit() 
                                self.afficher()
                                self.renitialiser()
                                messagebox.showinfo("succes","ajouter avec succes")           
                        
        except Exception as eror:
                messagebox.showerror("erreur", f" erreurde connection {str(eror)}")    
   
#    afficher au niveau du Treeview
    def afficher(self):
        conn =sqlite3.connect(database=r"C:\Users\USER\Desktop\mon_deuxieme_project\donnee\magasinbase.bd")
        curseur=conn.cursor()
        try:
                curseur.execute("select * from employe")
                rows = curseur.fetchall()
                self.employeliste.delete(*self.employeliste.get_children())
                for row in rows:
                                self.employeliste.insert("",END,values=row)      
                        
        except Exception as eror:
                 messagebox.showerror("erreur", f" erreurde connection {str(eror)}")    
           
        
 #   pour recuperer et pouvoir modifier      

    def get_donne (self, ev):
        self.btn_ajouter.config(state="disabled")  
        self.btn_Modifier.config(state="normal")
        self.btn_Supprimer.config(state="normal")  
        self.txt_empid.config(state="readonly")
        r = self.employeliste.focus()
        contenu=self.employeliste.item(r)
        row = contenu["values"]
                
        self.var_emplo_id.set(row[0]),
        self.var_nom_complet.set(row[1]),
        self.var_email.set(row[2]),
        self.var_sexe.set(row[3]),
        self.var_contact.set(row[4]),
        self.var_naissance.set(row[5]),
        self.var_adhesion.set(row[6]),
        self.var_pasword.set(row[7]),
        self.var_type.set(row[8]),
        self.txt_empadresse.delete("1.0",END),
        self.txt_empadresse.insert(END,row[9])
        self.var_salaire.set(row[10]),
        self.var_fonction.set(row[11])   
        
        # bouton modifier           
    def modifier(self):
        conn =sqlite3.connect(database=r"C:\Users\USER\Desktop\mon_deuxieme_project\donnee\magasinbase.bd")
        curseur=conn.cursor()
        try:
               curseur.execute("update employe set Nom=?,Email=?,Sexe=?,contact=? , Naissance=? , Adhésion=? ,password=?,Type=? ,Adresse=?,Salaire=? ,Fonction=? where ID=?",( 
                                self.var_nom_complet.get(),
                                self.var_email.get(),
                                self.var_sexe.get(),
                                self.var_contact.get(),
                                self.var_naissance.get(),
                                self.var_adhesion.get(),
                                self.var_pasword.get(),
                                self.var_type.get(),
                                self.txt_empadresse.get("1.0",END),
                                self.var_salaire.get(),
                                self.var_fonction.get(),
                                self.var_emplo_id.get()
               ))
               conn.commit()
               self.afficher()
               self.renitialiser()
               messagebox.showinfo("succes","modification effectuer avec succes")
        except Exception as eror:
                 messagebox.showerror("erreur", f" erreurde connection {str(eror)}") 
                 
                #  boutton pour supprimer  
    def supprimer(self):
        conn =sqlite3.connect(database=r"C:\Users\USER\Desktop\mon_deuxieme_project\donnee\magasinbase.bd")
        curseur=conn.cursor()
        try: 
                comfirmer = messagebox.askyesno("comfirmer","voulez-vous vraiment suprimer?")
                if comfirmer==TRUE:
                        curseur.execute("delete from employe where ID=?",(self.var_emplo_id.get(),))
                        conn.commit()
                        self.afficher()
                        self.renitialiser()
                        messagebox.showinfo("supprimer","suppression effectuer avec succes")
        except Exception as eror:
                 messagebox.showerror("erreur", f" erreurde connection {str(eror)}") 
    #pour renitialiser 
    def renitialiser(self):
        self.txt_empid.config(state="normal")  
        self.btn_ajouter.config(state="normal")  
        self.btn_Modifier.config(state="disabled")
        self.btn_Supprimer.config(state="disabled")
        self.var_emplo_id.set("")     
        self.var_nom_complet.set(""),
        self.var_email.set(""),
        self.var_sexe.set("Homme"),
        self.var_contact.set(""),
        self.var_naissance.set(""),
        self.var_adhesion.set(""),
        self.var_pasword.set(""),
        self.var_type.set("Admin"),
        self.txt_empadresse.delete("1.0",END),
        self.var_salaire.set(""),
        self.var_fonction.set(""),
        self.var_recherche_txt.set(""),
        self.var_recherche_type.set("Nom")
       
    #  fonction pour recherche   
    def recherche(self):
        conn =sqlite3.connect(database=r"C:\Users\USER\Desktop\mon_deuxieme_project\donnee\magasinbase.bd")
        curseur=conn.cursor()
        try:     
            if self.var_recherche_txt.get()=="":
                   messagebox.showerror("Erreur","veuillez saisir dans le champs recherche")
            else:
                   curseur.execute("select * from employe where "+self.var_recherche_type.get()+" LIKE '%"+self.var_recherche_txt.get()+"%'")
                   rows= curseur.fetchall()
                   if len(rows)!=0:
                        self.employeliste.delete(*self.employeliste.get_children())
                        for row in rows: 
                            self.employeliste.insert("",END,values=row)
                   else:
                        messagebox.showerror("Resultat","aucun resultat trouvé")
                                        
        except Exception as eror:
                 messagebox.showerror("erreur", f" erreurde connection {str(eror)}")         
                  
if __name__=="__main__":
    root= Tk()
    obj= employe(root)
    root.mainloop()
