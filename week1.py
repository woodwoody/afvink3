def main():
    string = getString()
    codons = GetCodons(string)
    getCodonlist(codons)
    

def getString():
    bestand = open('m_p53.gb','r')
    lines = bestand.readlines()
    boolean = False
    string = ''
    for line in lines:
        if boolean == True:
            string += line.strip('\t\n\r').replace(' ','').strip("0123456789=,//")
        if "ORIGIN" in line:
            boolean = True
    return string

def GetCodons(bestand):
    codon = []
    for i in range(0, len(bestand),3):
        codon.append(bestand[i:i+3])
    return codon
main()

#getstring
#open bestand
#loop door de regels van het bestand
#if het woord ORIGIN is gevonden strip dan alle volgende regels van cijfers en whitespaces
#voeg de gestripte regel toe aan de string
#return een string

#getcodons
#loop met een range die even lang is als de string en de teller moet constant met 3 verhoogt worden
#voeg de 3 letters toe aan de array
#print de array
