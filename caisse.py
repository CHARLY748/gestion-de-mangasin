from tkinter import *
from PIL import Image, ImageTk 
import os
import pygetwindow as gw
from tkinter import messagebox,ttk
from tkinter import simpledialog
import time
import sqlite3
import tempfile



class caisse:
    def __init__(self,root):
        self.root=root
        self.root.title("caisse")
        self.root.geometry("1360x690+0+0")
        self.root.config(bg="white")
        self.root.focus_force()




        conn =sqlite3.connect(database=r"C:\Users\USER\Desktop\mon_deuxieme_project\donnee\magasinbase.bd")
        curseur=conn.cursor()
        curseur.execute("""CREATE TABLE IF NOT EXISTS vente(ID text INTEGER PRIMARY KEY,client_nom text,client_nom, client_contact text, montant_total text,
                              remise text, montant_paye text, date_vente text)""")
        conn.commit()

        conn =sqlite3.connect(database=r"C:\Users\USER\Desktop\mon_deuxieme_project\donnee\magasinbase.bd")
        curseur=conn.cursor()
        curseur.execute("""CREATE TABLE IF NOT EXISTS vente_produit(ID text INTEGER PRIMARY KEY,vente_id text, produit_id text, quantite_vendue text)""")
        conn.commit()



        titre = Label(self.root,text="La Caisse",font=( "times new roman",30,"bold"), bg="BLUE",anchor="w",
                      padx=20,compound=LEFT).place(x=0, y=0 ,relwidth=1, height=50 )
        # Boutton deconecté
        btn_decon= Button(self.root,command=self.deconecté, text="Déconnecté",font=( "times new roman",20,"bold"),
                          cursor="hand2",bg="orange").place(x=1205,y=5,height=40)
        # HEURE
        self.label_heure=Label(self.root,text="Bienvenue chez charly Design\t\t Date:DD-MM-YYYY\t\t Heure:HH:MM:SS",
                               font=( "times new roman",15,"bold"),bg="black",fg="white")
        self.label_heure.place(x=0, y=50 ,relwidth=1, height=40 )
        self.heure()

        # produit

        produitframe1=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        produitframe1.place(x=5,y=90,width=520,height=550)

        ptitre=Label(produitframe1,text="Tous les Produits",font=("goudy old style",25,"bold"),bg="blue",bd=2,relief=RIDGE)
        ptitre.pack(side=TOP,fill=X)

        produitframe2=Frame(produitframe1,bd=2,relief=RIDGE,bg="white")
        produitframe2.place(x=5,y=45,width=503,height=100)

        # recherche
        label_recherche=Label(produitframe2,text="Recherche Produits par Nom(Marque)",font=("goudy old style",17,"bold"),fg="Black",bg="white",bd=2,relief=RIDGE)
        label_recherche.place(x=50,y=5)

        label_nom=Label(produitframe2,text="Nom Produit",font=("goudy old style",16,"bold"),bg="white")
        label_nom.place(x=0,y=60)

        self.var_recherche=StringVar()
        self.var_clnom=StringVar()
        self.var_clcontact=StringVar()

        label_recherche=Entry(produitframe2,textvariable=self.var_recherche,font=("goudy old style",15,"bold"),bg="lightyellow")
        label_recherche.place(x=121,y=60,width=166,height=35)

        recherche_btn=Button(produitframe2,command=self.recherche,text="Recherche",font=("times new roman",16,"bold"),fg="white",bg="GREEN")
        recherche_btn.place(x=290,y=60,width=105,height=35)

        affiche_btn=Button(produitframe2,text="afficher",command=self.afficher,font=("times new roman",17,"bold"),fg="white",bg="BLUE")
        affiche_btn.place(x=399,y=60,width=100,height=35)

                 # liste des produits
        produitframe3=Frame(produitframe1,bd=3,relief=RIDGE)
        produitframe3.place(x=2,y=145,height=245,relwidth=1)
        
        scroll_y=Scrollbar(produitframe3,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x=Scrollbar(produitframe3,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)
        
        self.produit_table=ttk.Treeview(produitframe3,columns=("ID","nom","prix","quantite","status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.config(command=self.produit_table.xview)
        scroll_y.config(command=self.produit_table.yview)
        
        self.produit_table.heading("ID",text="ID",anchor="w")
        self.produit_table.heading("nom",text="Nom Produit",anchor="w")
        self.produit_table.heading("prix",text="Prix",anchor="w")
        self.produit_table.heading("quantite",text="Quantite",anchor="w")
        self.produit_table.heading("status",text="status",anchor="w")
        
        
        self.produit_table.column("ID",width=60)
        self.produit_table.column("quantite",width=120)
        self.produit_table.column("prix",width=150)
        self.produit_table.column("status",width=100)
        self.produit_table.column("nom",width=180)

        
        self.produit_table["show"]="headings"
        self.produit_table.pack(fill=BOTH,expand=1)
        self.produit_table.bind("<ButtonRelease-1>",self.get_donne) 
        self.afficher()

        label_note=Label(produitframe1,text="A savoir: 'Entrez 0 pour retirer le produit du panier'",anchor="w",font=( "times new roman",15),bg="white",fg="red")
        label_note.place(x=2,y=390)

        #frame pour client

        client_frame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        client_frame.place(x=525,y=90,width=440,height=90)   
        cltitre=Label(client_frame,text="Details du Client",font=("goudy old style",20,"bold"),bg="orange",bd=3,relief=RIDGE)
        cltitre.pack(side=TOP,fill=X) 

        label_nom=Label(client_frame,text="Nom",font=("goudy old style",16),bg="white")
        label_nom.place(x=0,y=40) 
        txt_nom=Entry(client_frame,textvariable=self.var_clnom,font=("goudy old style",16),bg="lightyellow")
        txt_nom.place(x=50,y=45,width=145,height=35) 

        label_contact=Label(client_frame,text="Contact",font=("goudy old style",16),bg="white")
        label_contact.place(x=195,y=40) 
        txt_contact=Entry(client_frame,textvariable=self.var_clcontact,font=("goudy old style",16),bg="lightyellow")
        txt_contact.place(x=272,y=45,width=135,height=35) 

        # la calculatrice
        self.var_cal_input=StringVar()

         #FRAME GLOBAL DE LA CALCULATRICE
        calcul_cart_frame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        calcul_cart_frame.place(x=525,y=180,width=440,height=460)
        #FRAME A DROITE DE LA CALCULATRICE
        calcul_frame=Frame(calcul_cart_frame,bd=4,relief=RIDGE,bg="white")
        calcul_frame.place(x=5,y=10,width=239,height=400)

        self.txt_cal_input=Entry(calcul_frame,textvariable=self.var_cal_input,font=("arial",15,"bold"),justify=RIGHT,bg="lightgray",bd=4,state="readonly")
        self.txt_cal_input.grid(row=0,columnspan=4)
        
        #BOUTTON POUR LES CHIFFRES
        self.btn_7=Button(calcul_frame,text="7",font=("arial",15,"bold"),cursor="hand2",width=4,pady=25,command=lambda:self.get_input(7)).grid(row=1,column=0)
        self.btn_8=Button(calcul_frame,text="8",font=("arial",15,"bold"),cursor="hand2",width=4,pady=25,command=lambda:self.get_input(8)).grid(row=1,column=1)
        self.btn_9=Button(calcul_frame,text="9",font=("arial",15,"bold"),cursor="hand2",width=4,pady=25,command=lambda:self.get_input(9)).grid(row=1,column=2)
        self.btn_add=Button(calcul_frame,text="+",font=("arial",15,"bold"),cursor="hand2",width=4,pady=25,command=lambda:self.get_input("+")).grid(row=1,column=3)
 
        self.btn_4=Button(calcul_frame,text="4",font=("arial",15,"bold"),cursor="hand2",width=4,pady=25,command=lambda:self.get_input(4)).grid(row=2,column=0)
        self.btn_5=Button(calcul_frame,text="5",font=("arial",15,"bold"),cursor="hand2",width=4,pady=25,command=lambda:self.get_input(5)).grid(row=2,column=1)
        self.btn_6=Button(calcul_frame,text="6",font=("arial",15,"bold"),cursor="hand2",width=4,pady=25,command=lambda:self.get_input(6)).grid(row=2,column=2)
        self.btn_sous=Button(calcul_frame,text="-",font=("arial",15,"bold"),cursor="hand2",width=4,pady=25,command=lambda:self.get_input("-")).grid(row=2,column=3)
 
        self.btn_1=Button(calcul_frame,text="1",font=("arial",15,"bold"),cursor="hand2",width=4,pady=25,command=lambda:self.get_input(1)).grid(row=3,column=0)
        self.btn_2=Button(calcul_frame,text="2",font=("arial",15,"bold"),cursor="hand2",width=4,pady=25,command=lambda:self.get_input(2)).grid(row=3,column=1)
        self.btn_3=Button(calcul_frame,text="3",font=("arial",15,"bold"),cursor="hand2",width=4,pady=25,command=lambda:self.get_input(3)).grid(row=3,column=2)
        self.btn_mul=Button(calcul_frame,text="*",font=("arial",15,"bold"),cursor="hand2",width=4,pady=25,command=lambda:self.get_input("*")).grid(row=3,column=3)

        self.btn_0=Button(calcul_frame,text="0",font=("arial",15,"bold"),cursor="hand2",width=4,pady=25,command=lambda:self.get_input(0)).grid(row=4,column=0)
        self.btn_c=Button(calcul_frame,text="c",font=("arial",15,"bold"),cursor="hand2",width=4,pady=25,command=self.clear_cal).grid(row=4,column=1)
        self.btn_egal=Button(calcul_frame,text="=",font=("arial",15,"bold"),cursor="hand2",width=4,pady=25,command=self.resultat).grid(row=4,column=2)
        self.btn_div=Button(calcul_frame,text="/",font=("arial",15,"bold"),cursor="hand2",width=4,pady=25,command=lambda:self.get_input("/")).grid(row=4,column=3)
        

        cart_frame=Frame(calcul_cart_frame,bd=3,relief=RIDGE)
        cart_frame.place(x=240,y=10,height=400,width=193)

        self.cltitle=Label(cart_frame,text="Total des Produits :[0]",font=("times new roman",11,"bold"),bg="orange",bd=3,relief=RIDGE)
        self.cltitle.pack(side=TOP,fill=X) 

                  # liste des produits
        scroll_y=Scrollbar(cart_frame,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x=Scrollbar(cart_frame,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)
        
        self.carttable=ttk.Treeview(cart_frame,columns=("ID","nom","prix","quantite","status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.config(command=self.carttable.xview)
        scroll_y.config(command=self.carttable.yview)
        
        self.carttable.heading("ID",text="ID",anchor="w")
        self.carttable.heading("nom",text="Nom Produit",anchor="w")
        self.carttable.heading("prix",text="Prix",anchor="w")
        self.carttable.heading("quantite",text="Quantite",anchor="w")
        self.carttable.heading("status",text="status",anchor="w")
        
        
        self.carttable.column("ID",width=60)
        self.carttable.column("nom",width=180)
        self.carttable.column("prix",width=150)
        self.carttable.column("quantite",width=120)
        self.carttable.column("status",width=100)
        
        self.carttable["show"]="headings"
        self.carttable.pack(fill=BOTH,expand=1)
        self.carttable.bind("<ButtonRelease-1>",self.get_donne_cart) 

        #ajouter les bouton
        #les variables
        self.varid=StringVar()
        self.varname=StringVar()
        self.varprix=StringVar()
        self.varqte=StringVar()
        self.varstock=StringVar()
        self.var_recherche=StringVar()
        self.cart_list=[]
        self.ck_print=0
        
       # framme que jai mis en bas DE LA CALCULATRICE
        Button_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        Button_Frame.place(x=5,y=510,width=520,height=130)
        #le nom du produit
        label_prod_nom=Label(Button_Frame,text="Nom Produit",font=("goudy old style",15),bg="white")
        label_prod_nom.place(x=0,y=0)
        txt_prod_nom=Entry(Button_Frame,font=("goudy old style",15),textvariable=self.varname,bg="lightgray",state="readonly")
        txt_prod_nom.place(x=5,y=40,width=160,height=35)
         #le prix du produit
        label_prod_prix=Label(Button_Frame,text="Prix Produit",font=("goudy old style",15),bg="white")
        label_prod_prix.place(x=180,y=5)
        txt_prod_prix=Entry(Button_Frame,font=("goudy old style",15),textvariable=self.varprix,bg="lightgray",state="readonly")
        txt_prod_prix.place(x=180,y=40,width=120,height=35)
        #la quantité  du produit
        label_prod_qte=Label(Button_Frame,text="Quantité",font=("goudy old style",15),bg="white")
        label_prod_qte.place(x=310,y=5)
        txt_prod_qte=Entry(Button_Frame,font=("goudy old style",15),textvariable=self.varqte,bg="lightyellow")
        txt_prod_qte.place(x=315,y=40,width=100,height=35)

        self.label_prod_stock=Label(Button_Frame,text="Le stock",font=("goudy old style",15),bg="white")
        self.label_prod_stock.place(x=0,y=90)

        #les boutton
        self.renitialiser_btn=Button(Button_Frame,command=self.reni_cart,text="Renitialiser",font=("times new roman",15,"bold"),cursor="hand2",bg="green",state="normal",bd=3)
        self.renitialiser_btn.place(x=135,y=80,width=110,height=40)

        self.ajoutmodif_btn=Button(Button_Frame,command=self.ajouter_modifier,text="Ajouter | Modifier",font=("times new roman",15,"bold"),cursor="hand2",bg="orange",state="normal",bd=3)
        self.ajoutmodif_btn.place(x=250,y=80,width=170,height=40)
        #DERNIERE FRAME
        facture_frame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        facture_frame.place(x=965,y=90,width=390,height=420)

        ctitle=Label(facture_frame,text="Facture client",font=("goudy old style",20),bd=3,relief=RIDGE)
        ctitle.pack(side=TOP,fill=X)

        scroll_y=Scrollbar(facture_frame,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=Y)

        self.txt_espace_facture=Text(facture_frame,yscrollcommand=scroll_x.set)
        self.txt_espace_facture.pack(fill=BOTH,expand=1)
        scroll_y.config(command=self.txt_espace_facture.yview)

        ##BOUTTON
        factureMenuFame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        factureMenuFame.place(x=965,y=510,width=390,height=130)

        self.labelMontantFacture= Label(factureMenuFame,text="Montant\n[0]",font=("goudy old style",15),bg="blue",fg="white")
        self.labelMontantFacture.place(x=0,y=5,width=120,height=60)


        self.labelRemiseFacture= Label(factureMenuFame,text="Remise\n[0]",font=("goudy old style",15),bg="red",fg="white")
        self.labelRemiseFacture.place(x=125,y=5,width=120,height=60)

        self.labelMontantAPayé= Label(factureMenuFame,text="A Payé\n[0]",font=("goudy old style",15),bg="green",fg="white")
        self.labelMontantAPayé.place(x=250,y=5,width=130,height=60)

      #   self.labelMontantJour= Label(factureMenuFame,text="Total du jour[0]",font=("goudy old style",15),bg="green",fg="white")
      #   self.labelMontantJour.place(x=150,y=5,width=130,height=60)


        btn_imprimer=Button(factureMenuFame,command=self.Imprimer_facture,text="Imprimer",font=("goudy old style",20),bg="gray",bd=5,cursor="hand2",fg="white")
        btn_imprimer.place(x=0,y=70,width=120,height=50)

        btn_generer_facture=Button(factureMenuFame,command=self.genere_facture,text="Générer",font=("goudy old style",20),bg="blue",bd=5,cursor="hand2",fg="white")
        btn_generer_facture.place(x=125,y=70,width=120,height=50)

        btn_renitialiser=Button(factureMenuFame,command=self.reniall,text="Renitialiser",font=("goudy old style",20),bg="orange",cursor="hand2",bd=5,fg="white")
        btn_renitialiser.place(x=250,y=70,width=133,height=50)

                # pied de page ou flooter
        label_footer=Label(self.root,text="Developper par charles kagambega\t\tcharleskagambega5@gmail.com\t\t+22664150340\t\tcopyright 2024",
        font=( "times new roman",16,"bold"),bg="black",fg="white").pack(side=BOTTOM,fill=X)

#      FONCTION POUR GERE LA CALCULATRICE ET RECUPERE LES DONNEES SAISI

        #fonction pour recupere les chiffres saisi
    def get_input(self,num):
        xnum=self.var_cal_input.get()+str(num)
        self.var_cal_input.set(xnum)

        #fonction pour renitialiser les chiffres saisi
    def clear_cal(self):
        self.var_cal_input.set("")

         #fonction pour afficher le resultats
    def resultat(self):
        resultat=self.txt_cal_input.get()
        self.var_cal_input.set(eval(resultat))

     #afficher au niveau du Treeview
    def afficher(self):
        conn =sqlite3.connect(database=r"C:\Users\USER\Desktop\mon_deuxieme_project\donnee\magasinbase.bd")
        curseur=conn.cursor()
        try:
                curseur.execute("select ID, nom,prix,quantite,status from produit where status='Active'")
                rows = curseur.fetchall()
                self.produit_table.delete(*self.produit_table.get_children())
                for row in rows:
                        self.produit_table.insert("",END,values=row)      
        except Exception as eror:
                 messagebox.showerror("erreur", f" erreurde connection {str(eror)}")   

    def recherche(self):
        conn =sqlite3.connect(database=r"C:\Users\USER\Desktop\mon_deuxieme_project\donnee\magasinbase.bd")
        curseur=conn.cursor()
        try:
              if self.var_recherche.get()=="":
                   messagebox.showerror("Erreur","Qu'est ce que vous recherchez?")
              else:
                    curseur.execute("select ID, nom,prix,quantite,status from produit where nom LIKE '%"+self.var_recherche.get()+"%'and status='Active'") 
                    rows=curseur.fetchall()
                    if len(rows)!=0:
                            self.produit_table.delete(*self.produit_table.get_children())
                            for row in rows: 
                                    self.produit_table.insert("",END,values=row)
                    else:
                          messagebox.showerror("Erreur","aucun resultat")

        except Exception as eror:
                 messagebox.showerror("erreur", f" erreurde connection {str(eror)}")
    
    def get_donne (self, ev):
            r = self.produit_table.focus()
            contenu=self.produit_table.item(r)
            row = contenu["values"]
            self.varid.set(row[0]),        
            self.varname.set(row[1]),
            self.varprix.set(row[2]),
            self.label_prod_stock.config(text=f"En stock[{str(row[3])}]"),
            self.varstock.set(row[3])
            self.varqte.set(1)
    
    def get_donne_cart (self, ev):
            r = self.carttable.focus()
            contenu=self.carttable.item(r)
            row = contenu["values"]
            self.varid.set(row[0]),        
            self.varname.set(row[1]),
            self.varprix.set(row[2]),
            self.varqte.set(row[3]),
            self.label_prod_stock.config(text=f"En stock[{str(row[4])}]"),
            self.varstock.set(row[4])

    def ajouter_modifier(self):
          if self.varid.get()=="":
                messagebox.showerror("erreur","Selectionné un produit")
          elif self.varqte.get=="":
                 messagebox.showerror("erreur","Donner la quantité du produit")
          elif int(self.varqte.get()) > int(self.varstock.get()):
                 messagebox.showerror("erreur","Quantité indisponible")
          else:
                prix_cal=self.varprix.get()
                cart_donne=[self.varid.get(),self.varname.get(),self.varprix.get(),self.varqte.get(),self.varstock.get()]

                present="nom"
                index_=0
                for row in self.cart_list:
                      if self.varid.get()==row[0]:
                            present="oui"
                            break
                      index_+=1
                if present=="oui":
                      op=messagebox.askyesno("comfirmer","le produit est present\n voulez vous vraiment modifier|supprimer de la liste?")
                      if op==TRUE:
                            if self.varqte.get()=="0":
                                  self.cart_list.pop(index_)
                            else:
                                  self.cart_list[index_][3]=self.varqte.get()
                else:
                      self.cart_list.append(cart_donne)
                self.afficher_cart()
                self.facture_modifier()

    def afficher_cart(self):
          try:
                    
            self.carttable.delete(*self.carttable.get_children())
            for row in self.cart_list: 
                self.carttable.insert("",END,values=row) 

          except Exception as eror:
                 messagebox.showerror("erreur", f" erreurde connection {str(eror)}")            

    def facture_modifier(self):
          self.montant_facture =0
          self.net_a_payer =0
          self.remise =0
          self.totaJour=0
          for row in self.cart_list:
                self.montant_facture = self.montant_facture + (float(row[2])*int(row[3]))
          self.remise = (self.montant_facture * 5)/100
          self.net_a_payer = self.montant_facture - self.remise
          self.totaJour=self.net_a_payer

          self.labelMontantFacture.config(text=f"Montant\n[{str(self.montant_facture)}]")
          self.labelMontantAPayé.config(text=f"A Payé\n[{str(self.net_a_payer)}]") 
          self.labelRemiseFacture.config(text=f"Remise\n[{str(self.remise)}]") 
          self.cltitle.config(text=f"Total des Produits :[{str(len(self.cart_list))}]") 
         
      #     self.labelMontantJour.config(text=f"Total du jour[{str(self.totaJour)}]")      
                   

    def genere_facture(self):
          if self.var_clnom.get()=="" or self.var_clcontact.get()=="":
                messagebox.showerror("Erreur","veuillez entrez le  nom et le contact  du client")
             
          elif len(self.cart_list)==0:
                messagebox.showerror("Erreur","veuillez ajouter le produits dans la liste")
          else:
                self.entete_facture()
                self.corp_facture()
                self.footer_facture()
                fp = open(fr"C:\Users\USER\Desktop\mon_deuxieme_project\facture\{str(self.facture)}.txt","w")
                fp.write(self.txt_espace_facture.get("1.0",END))
                fp.close
                messagebox.showinfo("sauvegarde","Generer avec succes")
                self.ck_print =1
          if self.ck_print == 1:          
              self.enregistrer_vente()
             


    def entete_facture(self):
          self.facture =int(time.strftime("%H%M%S"))+int(time.strftime("%d%m%Y"))
          facture_entete = f'''
\tmagasin charly design \n Tel : +226 64-15-03-40/79-73-42-96 \n Adresse : Ouagadougou/Tanghin
{str( " "*45)}
{str( "="*45)}
 Nom du client  : {self.var_clnom.get()}
 Tel du client  : {self.var_clcontact.get()}   
 Numero facture : {str(self.facture)}
 Date :{str(time.strftime("%d/%m/%Y"))}
{str( "="*45)} 
 Nom Produit \t      Quantité\t\t  Prix
{str( "="*45)}
          '''  
          self.txt_espace_facture.delete("1.0",END)
          self.txt_espace_facture.insert("1.0",facture_entete)      

    def corp_facture(self):
        conn =sqlite3.connect(database=r"C:\Users\USER\Desktop\mon_deuxieme_project\donnee\magasinbase.bd")
        curseur=conn.cursor()  
        try:
              for row in self.cart_list:
                    ID= row[0]
                    nom=row[1]
                    quantité=int(row[4])-int(row[3])
                    if int(row[3])==int(row[4]):
                          status="Inactive"
                    if int(row[3])!=int(row[4]):
                          status="Active"
                    prix = float(row[2])*float(row[3])  
                    prix = str(prix)     
                    self.txt_espace_facture.insert(END, "\n "+nom+"\t\t\t"+row[3]+"\t"+prix) 
                    curseur.execute("update produit set quantite=?,status=? WHERE ID=?",(
                          quantité,
                          status,
                          ID
                    ))    
                    conn.commit()
              conn.close() 
              self.afficher()

        except Exception as eror:
                 messagebox.showerror("erreur", f" erreurde connection {str(eror)}")  

    def  footer_facture(self):
          facture_flooter=f'''
{str( "="*45)} 
 Montant Facture : \t\t\t\t{self.montant_facture}
 Remise : \t\t\t\t{self.remise}
 Total : \t\t\t\t{self.net_a_payer}
{str( "="*45)}
          '''    
          self.txt_espace_facture.insert(END,facture_flooter)                   
                              

    def reni_cart(self):
          self.varid.set("") 
          self.varname.set("")  
          self.varprix.set("")  
          self.varqte.set("")  
          self.label_prod_stock.config(text=f"Le stock")
          self.varstock.set("")


    def reniall(self):
          del self.cart_list[:]
          self.var_clnom.set("")
          self.var_clcontact.set("")
          self.txt_espace_facture.delete("1.0",END)
          self.cltitle.config(text=f"Total des Produits :[0]")
          self.var_recherche.set("")
          self.labelMontantFacture.config(text=f"Montant\n[0]")
          self.labelMontantAPayé.config(text=f"A Payé\n[0]") 
          self.labelRemiseFacture.config(text=f"Remise\n[0]") 
          self.ck_print =0
          self.reni_cart()
          self.afficher_cart()

                                                        
    def Imprimer_facture(self):
          if self.ck_print==1:
                messagebox.showinfo("Imprimer"," Impression en cours veuillez Patientez")
                ficher=tempfile.mktemp(".txt")
                open(ficher,"w").write(self.txt_espace_facture.get("1.0",END))
                os.startfile(ficher,"print")
          else:
                messagebox.showerror("Erreur","veuillez Généré la facture")      

        
    def heure(self):
          heure=(time.strftime("%H:%M:%S")) 
          date=(time.strftime("%d-%m-%Y"))
          self.label_heure.config(text=f"Bienvenue chez charly Design\t\t Date:{str(date)}\t\t Heure:{str(heure)}") 
          self.label_heure.after(200,self.heure)

    

    def enregistrer_vente(self):
          
      try:
            conn = sqlite3.connect(database=r"C:\Users\USER\Desktop\mon_deuxieme_project\donnee\magasinbase.bd")
            curseur = conn.cursor()

            # Insérer les détails de la vente dans une table Vente
            curseur.execute("INSERT INTO vente (client_nom, client_contact, montant_total, remise, montant_paye, date_vente) VALUES (?, ?, ?, ?, ?, ?)",
                              (self.var_clnom.get(), self.var_clcontact.get(), self.montant_facture, self.remise, self.net_a_payer, time.strftime("%Y-%m-%d %H:%M:%S")))
            
            # Récupérer l'ID de la dernière vente
            curseur.execute("SELECT last_insert_rowid()")
            vente_id = curseur.fetchone()[0]

            # Insérer les détails de chaque produit vendu dans la table VenteProduit
            for row in self.cart_list:
                  curseur.execute("INSERT INTO vente_produit (vente_id, produit_id, quantite_vendue) VALUES (?, ?, ?)",
                              (vente_id, row[0], row[3]))

            conn.commit()
            conn.close()
      except Exception as error:
            messagebox.showerror("Erreur", f"Erreur lors de l'enregistrement de la vente : {str(error)}")
            
           


            # messagebox.showinfo("Enregistrement", "Vente enregistrée avec succès!")
            # self.reniall()  # Réinitialiser après l'enregistrement

      
    def somme_ventes_par_date(self):
        # Demander à l'utilisateur de saisir la date
        date_saisie = simpledialog.askstring("Somme des ventes par date", "Entrez la date (DD-MM-YYYY):")

        if date_saisie:
            # Effectuer la somme des ventes pour la date spécifiée
            conn = sqlite3.connect(database=r"C:\Users\USER\Desktop\mon_deuxieme_project\donnee\magasinbase.bd")
            curseur = conn.cursor()

            try:
                curseur.execute("SELECT SUM(net_a_payer) FROM vente WHERE date_vente = ?", (date_saisie,))
                total_ventes = curseur.fetchone()[0]

                if total_ventes:
                    messagebox.showinfo("Somme des ventes", f"La somme des ventes pour {date_saisie} est : {total_ventes}")
                else:
                    messagebox.showinfo("Somme des ventes", f"Aucune vente enregistrée pour {date_saisie}")

            except Exception as error:
                messagebox.showerror("Erreur", f"Erreur de connexion : {str(error)}")
            finally:
                conn.close()

    # ... (le reste de votre code) 

             

    def deconecté(self):
        self.root.destroy()
        self.obj=os.system("python3.11.exe c:/Users/USER/Desktop/mon_deuxieme_project/login.py")  
             
if __name__=="__main__":
    root= Tk()
    obj= caisse(root)
    root.mainloop()
