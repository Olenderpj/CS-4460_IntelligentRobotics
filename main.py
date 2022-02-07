import math
import signal

from Robot import *
from controls import *
from Utils import *
from zmqRemoteApi import RemoteAPIClient

client = RemoteAPIClient()
sim = client.getObject('sim')

# Stop any existing simulations
sim.stopSimulation()
sleep(1)

clientID = sim.startSimulation()
print("Client ID: ", clientID)

if clientID != -1:
    logging.warning("[Connection]: Connection to CopelliaSim via zmqAPI successful")
else:
    logging.warning("[Connection]: Connection was unsuccessful")

# Robot follows a square path
def square():
    while True:
        pioneer.setBothMotorsToSameVelocity(.5)
        sleep(5)
        pioneer.stop()
        sleep(.5)
        pioneer.pivot(90, 1)


pioneer = Robot(sim)
square()

sleep(2)
sim.stopSimulation()
connectionMessage("Connection has successfully ended")
