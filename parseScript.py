midi = open("simpleMid.MID", 'rb')
#simple  #notes: 36, 37, 38, 39

#Header Chunk
MThd = midi.read(4) #first four bytes
header_length = midi.read(4) #next 4 bytes
format = midi.read(2)
#0 = single track file format 
#1 = multiple track file format 
#2 = multiple song file format (i.e., a series of type 0 files)
numTracks = midi.read(2)
division = midi.read(2)

print ("**********HEADER CHUNK*********")
print (MThd)
print ("lenght of header in bytes: ", getNum(header_length))
print ("format:", getNum(format))
print ("number of tracks:", getNum(numTracks))
print ("division: ", getNum(division), " ticks per beat")

#Track Chunk 1
print ("***********TRACK CHUNK 1 *************")
MTrk1 = midi.read(4)
lengthChunk1 = midi.read(4)
track1Data = midi.read(getNum(lengthChunk1))

print (MTrk1)
print ("Length of track 1: ", getNum(lengthChunk1)) 
print ("Track 1 data:")
for i in range(20):
    print (hex(track1Data[i]))
print("End of track 1 data")

#Track Chunk 2
print ("***********TRACK CHUNK 2 *************")
MTrk2 = midi.read(4)
lengthChunk2 = midi.read(4)
track2Data = midi.read(getNum(lengthChunk2))

print (MTrk2)
print ("Length of track 2: ", getNum(lengthChunk2))
print("###############################")
for i in range(getNum(lengthChunk2)):
    print (hex(track2Data[i]))