class MidiFile:
	def __init__(self, headerChunk, *trackChunks):
		self.headerChunk = headerChunk
		this.trackChunks = []
		for (trackChunk in trackChunks):
			trackChunks.add(trackChunk)