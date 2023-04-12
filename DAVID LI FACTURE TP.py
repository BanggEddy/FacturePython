magasin=" Carrefour Market \n 9, Avenue de la Division Leclerc, \n 94230 Cachan"

#PARTIE CLIENTS
Nbp = 15
code = Nbp * [0]
nom = Nbp * [""]  
prix = Nbp * [0.0]
codetva = Nbp * [0]

numero_facture = 1

def ChargementClient(nomfichier):
    i = 0
    with open(nomfichier, 'r') as f:
        for ligne in f:
            client = ligne.split(';')
            print(client)
            print(i)
            codec[i] = int(client[0])
            nomc[i] = client[1]
            adrec[i] = client[2]
            CPC[i] = client[3]
            Villec[i] = client[4]
            i += 1
    f.close()


def AffichageClients():
    for i in range(Nbc):
        print(codec[i], "  ", nomc[i])



#pa=produit acheté
#clients=choisir
def ChoisirClients():
    clients = 'a'
    while clients == 'a' or clients == 'a':
        AffichageClients()
        selection = int(input("Qui êtes vous? Je suis le numéro: "))
        while selection < 0 or selection > 18:
            selection = int(input("Qui êtes vous? Je suis le numéro: "))

        if selection != 0:
            AffichageProduits()
            article = int(input("Que voulez vous acheter?Je prends le numéro: "))
            Nbpa = 0
            while article != 0:
                produitsachete[Nbpa] = article
                qta[Nbpa] = int(input("Combien de quantiter voulez vous? "))
                Nbpa += 1
                AffichageProduits()
                article = int(input("Que voulez vous acheter?Je prends le numéro: "))
            facture(selection)
        clients = input("Autre client (O/N) : ")
        
#PARIE PRODUITS   
Nbc = 18
codec = Nbc * [0]
nomc = Nbc * [""]
adrec = Nbc * [""]
CPC = Nbc * [""]
Villec = Nbc * [""]

produitsachete = Nbp * [0]
qta = Nbp * [0]
Nbpa = 0          
        
def ChargementProduit(nomfichier):
    i = 0
    with open(nomfichier, 'r') as f:
        for ligne in f:
            produit = ligne.split(';')
            code[i] = int(produit[0])
            nom[i] = produit[1]
            prix[i] = float(produit[2])
            codetva[i] = int(produit[3])
            i += 1
    f.close()


def AffichageProduits():
    for i in range(Nbp):
        print(code[i], "  ", nom[i], " ", prix[i], " ", codetva[i])
    
    


def facture(selection):
    somtotal=0
    tva20=0
    tva5_5=0
    adsclient = ("{0:>70}".format(nomc[selection - 1])) + "\n" + ("{0:>70}".format(adrec[selection - 1])) + "\n" + ("{0:>70}".format(CPC[selection - 1])) + " " + ("{0:>70}".format(Villec[selection - 1]))
    print(magasin,"\n\n" + ("{0:>35}".format("Facture ")) + str(numero_facture) + "\n\n" + adsclient)

    
    
    print("{:*^75}".format("*"))
    print("{0:>5}".format("Code"),"*","{0:>22}".format("Désignation"),"{0:>15}".format("* Prix"),"{0:>15}".format("* Quantité"),"{0:>10}".format("* Montant *"))
    print("{:*^75}".format("*"))
    i = 0
    for numeroproduit in produitsachete:
        if numeroproduit != 0:
            quantite = qta[i]
            
            montant = prix[numeroproduit - 1] * quantite
            somtotal += montant
            print("{0:>5}".format(str(numeroproduit)) + " * " +
                  ("{0:>30}".format(str(nom[numeroproduit - 1]))) + " * " +
                  ("{0:>5}".format(str(prix[numeroproduit - 1]))) + " * " +
                  (("{0:>10}".format("* ")+str(quantite))) + " * " +
                  (("{0:>5}".format("* ")+str(montant))),"*") 
        if codetva[numeroproduit-1]==1:
            tva20 += montant * 0.2
        elif codetva[numeroproduit-1]==2:
            tva5_5 += montant * 0.055
        i += 1
    print("{:*^75}".format("*"))
    
    somtotal += tva20 + tva5_5
    print("{0:>70}".format("Total TTC *")+str(round(somtotal,2)),"*")
         
    print("{:*^75}".format("*"))
    print("{0:>70}".format("Montant de la taxe de 20% *")+str(round(tva20,2)),"*")
        
    print("{:*^75}".format("*"))
    print("{0:>70}".format("Montant de la taxe de 5.5% *")+str(round(tva5_5,2)),"*")
    
    
    print("{:*^75}".format("*"))


ChargementClient("Client.txt")
ChargementProduit("Produit.txt")
ChoisirClients()


