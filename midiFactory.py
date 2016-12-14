import os
from headerChunk import HeaderChunk
from eventParser import getDec
from eventParser import getVariableLengthTime
from eventParser import getEventByte
from sysexEvent import SysexEvent
from metaEvent import MetaEvent

class MidiFactory:
	def __init__(self, directory, midiFile):
		os.chdir(directory)
		midi = open(midiFile, 'rb')

		self.addHeaderChunk(midi)
		# print (self.headerChunk)

		self.trackChunks = []
		self.addTrackChunk(midi)
		# for track in range(self.headerChunk.getNumTracks()):
		#  	print ("hello")

	def addHeaderChunk(self, midi):
		MThd = midi.read(4) 
		assert(MThd == b'MThd') #This makes sure that we're looking at a header chunk
		header_length = getDec(midi.read(4)) 
		format = getDec(midi.read(2))
		numTracks = getDec(midi.read(2))
		timeDivision = getDec(midi.read(2))

		self.headerChunk = HeaderChunk(MThd, header_length, format, numTracks, timeDivision)

	def addTrackChunk(self, midi):
		trackEvents = []
		MTrk = midi.read(4)
		assert (MTrk == b'MTrk') # Makes sure that we're looking at a track chunk
		
		dataLength = getDec(midi.read(4))
		print ("Length of current track: ", dataLength)

		nextEvent = self.readNextEvent(midi)
		trackEvents.append(nextEvent)
		print (nextEvent)
		
		print ("***********")
		nextEvent = self.readNextEvent(midi)
		trackEvents.append(nextEvent)
		print (nextEvent)

		print ("***********")
		nextEvent = self.readNextEvent(midi)
		trackEvents.append(nextEvent)
		print (nextEvent)

		print ("***********")
		nextEvent = self.readNextEvent(midi)
		trackEvents.append(nextEvent)
		print (nextEvent)

		# eventTypeValue, midiChannel = getEventByte(midi)
		# print (str(hex(eventTypeValue)))
		# print (str(midiChannel))
		# lengthMaybe = getVariableLengthTime(midi)
		# dataMaybe = midi.read(lengthMaybe)
		# print (lengthMaybe)
		# print (dataMaybe)
		
		# while nextEvent is not an end of track event:
		# 	nextEvent = readNextEvent(midi)
		# 	trackEvents.add(nextEvent)

	def readNextEvent(self, midi):
		#1 - Get delta time
		deltaTime = getVariableLengthTime(midi)

		#2 - Get event type value and midi channel
		#The below is for splitting a byte into event type and channel... not sure how to use it
		# eventTypeValue, midiChannel = getEventByte(midi)
		eventTypeValue = midi.read(1)
		print (eventTypeValue)

		if eventTypeValue == 0xf0 or eventTypeValue == 0xF7:
			length, data = self.readRestOfSysExEvent(midi)
			return SysexEvent(deltaTime, eventTypeValue, midiChannel, length, data)
		elif eventTypeValue == b'\xff':
			typeMeta, length, text = self.readRestOfMetaEvent(midi)
			return MetaEvent(deltaTime, typeMeta, length, text)

	def readRestOfMetaEvent (self, midi):
		typeMeta = midi.read(1)
		length = getVariableLengthTime(midi)
		text = midi.read(length)

		return (typeMeta, length, text)

	def readRestOfSysExEvent(self, midi):
		length = getVariableLengthTime(midi)
		data = midi.read(length)

		return (length, data)