import re
###########################################################################################
## Naam: Wouter Wajer                                                                    ##
## Datum: 31-03-2015                                                                     ##
## File: Thematoets course 3a                                                            ##
###########################################################################################
#code werkt niet ik was het aan het ombouwen naar OOP maar de tijd was helaas om:O


class getProteins():
    #word altijd uitgevoerd als de class geinstantieerd word
    def __init__(self):
        self.bestand = self.openFile()
        self.proteins,self.title = self.make2lists()
        self.protein = self.splitProteinlist()
        self.checkprotein()   
    #bestand word geopend en gereturned zodat er wat gedaan kan worden
    def openFile(self):
        try:
            bestand = open('HBI-OWE3a_Tentamen1415_KinaseProteins.fa.txt', 'r')
        #afvangen als het bestand niet bestaat
        except IOError:     
            print("Bestand niet gevonden.")
        #overige foutmeldingen afvangen
        except:
            print('Er gaat wat anders fout:O')
        return bestand

    #checkt of regex in sequentie voor komt en returned lijst        
    def reg(seq):
        prolist = re.findall(r"[LIV]G[^P]G[^P][FYWMGSTNH][SGA][^PW][LIVCAT][^PD].[GSTACLIVMFY].{5,18}[LIVMFYWCSTAR][AIVP][LIVMFAGCKR]", seq)
        return prolist


    #maakt 2 listen aan 1 voor de titel 1 voor de eiwit sequenties
    #je weet dat bij beide positie 0  de bijhorende titel en eiwit is
    def make2lists(self):
        try:
            lines = self.bestand.readlines()
            boolean = False
            seq = ''
            i = 0
            titles = []
            proteins = []
            #zet de sequentie in 1 string en zet hem daarna in een list item zodat hij daarna in zijn geheel doorzocht kan worden
            for line in lines:
                if ">" in line:
                    titles.append(line)
                    boolean = False
                if boolean == False:            
                    proteins.append(seq)
                    seq = ''
                if ">" not in line:            
                    boolean = True
                    seq += line
                #anders word de laatste sequentie niet meegepakt
                i += 1
                if i == len(lines):            
                    proteins.append(seq)
            return proteins,title
        except:
            print('er gaat iets fout')

    #kon geen makkelijkere manier vinden om de lege items uit protein list te halen
    #haalt lege items uit list proteins
    def splitProteinlist(self):
        try:
            protein = []
            for pro in proteins:
                if not pro == '':
                    protein.append(pro)
            return protein
        except:
            print('er gaat iets fout')
        
    #zet de titel van een protein in list
    def checkprotein(self,title,protein):
        try:
            eiwit = []
            i = 0
            for pro in protein:
                output = reg(pro)
                #er word een list gereturned met waardes die gevonden zijn
                #als deze list leeg is weet je dat er geen overeenkomsten zijn en doe je niks
                if not len(output) == 0:
                    eiwit.append(title[i])
                    acc = re.findall(r"sp>\|.....",title)
                    print('acc.code:' + acc + str(len(output)) )
                i =+ 1
        except:
            print('er gaat iets fout')
        
getProteins()
