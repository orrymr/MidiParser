class TrackEvent:
	def __init__(self, deltaTime, eventType, midiChannel):
		self.deltaTime = deltaTime
		self.eventType = eventType
		self.midiChannel = midiChannel

	def __str__(self):
		return "Delta Time: " + str(self.deltaTime) + "\nEvent Type: " + str(self.eventType) + "\nMidi Channel: " + str(self.midiChannel)