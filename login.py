from tkinter import *
from PIL import Image, ImageTk 
import os
from tkinter import messagebox
import time
import sqlite3
import smtplib
import email_pass

class login:
    def __init__(self,root):
        self.root=root
        self.root.title("connexion")
        self.root.geometry("1000x680+170+0")
        self.root.config(bg="white")
        self.root.focus_force()

        self.code_envoie= ""

         ### LE LOGIN AVEC SES LABEL ET SES ENTRY
        loginframe=Frame(self.root,bg="lightblue")
        loginframe.place(x=300,y=130,width=400,height=400)

        titre = Label(loginframe,text="Se Connecté",font=("Algerian",40,),bg="lightblue",fg="blue")
        titre.pack(side=TOP,fill=X)

        labelId=Label(loginframe,text="Identifiant",font=("times new roman",20,"bold"),bg="lightblue")
        labelId.place(x=130,y=70)

        labelMotPasse=Label(loginframe,text="Mot de Passe",font=("times new roman",20,"bold"),bg="lightblue")
        labelMotPasse.place(x=130,y=170)

        self.txtIdentifiant=Entry(loginframe,font=("times new roman",20),bg="lightgray")
        self.txtIdentifiant.place(x=60,y=110)

        self.txtmoPasse=Entry(loginframe,show='*',font=("times new roman",20),bg="lightgray")
        self.txtmoPasse.place(x=60,y=210)

        connecterBtn=Button(loginframe,command=self.connexion,text="Connexion",font=("times new roman",20,"bold"),cursor="hand2",bg="lightgray",activebackground="lightblue",bd=5,fg="green")
        connecterBtn.place(x=120,y=260,height=50)
        
        oulieBtn=Button(loginframe,command=self.password_oublié_fenetre,text="Mot de passe oublié",cursor="hand2",font=("times new roman",15),bg="lightblue",activebackground="lightblue",bd=0,fg="red")
        oulieBtn.place(x=190,y=350)

