# Ring modulation guitar effects
import numpy as np
import pyaudio
import wave
import math
import struct

wavfile = '天黑.wav'
#antoher guitar sound
#wavfile = 'sunnyday.wav'
#wavfile = 'music.wav'
print('Play file %s.' % wavfile)

# Open wave file (should be mono channel)
wf = wave.open( wavfile, 'rb' )

# Read the wave file properties
Rate           = wf.getframerate()     #get the famerate
Channels        = wf.getnchannels()     # get nums of channels
Width          = wf.getsampwidth()     #bytes per sample
SignalLength = wf.getnframes()  #get the length


#to print infomrations that we want to see while running
print('the frame rate is %d frame/second' % Rate) #print rate
print('there is %d channels' %Channels) #show how many channel
print ('there is %d bytes per sample' %Width)# show bytes
print('the frams of this file is %d' %SignalLength) #show frame

p = pyaudio.PyAudio()

# Open audio stream
stream = p.open(
    format      = p.get_format_from_width(Width), #get the width 
    channels    = Channels,
    rate        = Rate,
    input       = False,
    output      = True )

de= 4e-4
#try this and see the difference
#de =3e-4
maxV = 2**15-1  # Maximum allowed output signal value (because WIDTH = 2)
minfrequency = -0.8
maxfrequency = 0.9


BLOCKLEN = 64



#plt.ion() 
#plt.xlim(0, 2400)         # set x-axis limits
#plt.ylim(0, 150)
# plt.xlim(0, 2000)         # set x-axis limits
#plt.xlabel('Frequency (Hz)')
#f = Fs/BLOCKLEN * np.arange(0, BLOCKLEN)

#line, = plt.plot([], [], color = 'blue')  # Create empty line
#line.set_xdata(f)
# line.set_ydata(20 * np.log10(np.abs(X)))
#c = 0
#time = 10000



#while CONTINUE:
  #root.update()



  #om1 = 2.0 * pi * f1.get() / Fs
  #lineared_gain = gain.get() # record the  gain

# Open audio stream
# Use triangular wave
tri = np.arange(start=minfrequency, stop=maxfrequency, step=de)
while len(tri) < SignalLength:
    tri = np.concatenate([tri, tri[::-1]])

tri = tri[0:SignalLength]

for i in range(0, SignalLength): #list out a for loop
    # Convert binary data to number
    inBytes = wf.readframes(1)
    inTuple = struct.unpack('h', inBytes)  
    inValue = inTuple[0]/maxV  # inputValue calculation

    #  difference equation input
    x0 = inValue

    # Difference equation
    y0 = x0 * tri[i]

    yOut = y0*maxV #output calculation 
    yOut = np.clip(yOut, -maxV, maxV) #clip the file
    outString = struct.pack('h', int(yOut))  # 'h' for 16 bits
    stream.write(outString)

print('* Execution finish')

stream.stop_stream()
stream.close()
p.terminate()
