import numpy as np
import matplotlib.pyplot as plt

def main():
    string = getString()
    codons = GetCodons(string)
    codonlist,countlist = getCodonlist(codons)
    makeGraph(codonlist,countlist)


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

def getCodonlist(codons):
    codonlist = []
    countlist = []
    for codon in codons:
        if codon not in codonlist:
            codonlist.append(codon)
            countlist.append(codons.count(codon))
    return codonlist,countlist

def makeGraph(codonlist,countlist):
    print(len(codonlist))
    n_groups = len(codonlist)

    fig, ax = plt.subplots()

    index = np.arange(n_groups)
    bar_width = 0.35

    opacity = 0.4
    error_config = {'ecolor': '0.3'}

    rects1 = plt.bar(index, countlist, bar_width,
                     alpha=opacity,
                     color='b',
                     label='Dikke codons')


    plt.xlabel('Group')
    plt.ylabel('Scores')
    plt.title('Scores by group and gender')
    plt.xticks(index + bar_width, codonlist)
    plt.legend()

    plt.tight_layout()
    plt.show()


main()

