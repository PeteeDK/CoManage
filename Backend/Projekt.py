import csv
import os


class Projekt:

    def __init__(self, navn, beskrivelse, startdato, detaljer, deadline):
        self.projektnavn = navn
        self.projektbeskrivelse = beskrivelse
        self.projektstartdato = startdato
        self.projektDetaljer = detaljer
        self.projektDeadline = deadline
        self.projektOpgaveEmner = []
        self.projektRessourcer = []

    def CreateProjekt(self):
        navn = input("Please enter the name of the Projekt")
        beskrivelse = input("Please enter a description for Projekt")
        startdato = input("Please enter a start date the Projekt")
        detajler = input("Please enter extra details of the Projekt")
        deadLine = input("Please enter the deadline(date) of the Projekt")
        data = [[navn, beskrivelse, startdato, detajler, deadLine]]
        #hvis dette program bliver kørt på en windows pc så skal det muligvis kun være
        # users\xxxx\ som skal skiftes
        path = r'C:\Users\petee\PycharmProjects\Corolab\CoManage\Backend\projects.csv'
        os.path.normpath(path)
        file = open(path, "a", newline="",)
        csvwriter = csv.writer(file)
        csvwriter.writerows(data)

    def ReadProjekts(self):
        list = []
        path = r'C:\Users\petee\PycharmProjects\Corolab\CoManage\Backend\projects.csv'
        os.path.normpath(path)
        file = open(path, "r")
        csvReader = csv.reader(file)
        for navn, beskrivelse, startdato, detajler, deadLine in csvReader:
            list.append(Projekt(navn, beskrivelse, startdato, detajler, deadLine))
        #for x in list:
            #print(f"\n{x.projektnavn}")
        return list