###########################################################################################
## Naam: Leonoor Engeltjes                                                               ##
## Datum: 29-03-2012                                                                     ##
## File: Thematoets course 3a                                                            ##
## Functies: getData, isValidAA, maakDict en myGUI                                       ##
## Known bugs: patroon 2 klopt niet, wordt niet meegenomen in de rest van het programma, ##
##             in de GUI kan geen nieuwe IPI worden ingetikt, na invoer annuleren        ##
###########################################################################################

import re
import tkinter

class IPI():
    def __init__(self):        
        print("Deze class bevat de volgende functies: getData, isValidAA, maakDict en myGUI.")
        try:
            loadfile = 'hiv_interactions.txt'
            self.bestand = open(loadfile, 'r')
            self.getData()
            self.isValidAA()
            self.maakDict()
            self.myGUI()
        except IOError:     #afvangen als het bestand niet bestaat
            print("Bestand niet gevonden.")
        self.patroon1 = '[BJOUXZ]' #voor de controle op validAA
        self.patroon2 = '[ACDEFGHIKLMNPQRSTVWY]{1,9}\s[ACDEFGHIKLMNPQRSTVWY]{10}' #voor controle 10AA, spatie, 10AA, spatie, etc

    def getData(self):  #deze functie haalt alle benodigde data uit het bestand voor alle verdere functies
        try:
            read = False
            self.ipilist = []       
            self.seqlist = []
            self.desclist = []
            seq = ""
            for regel in self.bestand:
                regel = regel.replace('\n',' ') #anders worden de laatste 10 AA van regel 1 aan de eerste 10 van regel 2 geplakt, etc
                if 'SQ' in regel:
                    read = True #vanaf de sequentie lezen
                elif read == True:
                    if '//' in regel:
                        self.seqlist.append(seq) 
                        seq = "" 
                        read = False #sequentie afgelopen, stoppen met lezen
                    else:
                        seq += regel[5:] 
                if 'ID   ' in regel: 
                    self.ipilist.append(regel[5:16]) #lijst maken met alle ipi codes
                if 'DE   ' in regel: 
                    self.desclist.append(regel[5:]) #lijst maken met alle beschrijvingen
        except IOError:
            print("Bestand niet gevonden.")
        except IndexError:
            print("Er is iets fout gegaan bij het slicen van de data")
        except:
            print("Er is een onbekende fout opgetreden")

    def isValidAA(self):
        try:
            self.foutipilist = [] 
            self.foutseqlist = []
            self.foutdesclist = []
            for i in range(len(self.seqlist)):
                if re.search(self.patroon1, self.seqlist[i]) != None: #als er een hit is op patroon1, worden de bijbehorende seq, beschr en functie in lijsten gezet
                    self.foutseqlist.append(self.seqlist[i])
                    self.foutipilist.append(self.ipilist[i])
                    self.foutdesclist.append(self.desclist[i])

            #Aantal foute eiwitten weergeven en ipilist retourneren        
            print(len(self.foutseqlist),"eiwitten hebben een of meer foute aminozuren.")
            print("Dit zijn de IPI nummers van de foute eiwitten:")
            return self.foutipilist
        except IndexError:
            print("Er is iets fout gegaan bij het toevoegen aan de nieuwe lijsten.")
        except TypeError:
            print("Fout bij het itereren.")
        except:
            print("Er is een onbekende fout opgetreden.")
            
    def maakDict(self):
        try:
            values = []
            combo = []

            #eerst sequenties en beschr samen in lijstjes zetten
            #deze lijstjes in een grote lijst values zetten voor de dictionary
            for i in range(len(self.foutseqlist)):
                combo.append(self.foutseqlist[i])
                combo.append(self.foutdesclist[i])
                values.append(combo)
                combo = []

            #dictionary maken
            self.dict = {}
            for i in range(len(self.foutseqlist)):
                self.dict[self.foutipilist[i]] = values[i]
        except IndexError:
            print("Er is iets fout gegaan bij het toevoegen van data aan de dictionary.")
        except TypeError:
            print("Fout bij het itereren.")
        except:
            print("Er is een onbekende fout opgetreden.")

    def myGUI(self):
        #GUI maken

        #main_window
        self.main_window = tkinter.Tk()
        self.main_window.title("IPI Verifier - (c) Leonoor")

        #de frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.middle_frame = tkinter.Frame(self.main_window)
        self.middle_frame2 = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        #de labels om de foute IPI's overzichtelijk weer te geven
        self.label0 = tkinter.Label(self.top_frame, text = "Onderstaande codes horen bij foute eiwitten.")
        self.label0.pack()

        self.label1 = tkinter.Label(self.top_frame, text = ', '.join(self.foutipilist[0:15]))
        self.label1.pack()

        self.label2 = tkinter.Label(self.top_frame, text = ', '.join(self.foutipilist[15:30]))
        self.label2.pack()

        self.label3 = tkinter.Label(self.top_frame, text = ', '.join(self.foutipilist[30:45]))
        self.label3.pack()

        self.label4 = tkinter.Label(self.top_frame, text = ', '.join(self.foutipilist[45:60]))
        self.label4.pack()

        self.label5 = tkinter.Label(self.top_frame, text = ', '.join(self.foutipilist[60:68]))
        self.label5.pack()
        
        self.label6 = tkinter.Label(self.middle_frame, text = "Voer een IPI code in:")
        self.label6.pack(side="left")

        #entry voor de ipi code maken
        self.ipi_entry = tkinter.Entry(self.middle_frame, width=10)
        self.ipi_entry.pack(side = 'left')

        #knoppen maken om informatie te verkrijgen en de GUI te verlaten
        self.submit_button = tkinter.Button(self.middle_frame, \
                                        text = "Submit",\
                                        command = self.submission)
        self.quit_button = tkinter.Button(self.bottom_frame, \
                                          text = 'Annuleren', \
                                          command = self.main_window.destroy)

        #frames en knoppen packen
        self.top_frame.pack()
        self.middle_frame.pack()
        self.middle_frame2.pack()
        self.bottom_frame.pack()
        
        self.submit_button.pack(side='left')
        self.quit_button.pack(side='right')
      
        tkinter.mainloop()

    def submission(self):
        try:
            #entry verkrijgen
            ipi_code = self.ipi_entry.get()

            #value verkrijgen
            results = self.dict[ipi_code]
            print(results)

            #labels met output maken
            label7 = tkinter.Label(self.middle_frame2, text = "Aminozuren: " + results[0])
            label7.pack(side = "left")
            label8 = tkinter.Label(self.bottom_frame, text = "Functie: " + results[1])
            label8.pack(side = "left")
        except KeyError:
            print("Dit is geen IPI-code uit bovengenoemde reeks.")
        except:
            print("Er is een onbekende fout opgetreden.")
lala = IPI()

