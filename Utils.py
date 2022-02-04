import logging
import math


def connectionMessage(message):
    logging.warning(f'[Connection]:{message}')


def mapEntityOrientationFromRadiansToDegrees(orientationObj):
    newOrientationList = []
    for i in range(len(orientationObj)):
        # Convert radians to degrees
        if orientationObj[i] < 0:
            result = math.degrees(orientationObj[i]) % -360
        else:
            result = math.degrees(orientationObj[i]) % 360

        # Adjust the result by 10000 if the string of the value contains an E
        # This might have to be adjusted later
        if "e" in str(orientationObj[i]):
            result = result * 100000
        newOrientationList.append(result)
    return newOrientationList
