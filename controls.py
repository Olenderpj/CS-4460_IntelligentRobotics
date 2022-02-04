import logging
from time import sleep

def setSingleMotorVelocity(sim, motorPath, velocity ):
    motor = sim.getObject(motorPath)
    sim.setJointTargetVelocity(motor, velocity)

def setDualMotorToSameVelocity():
    pass

def setDualMotorToDifferentVelocity():
    pass


def restartSimulation(simulationObj):
    logging.warning("Restarting Simulation")
    try:
        logging.info("Stopping Simulation")
        simulationObj.stopSimulation()
        sleep(3)

        try:
            simulationObj.startSimulation()
            logging.info("Successfully re-started the simulation")
        except:
            logging.warning("Simulation Could not be re-started")

    except:
        logging.warning("Simulation could not be stopped")


