##########################################################################
# (c) 2013 HAN/Wouter Wajer                                              #
# Dictionaries voor het gebruik bij de afvinkopdrachten van HBI-Cou3a    #
# Update: 03-maart-2015 voorzien van commentaar en bestandsnaam aangepast#
##########################################################################
def main():
    string = getString()
    codons = GetCodons(string)
    ProteinFinder(codons)


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


def ProteinFinder(codons):
    code = {'ttt': 'F', 'tct': 'S', 'tat': 'Y', 'tgt': 'C',
        'ttc': 'F', 'tcc': 'S', 'tac': 'Y', 'tgc': 'C',
        'tta': 'L', 'tca': 'S', 'taa': '*', 'tga': '*',
        'ttg': 'L', 'tcg': 'S', 'tag': '*', 'tgg': 'W',
        'ctt': 'L', 'cct': 'P', 'cat': 'H', 'cgt': 'R',
        'ctc': 'L', 'ccc': 'P', 'cac': 'H', 'cgc': 'R',
        'cta': 'L', 'cca': 'P', 'caa': 'Q', 'cga': 'R',
        'ctg': 'L', 'ccg': 'P', 'cag': 'Q', 'cgg': 'R',
        'att': 'I', 'act': 'T', 'aat': 'N', 'agt': 'S',
        'atc': 'I', 'acc': 'T', 'aac': 'N', 'agc': 'S',
        'ata': 'I', 'aca': 'T', 'aaa': 'K', 'aga': 'R',
        'atg': 'M', 'acg': 'T', 'aag': 'K', 'agg': 'R',
        'gtt': 'V', 'gct': 'A', 'gat': 'D', 'ggt': 'G',
        'gtc': 'V', 'gcc': 'A', 'gac': 'D', 'ggc': 'G',
        'gta': 'V', 'gca': 'A', 'gaa': 'E', 'gga': 'G',
        'gtg': 'V', 'gcg': 'A', 'gag': 'E', 'ggg': 'G'
       }

    aa3 = {"Ala": ["GCU", "GCC", "GCA", "GCG"],
           "Arg": ["CGU", "CGC", "CGA", "CGG", "AGA", "AGG"],
           "Asn": ["AAU", "AAC"],
           "Asp": ["GAU", "GAC"],
           "Cys": ["UGU", "UGC"],
           "Gln": ["CAA", "CAG"],
           "Glu": ["GAA", "GAG"],
           "Gly": ["GGU", "GGC", "GGA", "GGG"],
           "His": ["CAU", "CAC"],
           "Ile": ["AUU", "AUC", "AUA"],
           "Leu": ["UUA", "UUG", "CUU", "CUC", "CUA", "CUG"],
           "Lys": ["AAA", "AAG"],
           "Met": ["AUG"],
           "Phe": ["UUU", "UUC"],
           "Pro": ["CCU", "CCC", "CCA", "CCG"],
           "Ser": ["UCU", "UCC", "UCA", "UCG", "AGU","AGC"],
           "Thr": ["ACU", "ACC", "ACA", "ACG"],
           "Trp": ["UGG"],
           "Tyr": ["UAU", "UAC"],
           "Val": ["GUU", "GUC", "GUA", "GUG"],
           "Start": ["AUG", "CUG", "UUG", "GUG", "AUU"],
           "Stop" : ["UAG", "UGA", "UAA"]
          }

    for codon in codons:
        for pr,cod in aa3.items():
            if codon in codons:
                print(pr)

main()