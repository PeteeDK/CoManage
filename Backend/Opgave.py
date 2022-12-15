class Opgave:

    def __init__(self,navn,estimeretTid,beskrivelse,startDato,deadline):
        opgaveNavn = navn
        opgavetid = estimeretTid
        opgaveBeskrivelse = beskrivelse
        opgaveStartDato = startDato
        opgaveDeadLine = deadline
        resourceListe = []

    def CreateErsignment(self):
        navn = input("Please enter the name of the Projekt")
        opgavetid = input("Please enter the name of the Projekt")
        opgaveBeskrivelse = input("Please enter the name of the Projekt")
        startdato = input("Please enter the name of the Projekt")
        deadLine = input("Please enter the name of the Projekt")
        opgave = Opgave(navn, opgavetid, opgaveBeskrivelse, startdato, deadLine)
        return opgave