import sys, os
from time import sleep
from json import JSONEncoder
import gpiozero
from gpiozero import DigitalInputDevice
from mcp23017 import *
from smbus2 import SMBus


class const:
    relais1=23
    relais2=24
    relais3=25
    relais4=26

    pinChambrePrincipale=GPA0
    pinChambreSecondaire=GPA1
    pinBureau=GPA2
    pinSalon=GPA3
    pinSousSol=GPA4
    pinSalleVernis=GPA5
    pinPorteAvant=GPA6
    pinPorteArriere=GPA7
    pinPorteSousSol=GPB0
    pinSensorFumeeSalleBillard=GPB1
    pinSensorFumeeAtelier=GPB2

    pinAlarmeSonore=GPB2

i2c = bus = SMBus(1)  # creates a I2C Object as a wrapper for the SMBus
mcp = MCP23017(0x20, i2c)   # creates an MCP object with the given address


relais1 = gpiozero.OutputDevice(const.relais1, active_high=False, initial_value=False)
relais2=  gpiozero.OutputDevice(const.relais2, active_high=False, initial_value=False)
relais3=  gpiozero.OutputDevice(const.relais3, active_high=False, initial_value=False)
relais4=  gpiozero.OutputDevice(const.relais4, active_high=False, initial_value=False)


def initialiseMcp23017():
    mcp.pin_mode(pinChambrePrincipale,INPUT)
    mcp.pin_mode(pinBureau,INPUT)
    mcp.pin_mode(pinSalon,INPUT)
    mcp.pin_mode(pinSousSol,INPUT)
    mcp.pin_mode(pinSalleVernis,INPUT)
    mcp.pin_mode(pinPorteAvant,INPUT)
    mcp.pin_mode(pinPorteArriere,INPUT)
    mcp.pin_mode(pinPorteSousSol,INPUT)
    mcp.pin_mode(pinSensorFumeeSalleBillard,GPB1,INPUT)
    mcp.pin_mode(pinAlarmeSonore,INPUT)



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

    detecteurAlarme.MouvChambrePrincipale=mcp.digital_read(const.pinChambrePrincipale)
    detecteurAlarme.MouvChambreSecondaire=mcp.digital_read(const.pinChambreSecondaire)
    detecteurAlarme.MouvBureau=mcp.digital_read(const.pinBureau)
    detecteurAlarme.MouvSalon=mcp.digital_read(const.pinSousSol)
    detecteurAlarme.MouvSalleBillard=mcp.digital_read(const.pinSalleBillard)
    detecteurAlarme.MouvSalleVernis=mcp.digital_read(const.pinSalleVernis)
    detecteurAlarme.InterPorteAvant=mcp.digital_read(const.pinPorteAvant)
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