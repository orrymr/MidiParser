import os
from eventParser import *
from eventParser import getDec

os.chdir("/mnt/orrymr/data/Documents/stuff/Python Midi Parser")

midi = open("simpleMid.MID", 'rb')

#Header Chunk
MThd = midi.read(4) #first four bytes
header_length = midi.read(4) #next 4 bytes
format = midi.read(6)

#Track Chunk 1
MTrk1 = midi.read(4)
lengthChunk1 = midi.read(4)
print ("Length: " + str(getDec(lengthChunk1)))

print (readEvent(midi))
print ("********")
print (readEvent(midi))
print ("********")

print (readEvent(midi))
print ("********")

print (readEvent(midi))
print ("********")

print (readEvent(midi))
print ("********")

print (readEvent(midi))
print ("********")
# track1Data = midi.read(getDec(lengthChunk1))

#Track Chunk 2
# MTrk2 = midi.read(4)
# lengthChunk2 = midi.read(4)



# print (getVariableLengthTime(midi))
# print (getEventByte(midi))
# print (getParams(midi))
# print (midi.read(4))