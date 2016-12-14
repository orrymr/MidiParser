class TrackChunk(Chunk):
	def __init__(self, chunkId, chunkSize, trackEventList):
		super().__init__(chunkId, chunkSize)
		self.trackEventList = trackEventList
