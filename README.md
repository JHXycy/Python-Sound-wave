# Python-Sound-wave
This project will implement 3 sounds of guitar effects. Which are the reverb, AM-tremolo, RM-tremolo effective as well. So to be able to complete this project, there are a couple python environments needed. 1. Math, 2.numpy , 3.pyaudio, 4,the wave instruction and 5. The struct instruction.  During this project I record down two of my favorite songs which are played by guitar so that you guys can listen to what the types of effects are like.  

 
Tremolo is an Italian term which means  trembling effect. When you are playing music it means that you are pressing a single note and it is repeated extremely rapidly.  For example, instruments such as guitar(although a pick is not really a  tremolo) , Mandolin, as well as the violin family (violin, viola, cello, and double bass)are  really typically used instruments that can make the tremolo sounds. 


For tremolo sounds. Amplitude Modulation is one signal that can change the gain or the amplitude of other ones.  For the information that I have, there are two types of Tremolo. The first one is AM_Tremolo and the second one is RM tremolo . One of the most specific differences between AM_Tremolo and RM tremolo is that AM_tremolo is used as the unipolar  modulation signals.  while RM_Tremolo is done as the bipolar modulation signals . On the other hand, one of the similarities with these two modulations is that we can represent them mathematically  almost the same, but when we used musical instruments to display the sound, we can clearly hear the differences between these two modulations. 

The most simple equation to represent basic tremolo is :
	Y(n) = x(n)*m(n)
With x(n) is equal to the input signal of the equations and m(n) is equal the changing signals.  For the typically sounds of the tremolo it will increase while the tremolo is changing. We also know that the frequency of the main tone is around 500 hz. The modulation signals can be can be represent by m(n), and the equation can represent be as: 
	m(n) = CosLFO + 1


The second one is Ring modulation tremolo, Ring modulation  tremolo is a modulation that to change the Amplitude of the one of the tone.In addition ,Multiplication of signals in the time domain is equivalent to convolution of spectra in the frequency domain.
The ring modulation is the audio modulation, we know that x(n) is multiplied by the sine wave and m(n), is the carrier frequency Fc so that we can implement the equation:
y(n) = m(n) * x(n);
If the modulator us also a sine wave with the frequency, fx then we can hear the sum and the differences frequency is : fc + fx and fc - fx . 
The equation of m(n) = cos(cn) and also the equation x(n)=cos(n). this is one of the sample transfer function to show the ring modulation 




Both of these modulations will be using a python program to represent.



For phrase effects play a really critical role in how the sounds are mixed together. The phaser sound is used to add sonic interest to audio signals. The phaser effect sounds allow us to manipulate the phase and control and distinct the modulation effect. 
One of the simple transfer function to show is this :
Show the phrase effects by simple difference function is : Y(n) = 0.5(x(n) y1(n).
For y1(n) we will use this equation to represent: y1(n)= -cx(n) +d(1-c)x(n-1)+x(n-1)+x(n-2)-d(1-c)y1(n-1)+ cy1(n-2）
In order to present this equation, we have to define c and d by these other equations. 
c = tan(2fcfs)-1tan(2fcfs)+1 .,  d = -cos(2fcfs)  By those two equations, we can use a python program to represent it.  Fs =Rate (For my own phaser effects, my fw can’t be over 200 because once it reach 200 it will exceed the limited so that while testing, please not put above 200)







Conclusion : 
For this project, I showed 3 examples of guitar sound effects by using different equations. There are Both tremolo and Phaser effects. I think the most difficult part for me during this project is understanding the equations and converting them into python code . In addition, even if I put the equations down properly I also need to be really careful about the range.If I exceed the range the guitar music would not be shown. Overall, i think this project is quite interesting and I am really enjoy it while i was working on it.

