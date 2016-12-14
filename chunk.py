class Chunk:
	def __init__(self, chunkId, chunkSize):
		self.chunkId = chunkId
		self.chunkSize = chunkSize

	def __str__(self):
		return "Chunk Id: " + str(self.chunkId) + "\nChunk Size: " + str(self.chunkSize)
