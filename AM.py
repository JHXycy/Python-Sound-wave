# guitar effect with Am modulation
import numpy as np
import pyaudio
import wave
import struct
import math

#open the wavefile being record
#(pick either one)
#this is the second orginal guitar sound

wavfile = '天黑.wav'
#wavfile = 'sunnyday.wav'
#wavfile = 'music.wav'

print('Play  wavefile %s.' % wavfile)

# Open wave file (mono channel)
wf = wave.open(wavfile, 'rb')

#wave file properties
Rate = wf.getframerate() #get the famerate
Channels = wf.getnchannels() # get channels
Width = wf.getsampwidth()  # bytes per sample
SignalLength = wf.getnframes()  #get the length

#to print infomrations that we want to see while running
print('the frame rate is %d frame/second' % Rate) #print rate
print('there is %d channels' %Channels) #show how many channel
print ('there is %d bytes per sample' %Width)# show bytes
print('the frams of this file is %d' %SignalLength) #show frame
p = pyaudio.PyAudio()



stream = p.open(
    format      = p.get_format_from_width(Width),
    channels    = Channels,
    rate        = Rate,
    input       = False,
    output      = True )

blcokLen = 64 # length
#try this
#blcokLen = 20 # as get lower more trumbling sounds. 
fw = 500
#fw = 1000
maxValue = 2** 15-1   #2^(15-1) max
al = 0.5 # for defer equation later use
# try another ai value. 
#al = 0.9 # as it goes higher more trumbling sounds

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





for i in range(0, int(SignalLength/blcokLen)):
    # Convert binary data to number
    inputBytes = wf.readframes(blcokLen) #the length of it.
    inputTuple = struct.unpack('h' * blcokLen, inputBytes)  

#Am modulation difference eq:
    outBlock = [int((1 + al * math.sin(2 * i* fw  * math.pi  / Rate)) * n) for n in inputTuple]

    y0out = np.clip(outBlock, -maxValue, maxValue) #this is to clip the file. 
    outString = struct.pack('h' * blcokLen, *y0out)  # 'h' for 16 bits
    stream.write(outString)




print('* Execution finished')



stream.stop_stream()
stream.close()
p.terminate()
