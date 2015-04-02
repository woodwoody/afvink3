class MyClass():   

    def __init__(self, naam_gen,DNA_sequentie,familiename,organisme):
        self.naam_gen = naam_gen
        self.DNA_sequentie = DNA_sequentie
        self.familiename = familiename
        self.organisme = organisme

    def getTranscript(self):        
        rna = self.DNA_sequentie.replace("t", "u")
        return rna

    def getTranslation(self,rna):
        for i in range(0,len(rna),3):
            print(rna[i:i+3])

naam_gen = input('Maak een leuke naam')
DNA_sequentie = input('DNA sequentie')
familiename = input('familie naam')
organisme = input('Naam organisme')

jemoeder = MyClass(naam_gen,DNA_sequentie,familiename,organisme)
rna = jemoeder.getTranscript()
jemoeder.getTranslation(rna)

jemoeder1 = MyClass(naam_gen,DNA_sequentie,familiename,organisme)
rna = jemoeder1.getTranscript()
jemoeder1.getTranslation(rna)
