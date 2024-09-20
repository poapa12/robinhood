import json
import random


class Lokalita:
    def __init__(self):
        self.bobri = []
        self.nory = [] 
        self.bobri_nory = {} 


    def nacti_bobry(self, bobri_soubor):
        with open(bobri_soubor, 'r') as f:
            data = json.load(f)
            self.bobri = data["bobri"]

 
    def nacti_nory(self, nory_soubor):
        with open(nory_soubor, 'r') as f:
            data = json.load(f)
            self.nory = data["nory"]


    def prirad_nory(self):
        random.shuffle(self.nory)
        for i, bobr in enumerate(self.bobri):
         
            self.bobri_nory[bobr] = self.nory[i % len(self.nory)]


    def __str__(self):
        vystup = "Bobři a jejich nory:\n"
        for bobr, nora v self.bobri_nory.items():
            vystup += f"{bobr} je v noře {nora}\n"
        return vystup


if __name__ == "__main__":

    lokalita = Lokalita()


    lokalita.nacti_bobry("bobri.json")
    lokalita.nacti_nory("nory.json")


    lokalita.prirad_nory()


    print(lokalita)