###     GESTION DU MOT DE PASSE OUBLIE
    def password_oublié_fenetre(self):
            if self.txtIdentifiant.get()=="":
                 messagebox.showerror("Erreur","Veuillez saisir votre identifiant")
            else: 
                conn =sqlite3.connect(database=r"C:\Users\USER\Desktop\mon_deuxieme_project\donnee\magasinbase.bd")
                curseur=conn.cursor()  
                try:
                    curseur.execute("select email from employe where ID=?",(self.txtIdentifiant.get(),))
                    email=curseur.fetchone()
                    if email==None:
                         messagebox.showerror("Erreur","l'identifiant n'existe pas") 
                    else:
                        chk = self.envoieMail(email[0])
                        if chk=='f':
                              messagebox.showerror("Erreur","Erreur de connection ou email introuvable")
                        else:
                             self.varCode = StringVar()
                             self.varNewPass = StringVar()
                             self.varConfirmePass = StringVar()

                             self.root2 = Toplevel()
                             self.root2.title("Rénitialiser mot de passe")
                             self.root2.config(bg="white")
                             self.root2.geometry("400x430+470+100")
                             self.root2.focus_force()
                             self.root2.grab_set()

                             title=Label(self.root2,text="Recupéré le Mot de Passe",font=("algerian",20,"bold"),bg="gray")
                             title.pack(side=TOP,fill=X)

                             # champ de saisi du code recu dans la boite mail
                             afficheCode = Label(self.root2,text="Saisissez le code recu par mail",font=("times new roman",15,"bold"),bg="white")
                             afficheCode.place(x=70,y=50)

                             txt_reset=Entry(self.root2,textvariable=self.varCode,font=("times new roman",20,"bold"),bg="lightgray")
                             txt_reset.place(x=90,y=100,width=190)

                             self.codeBtn= Button(self.root2,command=self.codeValide,text="Valider",cursor="hand2",font=("times new roman",20,"bold"),bg="lightgray",bd=3,fg="green")
                             self.codeBtn.place(x=290,y=98,height=35,width=100)

                             #nouveau mot de passe
                             nouveauPasse=Label(self.root2,text="Nouveau Mot de Passe",font=("times new roman",15,"bold"),bg="white")
                             nouveauPasse.place(x=70,y=150)

                             comfimerPasse=Label(self.root2,text="Comfimer le Mot de passe",font=("times new roman",15,"bold"),bg="white")
                             comfimerPasse.place(x=70,y=250)

                             txt_passe=Entry(self.root2,textvariable=self.varNewPass,font=("times new roman",20,"bold"),bg="lightgray")
                             txt_passe.place(x=90,y=200,width=200)

                             txt_comfirmepasse=Entry(self.root2,textvariable=self.varConfirmePass,font=("times new roman",20,"bold"),bg="lightgray")
                             txt_comfirmepasse.place(x=90,y=300,width=200)

                             ##modifier mot de passe
                             self.changerBtn= Button(self.root2,text="Modifier",cursor="hand2",command=self.modifier,font=("times new roman",20,"bold"),state="disabled",bg="lightgreen",bd=3)
                             self.changerBtn.place(x=120,y=350,height=35,width=150)
                                    
                except Exception as eror:
                    messagebox.showerror("erreur", f" erreurde connection {str(eror)}")  
     # modifier mot de passe
    def modifier(self):
        if self.varNewPass.get()=="" or self.varConfirmePass.get()=="":
             messagebox.showerror("Erreur","Veuillez saisir votre mot de passe")
        elif self.varNewPass.get()!=self.varConfirmePass.get():  
             messagebox.showerror("Erreur","les mots de passes doivent être identique") 
        else:
            try:
                conn =sqlite3.connect(database=r"C:\Users\USER\Desktop\mon_deuxieme_project\donnee\magasinbase.bd")
                curseur=conn.cursor()
                curseur.execute("UPDATE employe SET password=? WHERE ID=?", (self.varNewPass.get(), self.txtIdentifiant.get(),))

                conn.commit()
                messagebox.showinfo("succes","mot de passe modifier avec succes")
                self.root2.destroy()
            except Exception as eror:
                 messagebox.showerror("erreur", f" erreurde connection {str(eror)}")    
                
                                                  

     # FONCTION POUR VERIFIER QUE LE CODE EST VALIDE
    def codeValide(self):
        if int(self.code_envoie)==int(self.varCode.get()):
            self.changerBtn.config(state="normal")
            self.codeBtn.config(state="disabled")
        else:
             messagebox.showerror("Erreur","code Invalide")    


    # CETTE FONCTION PERMET D'ENVOYE UN MAIL
    def envoieMail(self,send) :
         s = smtplib.SMTP("smtp.gmail.com",587)
         s.starttls()
         email_ =email_pass.email_
         pass_ =email_pass.pass_
         s.login(email_,pass_)
         self.code_envoie = time.strftime("%H%S%M") + time.strftime("%S")


         subj = "Magasin Charly Design Code de Renitialisation Mot de Passe"
         msg =f"Bonjour Monsieur/Madame\nVotre code de renitialisation est: {self.code_envoie}\nMercie pour la confiance du service "
         msg="Subject{}\n{}".format(subj,msg)
         s.sendmail(email_,send ,msg)
         chk =s.ehlo()
         if chk[0]== 250:
              return 's'
         else:
              return 'f'  

         

    def connexion(self):
        conn =sqlite3.connect(database=r"C:\Users\USER\Desktop\mon_deuxieme_project\donnee\magasinbase.bd")
        curseur=conn.cursor()
        try:
            if self.txtIdentifiant.get()=="" or self.txtmoPasse.get()=="":
                messagebox.showerror("Ereuur", "veuillez saisir l'Identifiant et le Mot de passe")
            else:   
                  curseur.execute("select type from employe where ID=? AND password=?",(self.txtIdentifiant.get(),self.txtmoPasse.get())) 
                  user= curseur.fetchone()
                  if user==None:
                       messagebox.showerror("Erreur","l'itantifiant ou le mot de passe n'existe pas")
                  else:
                       if user[0]=="Admin":
                            self.root.destroy() 
                            os.system("python3.11.exe c:/Users/USER/Desktop/mon_deuxieme_project/acceuille.py") 
                       else:
                            os.system("python3.11.exe c:/Users/USER/Desktop/mon_deuxieme_project/caisse.py") 
                                 
        except Exception as eror:
                 messagebox.showerror("erreur", f" erreurde connection {str(eror)}")

             
                     

if __name__=="__main__":
    root= Tk()
    obj= login(root)
    root.mainloop()
