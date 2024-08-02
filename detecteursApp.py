import sys, os
import rpiMethodes
import RedisInOut as redisInOut
from dataclasses import dataclass


redisIpAdresse="192.168.1.143"
redisInOut.InitialiseRedisClient(redisIpAdresse)

class const:
    format = "02-01-2006 15:04:05"

detecteurGicleur = dict()
requete=""

class DETECTEUR:
    MouvChambrePrincipale: int
    MouvChambreSecondaire: int
    MouvBureau: int
    MouvSalon: int
    MouvSalleBillard: int
    MouvSalleVernis: int
    InterPorteAvant: int
    InterPorteArriere: int
    InterPorteSousSol: int
    DectEauAtelier: int
    DectEauSalleLavage: int
    DectEauPluie: int
    DectFumeeSalleBillard: int
    DectFumeeAtelier: int


@dataclass
class DETECTEUR:
    Prop: float = 0.0
    Co: float = 0.0
    Fumee: float = 0.0
    Mouvement: float = 0.0
    EauElectrique: float = 0.0
    EauTraitement: float = 0.0
    PanneElectrique: float = 0.0

@dataclass
class GICLEURS_STATUT:  
    NoZone: int = 0
    Statut: bool = False


def initialiseGicleursStatut(**gicleursStatut):
    gicleurRec = GICLEURS_STATUT()
    gicleurRec.NoZone = 1
    gicleurRec.Statut = 0
    gicleursStatut[str(gicleurRec.NoZone)] = gicleurRec

    gicleurRec = GICLEURS_STATUT()
    gicleurRec.NoZone = 2
    gicleurRec.Statut = 0
    gicleursStatut[str(gicleurRec.NoZone)] = gicleurRec

    gicleurRec = GICLEURS_STATUT()
    gicleurRec.NoZone = 3
    gicleurRec.Statut = 0
    gicleursStatut[str(gicleurRec.NoZone)] = gicleurRec

    gicleurRec = GICLEURS_STATUT()
    gicleurRec.NoZone = 4
    gicleurRec.Statut = 0
    gicleursStatut[str(gicleurRec.NoZone)] = gicleurRec
    
    return gicleursStatut


def executeRequete(requete):
    print ("requete arrosage 1 ", requete)
    if requete == "Gicleur_1_ON":
        print ("--------------------- ON")
        rpiMethodes.set_relais("relais1", True)
        redisInOut.setRequeteArrosageNil()

    if requete == "Gicleur_1_OFF":
        print ("-------------------- OFF")
        rpiMethodes.set_relais("relais1", False)    
        redisInOut.setRequeteArrosageNil()

    if requete == "Gicleur_2_ON":
        print ("--------------------- ON")
        rpiMethodes.set_relais("relais1", True)
        redisInOut.setRequeteArrosageNil()

    if requete == "Gicleur_2_OFF":
        print ("-------------------- OFF")
        rpiMethodes.set_relais("relais1", False)    
        redisInOut.setRequeteArrosageNil()

    if requete == "Gicleur_3_ON":
        print ("--------------------- ON")
        rpiMethodes.set_relais("relais1", True)
        redisInOut.setRequeteArrosageNil()

    if requete == "Gicleur_3_OFF":
        print ("-------------------- OFF")
        rpiMethodes.set_relais("relais1", False)    
        redisInOut.setRequeteArrosageNil()

    if requete == "Gicleur_4_ON":
        print ("--------------------- ON")
        rpiMethodes.set_relais("relais1", True)
        redisInOut.setRequeteArrosageNil()

    if requete == "Gicleur_4_OFF":
        print ("-------------------- OFF")
        rpiMethodes.set_relais("relais1", False)    
        redisInOut.setRequeteArrosageNil()


redisInOut.StartSystemeArrosageRequete()

if __name__ == '__main__':

    gicleursStatut = dict()
    gicleursStatut = initialiseGicleursStatut()

    detecteurAlarme=DETECTEUR()

    while True:
        try:

            # pour alarmes
            detecteurAlarme=rpiMethodes.getAlarmeDetecteur(detecteurAlarme)
            redisInOut.publishInterfaceAlarmeDetecteur(detecteurAlarme)
            # pour systeme arrosage va lire si le systeme arrose
            gicleursStatut=rpiMethodes.getArrosageDetecteur(gicleursStatut)

            requete=redisInOut.getRequeteArrosage()
            redisInOut.setRequeteArrosageNil()
            if requete != "1" and  requete != "":
                executeRequete(requete)
            
            redisInOut.publishInterfaceDetecteurArrosage(gicleursStatut)  

        except Exception as e:
            print (e)
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]    
            # print(exc_type, fname, exc_tb.tb_lineno)
