import math

from Pioneer_Paths import *
from time import *
from UltrasonicSensorReading import *
from Utils import *

''' This class is mostly set up for a pioneer robot, but could be configured for others as well'''


class Robot:

    def __init__(self, sim, robotPath=PIONEER_ROBOT):
        self.sim = sim
        self.robotPath = robotPath
        self.entityHandle = self.sim.getObject(PIONEER_ROBOT)
        self.floorHandle = self.sim.getObject(FLOOR)

    def setLeftMotorVelocity(self, velocity):
        leftMotor = self.sim.getObject(PIONEER_LEFT_MOTOR)
        self.sim.setJointTargetVelocity(leftMotor, velocity)

    def setRightMotorVelocity(self, velocity):
        rightMotor = self.sim.getObject(PIONEER_RIGHT_MOTOR)
        self.sim.setJointTargetVelocity(rightMotor, velocity)

    def setBothMotorsToSameVelocity(self, velocity):
        self.setLeftMotorVelocity(velocity)
        self.setRightMotorVelocity(velocity)

    def readUltrasonicSensor(self, sensorNumber):
        sensorNumber = self.__generateUltrasonicSensorPath(sensorNumber)
        sensorHandle = self.sim.getObject(sensorNumber)
        sensorReading = UltraSonicSensorReading(self.sim.readProximitySensor(sensorHandle))
        return sensorReading

    #Still a bug here - hmmmmmm
    def pivotLeft90Degrees(self, velocity=.5, targetAngle=90):
        self.setRightMotorVelocity(velocity)

        currentEntityAngleDegrees = mapEntityOrientationFromRadiansToDegrees(self.getEntityAngle())
        while True:
            if currentEntityAngleDegrees[2] <= targetAngle:
                print("false", currentEntityAngleDegrees[2])
            else:
                print("True", currentEntityAngleDegrees[2])
                self.logMessageToSim(f"The Entity {self.entityHandle} has pivoted left by 90 degrees")
                self.setBothMotorsToSameVelocity(0)
                break
            currentEntityAngleDegrees = mapEntityOrientationFromRadiansToDegrees(self.getEntityAngle())

    def pivotRight90Degrees(self, velocity=.5, targetAngle=90):
        self.setLeftMotorVelocity(velocity)

        currentEntityAngleDegrees = mapEntityOrientationFromRadiansToDegrees(self.getEntityAngle())
        while True:
            if currentEntityAngleDegrees[2] <= targetAngle:
                print("false", currentEntityAngleDegrees[2])
            else:
                print("True", currentEntityAngleDegrees[2])
                self.logMessageToSim(f"The Entity {self.entityHandle} has pivoted right by 90 degrees")
                self.setBothMotorsToSameVelocity(0)
                break
            currentEntityAngleDegrees = mapEntityOrientationFromRadiansToDegrees(self.getEntityAngle())

    # roll = x, pitch = y, yaw = z
    def setEntityAngle(self, roll, pitch, yaw):
        self.sim.setObjectOrientation(self.entityHandle, self.floorHandle, [roll, pitch, yaw])

    def getEntityAngle(self):
        orientation = self.sim.getObjectOrientation(self.entityHandle, self.floorHandle)
        return orientation

    # Incomplete
    def getCenterOfTwoObjectsWithFrontSensor(self):
        leftReading = self.readUltrasonicSensor(3)
        rightReading = self.readUltrasonicSensor(4)

        # An object exists within the front of the robot
        if leftReading.distance is not None and rightReading.distance is not None:
            distanceFromCenterOfRobot = (leftReading.distance + rightReading.distance) / 2
            print(f"Center Distance:{distanceFromCenterOfRobot} meters")
            return distanceFromCenterOfRobot
        else:
            # nothing exists within 1 meter in front of the robot
            return 0

    def safeToMoveForward(self):
        nearestObject = self.getCenterOfTwoObjectsWithFrontSensor()
        self.logMessageToSim(f"Nearest Object: {nearestObject}m")

        if nearestObject == 0 or nearestObject > 0.3:
            return True
        else:
            return False

    # Not sure what to use this for
    def checkFrontDistance(self):
        leftSensorReading = self.readUltrasonicSensor(3)
        rightSensorReading = self.readUltrasonicSensor(4)

        print(leftSensorReading)
        print(rightSensorReading)

        distance = self.sim.checkDistance(self.entityHandle, leftSensorReading.detectedObjectHandle, 0)
        print("Dist", distance)

    def logErrorToSim(self, message):
        self.sim.addLog(self.sim.verbosity_errors, message)

    def logMessageToSim(self, message):
        self.sim.addLog(self.sim.verbosity_default, message)

    @staticmethod
    def __generateUltrasonicSensorPath(sensorNumber):
        return f'/ultrasonicSensor[{sensorNumber}]'
