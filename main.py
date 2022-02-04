from Robot import *
from controls import *
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

for i in range(1000):
    print(i, pioneer.readProximitySensor(4))


sleep(3)
sim.stopSimulation()
