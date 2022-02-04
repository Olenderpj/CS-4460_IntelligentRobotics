class UltraSonicSensorReading:

    def __init__(self, sensorReading):
        if sensorReading != 0:
            self.result, self.distance, self.detectedPoint, self.detectedObjectHandle, self.detectedSurfaceNormalVector = sensorReading
        else:
            self.result = None
            self.distance = None
            self.detectedPoint = None
            self.detectedObjectHandle = None
            self.detectedSurfaceNormalVector = None

    def __str__(self):
        return f"Result: {self.result}, " \
               f"Distance: {self.distance}, " \
               f"DetectedPoint: {self.detectedPoint}, " \
               f"DetectedObjectHandle: {self.detectedObjectHandle}, " \
               f"DetectedSurfaceNormalVector: {self.detectedSurfaceNormalVector}"
