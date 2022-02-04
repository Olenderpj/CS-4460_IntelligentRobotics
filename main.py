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
pioneer.setLeftMotorVelocity(.5)

for i in range(10):
    print(pioneer.readUltrasonicSensor(4))


sleep(3)
sim.stopSimulation()
connectionMessage("Connection has successfully ended")