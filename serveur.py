"""Serveur Modbus TCP : automate régulation de tension

Carte mémoire :
    CO 0 : Régulation (0 éteinte ; 1 allumée)
    DI 0 : Seuil bas tension (0 = OK ; 1 = alarme)
    DI 1 : Seuil haut tension (0 = OK ; 1 = alarme)
    HR 0 : seuil haut réglable (en volts, valeur entière)
    HR 1 : seuil bas réglable (en volts, valeur entière)
    HR 2 : tension mesurée (en volts, valeur entière)
"""

from pymodbus.server import StartTcpServer
from pymodbus.simulator import DataType, SimData, SimDevice
import asyncio

CO_REGULATION = 0
DI_HIGH_VOLTAGE = 0
DI_LOW_VOLTAGE = 1
HR_THRESHOLD_HIGH = 0
HR_THRESHOLD_LOW = 1
HR_VOLTAGE = 2

# Réseau
DEVICE_ID = 1
ADDRESS = ("0.0.0.0", 502)

import config

def build_device() -> SimDevice:
    """Décrit les 4 blocs de la mémoire Modbus."""
    # Ordre imposé par pymodbus : coils, discrete inputs, holding registers, input registers
    return SimDevice(
        id=DEVICE_ID,
        simdata=(
            # CO : régulation éteinte au démarrage
            [SimData(CO_REGULATION, values=False, datatype=DataType.BITS)],
            # DI : aucune alarme au démarrage
            [
                SimData(DI_HIGH_VOLTAGE, values=False, datatype=DataType.BITS),
                SimData(DI_LOW_VOLTAGE, values=False, datatype=DataType.BITS),
            ],
                        # HR : seuils réglables et tension choisie par le client
            [
                SimData(
                    HR_THRESHOLD_HIGH,
                    values=config.VOLTAGE_THRESHOLD_HIGH_DEFAULT,
                    datatype=DataType.REGISTERS,
                ),
                SimData(
                    HR_THRESHOLD_LOW,
                    values=config.VOLTAGE_THRESHOLD_LOW_DEFAULT,
                    datatype=DataType.REGISTERS,
                ),
                SimData(
                    HR_VOLTAGE,
                    values=config.VOLTAGE_START,
                    datatype=DataType.REGISTERS,
                ),
            ],
            # IR : inutilisé pour l'instant (pymodbus refuse un bloc vide)
            [SimData(0, values=0, datatype=DataType.REGISTERS)],
        ),
    )

def main() -> None:
    """Étape 2 : démarrer le serveur TCP sur le port 502."""
    StartTcpServer(context=build_device(), address=ADDRESS)


if __name__ == "__main__":
    main()