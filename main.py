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

pioneer = Robot(sim)
pioneer.pivotLeft90Degrees()

sleep(5)
sim.stopSimulation()
connectionMessage("Connection has successfully ended")

# Degrees -> Radians
#   print(math.radians(45))

# Radians -> Degrees
# print(math.degrees(6.706922431476414e-05))
