#DEPRECATED


class Event:
	def __init__(self, deltaTime, eventTypeValue, midiChannel, paramOne, paramTwo):
		self.deltaTime = deltaTime
		self.eventTypeValue = eventTypeValue
		self.midiChannel = midiChannel
		self.paramOne = paramOne
		self.paramTwo = paramTwo

	def __str__(self):
		returnString = "deltaTime: " + str(self.deltaTime) + "\n" + \
						"eventTypeValue: " + str (self.eventTypeValue) + "\n" + \
						"midiChannel: " + str(self.midiChannel) + "\n" + \
		 				"paramOne: " + str(self.paramOne) + "\n" + \
		 				"paramTwo: " + str(self.paramTwo)
		return returnString