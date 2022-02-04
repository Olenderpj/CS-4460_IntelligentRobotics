from Pioneer_Paths import *

''' This class is mostly set up for a pioneer robot, but could be configured for others as well'''


class Robot:

    def __init__(self, sim, robotPath=PIONEER_ROBOT):
        self.sim = sim
        self.robotPath = robotPath
        self.entityHandle = self.sim.getObject(PIONEER_ROBOT)

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
        sensorReading = self.sim.readProximitySensor(sensorHandle)
        return sensorReading

    @staticmethod
    def __generateUltrasonicSensorPath(sensorNumber):
        return f'/ultrasonicSensor[{sensorNumber}]'
