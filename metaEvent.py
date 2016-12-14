from trackEvent import TrackEvent

class MetaEvent (TrackEvent):
	def __init__(self, deltaTime, typeMeta, length, text):
		super().__init__(deltaTime, typeMeta, -1)
		self.length = length
		self.text = text


	def __str__(self):
		return super().__str__() + "\nLength: " + str(self.length) + "\nText: " + str(self.text)