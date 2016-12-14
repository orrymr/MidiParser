from binascii import hexlify
from event import Event

#This file contains methods for reading track events

#Takes in a byte val, and returns the decimal value 
def getDec(val):
    return int(hexlify(val), 16)

def getDecimalFromBinaryString(binaryString):
	return int(binaryString, 2)

# This method takes in the data from a track chunk and returns the next event
def readEvent(trackData):
	#1 - Get delta time
	deltaTime = getVariableLengthTime(trackData)

	#2 - Get event type value and midi channel
	eventTypeValue, midiChannel = getEventByte(trackData)

	#3 - Get first and second parameters
	paramOne, paramTwo = getParams(trackData)

	event = Event(deltaTime, eventTypeValue, midiChannel, paramOne, paramTwo)

	return event

#returns a tuple containing (paramOne, paramTwo) both in dec
def getParams(trackData):
	paramOne = trackData.read(1)
	paramTwo = trackData.read(1)
	return (getDec(paramOne), getDec(paramTwo))


#returns a tuple containing (eventType, channel)
def getEventByte(trackData):
	eventByte = trackData.read(1)
	binaryString = '{0:08b}'.format(getDec(eventByte))
	eventTypeDecimal = getDecimalFromBinaryString(binaryString[0:4] + "0000")
	channelDecimal = getDecimalFromBinaryString("0000" + binaryString[4:8])
	return (eventTypeDecimal, channelDecimal)

def getVariableLengthTime(trackData):
	timeBytes = getTimeBytes(trackData)
	binaryString = ""

	for timeByte in timeBytes:
		binaryString += '{0:08b}'.format(getDec(timeByte))

	#print (binaryString)
	return (getDecimalFromBinaryString(binaryString))

# Returns a tuple containing 1-4 bytes of deltaTime
def getTimeBytes(trackData):
	nextTimeByte = trackData.read(1)
	if (getDec(nextTimeByte) > 127):
		return (nextTimeByte, getTimeBytes(trackData)[0]) 
	else:
		return (nextTimeByte, )

# 