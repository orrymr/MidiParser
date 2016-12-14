from trackEvent import TrackEvent

class SysexEvent(TrackEvent):
	def __init__(self, deltaTime, eventType, midiChannel, length, data):
		super().__init__(deltaTime, eventType, midiChannel)
		self.length = length
		self.data = data

	def __str__(self):
		return super().__str__() + "\nLength " + str(self.length) + "\nData: " + str(self.data)