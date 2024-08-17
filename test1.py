# SPDX-FileCopyrightText: 2017 Tony DiCola for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# Simple demo of reading and writing the digital I/O of the MCP2300xx as if
# they were native CircuitPython digital inputs/outputs.
# Author: Tony DiCola
import time

from dataclasses import dataclass
from datetime import datetime, timedelta
from time import sleep

import rpiMethodes

@dataclass
class EQUIPEMENT:
    heureLecture: datetime = datetime.now()
    nomEquipement: str = ""
    valeur: int = 0

equipementsAlarmes = dict ()
equipementsGicleurs = dict()

def initialiseGicleurs(equipementsGicleurs):
    temp = EQUIPEMENT()
    temp.heureLecture = datetime.now()
    temp.nomEquipement = "pinGicleur1"
    temp.valeur=0 
    equipementsGicleurs[temp.nomEquipement]=temp

    temp = EQUIPEMENT()
    temp.heureLecture = datetime.now()
    temp.nomEquipement = "pinGicleur2"
    temp.valeur=0 
    equipementsGicleurs[temp.nomEquipement]=temp

    temp = EQUIPEMENT()
    temp.heureLecture = datetime.now()
    temp.nomEquipement = "pinGicleur3"
    temp.valeur=0 
    equipementsGicleurs[temp.nomEquipement]=temp

    temp = EQUIPEMENT()
    temp.heureLecture = datetime.now()
    temp.nomEquipement = "pinGicleur4"
    temp.valeur=0 
    equipementsGicleurs[temp.nomEquipement]=temp
    
    return equipementsGicleurs


def initialiseAlarmes(equipementsAlarmes):
    temp = EQUIPEMENT()
    temp.heureLecture = datetime.now()
    temp.nomEquipement = "pinChambrePrincipale"
    temp.valeur=0 
    equipementsAlarmes[temp.nomEquipement]=temp

    temp = EQUIPEMENT()
    temp.heureLecture = datetime.now()
    temp.nomEquipement = "pinChambreSecondaire"
    temp.valeur=0 
    equipementsAlarmes[temp.nomEquipement]=temp

    temp = EQUIPEMENT()
    temp.heureLecture = datetime.now()
    temp.nomEquipement = "pinSalon"
    temp.valeur=0 
    equipementsAlarmes[temp.nomEquipement]=temp

    temp = EQUIPEMENT()
    temp.heureLecture = datetime.now()
    temp.nomEquipement = "pinBureau"
    temp.valeur=0 
    equipementsAlarmes[temp.nomEquipement]=temp

    temp = EQUIPEMENT()
    temp.heureLecture = datetime.now()
    temp.nomEquipement = "pinSousSol"
    temp.valeur=0 
    equipementsAlarmes[temp.nomEquipement]=temp

    temp = EQUIPEMENT()
    temp.heureLecture = datetime.now()
    temp.nomEquipement = "pinSalleVernis"
    temp.valeur=0 
    equipementsAlarmes[temp.nomEquipement]=temp

    temp = EQUIPEMENT()
    temp.heureLecture = datetime.now()
    temp.nomEquipement = "pinPorteAvant"
    temp.valeur=0 
    equipementsAlarmes[temp.nomEquipement]=temp

    temp = EQUIPEMENT()
    temp.heureLecture = datetime.now()
    temp.nomEquipement = "pinPorteArriere"
    temp.valeur=0 
    equipementsAlarmes[temp.nomEquipement]=temp

    temp = EQUIPEMENT()
    temp.heureLecture = datetime.now()
    temp.nomEquipement = "pinPorteSousSol"
    temp.valeur=0 
    equipementsAlarmes[temp.nomEquipement]=temp

    temp = EQUIPEMENT()
    temp.heureLecture = datetime.now()
    temp.nomEquipement = "pinSensorFumeeSalleBillard"
    temp.valeur=0 
    equipementsAlarmes[temp.nomEquipement]=temp

    temp = EQUIPEMENT()
    temp.heureLecture = datetime.now()
    temp.nomEquipement = "pinEauAtelier"
    temp.valeur=0 
    equipementsAlarmes[temp.nomEquipement]=temp

    temp = EQUIPEMENT()
    temp.heureLecture = datetime.now()
    temp.nomEquipement = "pinSensorFumeeAtelier"
    temp.valeur=0 
    equipementsAlarmes[temp.nomEquipement]=temp

    temp = EQUIPEMENT()
    temp.heureLecture = datetime.now()
    temp.nomEquipement = "pinSensorPluie"
    temp.valeur=0 
    equipementsAlarmes[temp.nomEquipement]=temp

    return equipementsAlarmes

if __name__ == '__main__':

    # Now loop blinking the pin 0 output and reading the state of pin 1 input.
    sleep(10)

    equipementsAlarmes = initialiseAlarmes(equipementsAlarmes)
    equipementsGicleurs = initialiseGicleurs(equipementsGicleurs)

    while True:
        # Blink pin 0 on and then off.
        # pin0.value = True
        time.sleep(1)
        print ("passe 1")
        equipementsAlarmes=rpiMethodes.getValeursAlarme(equipementsAlarmes)
        print(equipementsAlarmes)
        print ("passe 2")
        equipementsGicleurs=rpiMethodes.getValeursGicleurs(equipementsGicleurs)
        print ("passe 3")
