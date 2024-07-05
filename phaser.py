#phaser guitar effects
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

#data to be use in the difference equation
MaxValue = 2**15-1
var = 0.05
var1 = 2*var
blockLen= 64
minfrequency = 50
maxfrequency = 1000
fw = 50 # fw can't be equal or larger than 200 or it will complied error
#error
# fw = 200
de = fw/Rate

x1 = 0
x2 = 0
y11 = 0
y12 = 0


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



Fc = np.arange(start=minfrequency, stop=maxfrequency, step=de)
while len(Fc) < maxfrequency:
    Fc = np.concatenate([Fc, Fc[::-1]])

Fc = Fc[0:SignalLength]


for i in range(0, SignalLength):
    
    inBytes = wf.readframes(1)
    inTuple = struct.unpack('h', inBytes)  
    inValue = inTuple[0]/MaxValue  # Number

    # Set input to difference equation
    x0 = inValue

    # Difference equation
    c = ((math.tan(2 * math.pi * Fc[i] / Rate) - 1) / (math.tan(2 * math.pi * Fc[i] / Rate) + 1))
    d = (-math.cos(math.pi * Fc[i] / Rate))
    y1 =( -c * x0) + d * (1-c) * x1 + x2 - d * (1-c) * y11 + c * y12
   

   # y0 = (x0 - y1) * 0.5

    y0 = (x0-y1) *0.5
    y12 = y11
    y11 = y1
    x2 = x1
    x1 = x0

    yOut = y0*MaxValue
    yOut = np.clip(yOut, -MaxValue, MaxValue)
    output = struct.pack('h', int(yOut))  # 'h' for 16 bits
    stream.write(output)

print('* Finished')

stream.stop_stream()
stream.close()
p.terminate()
