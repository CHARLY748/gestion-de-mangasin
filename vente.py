from tkinter import *
from PIL import Image, ImageTk 
import os
from tkinter import messagebox
import time


class vente:
    def __init__(self,root):
        self.root=root
        self.root.title("vente")
        self.root.geometry("1000x480+350+100")
        self.root.config(bg="white")
        self.root.focus_force()

        self.varnumero_facture=StringVar()
        self.list_facture= []

      ###LE TITTRE
        title= Label(self.root,text="consulter la facture des clients",font=("goudy old style",20,"bold "),bg="blue",bd=3,relief=RIDGE)
        title.pack(side=TOP,fill=X,padx=10,pady=10)

       # LES LABEL
        label_num_facture= Label(self.root,text="Numero Facture",font=("times new roman",20),bg="white")
        label_num_facture.place(x=10,y=80)
        txt_num_facture = Entry(self.root,textvariable=self.varnumero_facture,font=("times new roman",20),bg="lightyellow")
        txt_num_facture.place(x=200,y=80,width=190)

        ###LES BOUTTON
        btn_recherche=Button(self.root,command=self.recherche,text="Rechercher",font=("times new roman",20,"bold"),bg="lightgray",cursor="hand2")
        btn_recherche.place(x=395,y=80,width=150,height=35)

        btn_Renitialise=Button(self.root,command=self.reni,text="Renitialiser",font=("times new roman",20,"bold"),bg="green",cursor="hand2")
        btn_Renitialise.place(x=550,y=80,width=150,height=35)
        
        btn_voir=Button(self.root,text="consulter la caisse",command=self.voirCaisse ,cursor="hand2",activebackground="white",font=("alegerian",20,"bold"),bg="white",fg="green")
        btn_voir.place(x=710,y=80,width=280,height=35)
         # LISTE VENTE
        vente_frame=Frame(self.root,bd=3,relief=RIDGE)
        vente_frame.place(x=10,y=120,height=350,width=242)
        
        scroll_y=Scrollbar(vente_frame,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=Y)

        self.list_ventes=Listbox(vente_frame,font=("goudy old style",18),bg="white",yscrollcommand=scroll_y.set)
        scroll_y.config(command=self.list_ventes.yview)
        self.list_ventes.pack(fill=BOTH, expand=1)
        self.list_ventes.bind("<ButtonRelease-1>",self.recupereDonnee)

        ###ESPACE FACTURE
        facture_frame =Frame(self.root,bd=3,relief=RIDGE)
        facture_frame.place(x=250,y=120,height=350,width=450)

        titre=Label(facture_frame,text="Facture du Client",font=("goudy old style",20),bg="orange")
        titre.pack(side=TOP,fill=X)

        scroll_y2=Scrollbar(facture_frame,orient=VERTICAL)
        scroll_y2.pack(side=RIGHT,fill=Y)
        self.espacefacture=Text(facture_frame,font=("goudy old style",12),bg="lightyellow",yscrollcommand=scroll_y2.set)
        scroll_y2.config(command=self.espacefacture.yview)
        self.espacefacture.pack(fill=BOTH, expand=1)

        #### image facture
        self.imagefacture= Image.open(r"C:\Users\USER\Desktop\mon_deuxieme_project\image\facture6.jpg")
        self.imagefacture=self.imagefacture.resize((290 ,343))
        self.imagefacture=ImageTk.PhotoImage(self.imagefacture)

        label_image=Label (self.root,image=self.imagefacture)
        label_image.place(x=700,y=122)

        self.afficher()


        #foncion pour voir la caisse
    def voirCaisse(self):
        self.obj=os.system("python3.11.exe c:/Users/USER/Desktop/mon_deuxieme_project/caisse.py")  
             

    def afficher(self):
        del self.list_facture[:]    
        self.list_ventes.delete(0,END)
        for i in os.listdir(r"C:\Users\USER\Desktop\mon_deuxieme_project\facture"):
            if i.split(".")[-1]=="txt":
                self.list_ventes.insert(END,i)
                self.list_facture.append(i.split(".")[0])

    def recupereDonnee(self,ev):
        index =self.list_ventes.curselection()
        nomFicher=self.list_ventes.get(index)
        ficherOuvert= open(fr"C:\Users\USER\Desktop\mon_deuxieme_project\facture\{nomFicher}","r")
        self.espacefacture.delete("1.0",END)
        for i in ficherOuvert:
            self.espacefacture.insert(END,i)
        ficherOuvert.close()   

    def recherche(self):
        if self.varnumero_facture.get()=="":
            messagebox.showerror("Erreur","Donnez le numero de Facture")
        else:
            if self.varnumero_facture.get() in self.list_facture:
                ficherOuvert= open(fr"C:\Users\USER\Desktop\mon_deuxieme_project\facture\{self.varnumero_facture.get()}.txt","r")
                self.espacefacture.delete("1.0",END)
                for i in ficherOuvert:
                    self.espacefacture.insert(END,i)
                ficherOuvert.close()
            else:messagebox.showerror("Erreur","le Numero de facture n'existe pas") 


        
    def reni(self):
        self.afficher()
        self.espacefacture.delete("1.0",END)
        self.varnumero_facture.set("")        





        




if __name__=="__main__":
    root= Tk()
    obj= vente(root)
    root.mainloop()
