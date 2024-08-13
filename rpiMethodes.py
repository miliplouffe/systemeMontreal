import sys, os
from time import sleep
from json import JSONEncoder
import gpiozero
from gpiozero import DigitalInputDevice
import board
import busio

from digitalio import Direction
from adafruit_mcp230xx.mcp23017 import MCP23017

class const:
    relais1=23
    relais2=24
    relais3=25
    relais4=26

    pinChambrePrincipale=0
    pinChambreSecondaire=1
    pinBureau=2
    pinSalon=3
    pinSousSol=4
    pinSalleVernis=5
    pinPorteAvant=6
    pinPorteArriere=7
    pinPorteSousSol=8
    pinSensorFumeeSalleBillard=9
    pinSensorFumeeAtelier=10
    pinAlarmeSonore=11
    pinMouvementSalleBillard=12



i2c = busio.I2C(board.SCL, board.SDA)
mcp = MCP23017(i2c)


relais1 = gpiozero.OutputDevice(const.relais1, active_high=False, initial_value=False)
relais2=  gpiozero.OutputDevice(const.relais2, active_high=False, initial_value=False)
relais3=  gpiozero.OutputDevice(const.relais3, active_high=False, initial_value=False)
relais4=  gpiozero.OutputDevice(const.relais4, active_high=False, initial_value=False)

pinChambrePrincipale = mcp.get_pin(const.pinChambrePrincipale)
pinChambrePrincipale.direction = Direction.INPUT
pinChambrePrincipale.pull = Direction.Pull.UP

pinChambreSecondaire = mcp.get_pin(const.pinChambreSecondaire)
pinChambreSecondaire.direction = Direction.INPUT
pinChambreSecondaire.pull = Direction.Pull.UP

pinBureau = mcp.get_pin(const.pinBureau)
pinBureau.direction = Direction.INPUT
pinBureau.pull = Direction.Pull.UP

pinSalon = mcp.get_pin(const.pinSalon)
pinSalon.direction = Direction.INPUT
pinSalon.pull = Direction.Pull.UP

pinSousSol = mcp.get_pin(const.pinSousSol)
pinSousSol.direction = Direction.INPUT
pinSousSol.pull = Direction.Pull.UP

pinMouvementSalleBillard = mcp.get_pin(const.pinMouvementSalleBillard)
pinMouvementSalleBillard.direction = Direction.INPUT
pinMouvementSalleBillard.pull = Direction.Pull.UP

pinSalleVernis = mcp.get_pin(const.pinSalleVernis)
pinSalleVernis.direction = Direction.INPUT
pinSalleVernis.pull = Direction.Pull.UP

pinPorteAvant = mcp.get_pin(const.pinPorteAvant)
pinPorteAvant.direction = Direction.INPUT
pinPorteAvant.pull = Direction.Pull.UP

pinPorteArriere = mcp.get_pin(const.pinPorteArriere)
pinPorteArriere.direction = Direction.OUTINPUTPUT
pinPorteArriere.pull = Direction.Pull.UP

pinPorteSousSol = mcp.get_pin(const.pinPorteSousSol)
pinPorteSousSol.direction = Direction.INPUT
pinPorteSousSol.pull = Direction.Pull.UP

pinSensorFumeeSalleBillard = mcp.get_pin(const.pinSensorFumeeSalleBillard)
pinSensorFumeeSalleBillard.direction = Direction.INPUT
pinSensorFumeeSalleBillard.pull = Direction.Pull.UP

pinAlarmeSonore = mcp.get_pin(const.pinAlarmeSonore)
pinAlarmeSonore.direction = Direction.INPUT
pinAlarmeSonore.pull = Direction.Pull.UP



def get_relais(nomRelais):
    global relais1, relais2, relais3, relais4

    valeur=False

    if nomRelais=="relais1":
       valeur= relais1.value
    if nomRelais=="relais2":
        valeur= relais2.value
    if nomRelais=="relais3":
        valeur= relais3.value            
    if nomRelais=="relais4":
        valeur= relais4.value
    
    return valeur

def set_relais(nomRelais, statut):
    global relais1, relais2, relais3, relais4

    if statut==True:
        print ("statut True")
        if nomRelais =="relais1":
            print ("relais on")
            relais1.on()
        if nomRelais =="relais2":
            relais2.on()        
        if nomRelais =="relais3":
            relais3.on()
        if nomRelais =="relais4":
            relais4.on()            
    else:
        if nomRelais =="relais1":
            print ("relais off")
            relais1.off()
        if nomRelais =="relais2":
            relais2.off()
        if nomRelais =="relais3":
            relais3.off()
        if nomRelais =="relais4":
            relais4.off()


    PanneElectrique: float = 0.0

def getAlarmeDetecteur(detecteurAlarme):

    pinChambrePrincipale=0
    pinChambreSecondaire=1
    pinBureau=2
    pinSalon=3
    pinSousSol=4
    pinSalleVernis=5
    pinPorteAvant=6
    pinPorteArriere=7
    pinPorteSousSol=8
    pinSensorFumeeSalleBillard=9
    pinSensorFumeeAtelier=10
    pinAlarmeSonore=11
    detecteurAlarme.MouvChambrePrincipale=pinChambreSecondaire.value
    detecteurAlarme.MouvChambreSecondaire=pinChambreSecondaire.value
    detecteurAlarme.MouvBureau=pinBureau.value
    detecteurAlarme.MouvSalon=pinSalon.value
    detecteurAlarme.MouvSalleBillard=pinMouvementSalleBillard.value
    detecteurAlarme.MouvSalleVernis=pinSalleVernis.value
    detecteurAlarme.InterPorteAvant=pinPorteAvant.value
    detecteurAlarme.InterPorteArriere=mcp.digital_read(const.pinPorteArriere)
    detecteurAlarme.InterPorteSousSol=mcp.digital_read(const.pinPorteSousSol)
    detecteurAlarme.DectEauAtelier=mcp.digital_read(const.pinChambrePrincipale)
    detecteurAlarme.DectEauSalleLavage=mcp.digital_read(const.pinChambrePrincipale)
    detecteurAlarme.DectFumeeAtelier=mcp.digital_read(const.pinSensorFumeeAtelier)
    detecteurAlarme.DectFumeeSalleBillard=mcp.digital_read(const.pinSensorFumeeSalleBillard)

    return detecteurAlarme

def getArrosageDetecteur(gicleursStatut):
    gicleursStatut["1"].statut = get_relais("relais1")
    gicleursStatut["2"].statut = get_relais("relais2")
    gicleursStatut["3"].statut = get_relais("relais3")
    gicleursStatut["4"].statut = get_relais("relais4")

    return gicleursStatut