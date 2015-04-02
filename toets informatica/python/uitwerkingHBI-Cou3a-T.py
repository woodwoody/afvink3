import re

def main():
    bestandsnaam = "hiv_interactions.txt"
    maakDict(bestandsnaam)

def controleerAccession(acc):
    # twee letter, underscore,cijfers een punt en een cijfer
    if not re.search("[A-Za-z]{2}_[0-9]{6}\.[0-9]",acc):
        print (" Fout in :",acc)

def vindAccession(naam):
    bestand = open(naam,"r")
    for regel in bestand:
        lijst = regel.split("\t")
        acc = lijst[2]
        controleerAccession(acc)

def maakDict(naam):
    dikt = {}
    bestand = open("hiv_interactions.txt","r")
    for regel in bestand:
        lijst = regel.split("\t")
        acc1 = lijst[2] # eerste accession
        acc2 = lijst[7] # eerste accession
        #print (acc1,"heeft interactie met ",acc2)
        # als er nog niks in zit zet hem erin
        if acc1 not in dikt.keys():
            dikt.update ({acc1:[acc2]})
        else:            
            lijstAcc = dikt[acc1]
            lijstAcc.append(acc2)
            dikt.update ({acc1:lijstAcc})
        
    print (dikt)
main()

class eiwit:

    def __init__(self,acc):
        self.lijstInteractions = dikt[acc]

    def getInteractions(self):
        return self.lijstInteractions
