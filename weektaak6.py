import re

def main():
    i = 0
    dna = 'ATGCCCCB'
    funct1(i,dna)
    
    #print(isDNA(dna))

#deze functie was niet conform de opdracht
#def isDNA(dna):
    #main(i)
    #x = re.findall(r"[^ATGC]", dna)
    #if not x:
        #return True
    #else:
        #return False

def funct1(i,dna):
    if i == 1500:
        print('teveel gedoe stoppen!!!')
    else:
        if i == len(dna):
            print('Het DNA is DNA yeah!!!')
        else:
            x = re.findall(r"[ATGC]", dna[i])
            if not x:
                print('ojee dit is geen dna')            
            else:
                i += 1
                funct1(i,dna)

main()
