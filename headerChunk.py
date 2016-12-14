from chunk import Chunk

class HeaderChunk(Chunk):
	def __init__(self, chunkId, chunkSize, formatType, numTracks, timeDivision):
		super().__init__(chunkId, chunkSize)
		self.formatType = formatType
		self.numTracks = numTracks
		self.timeDivision = timeDivision

	def __str__(self):
		return super().__str__() + "\nFormat Type: " + str(self.formatType) + "\nNumber of Tracks " + str(self.numTracks) + "\nTime Division: " + str(self.timeDivision)

	def getNumTracks(self):
		return self.numTracks	