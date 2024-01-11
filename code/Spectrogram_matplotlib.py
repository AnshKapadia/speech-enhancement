#Necessary imports 
import  numpy  as  np
import matplotlib.pyplot as plt
import scipy as sp

#converting .wav audio file to numpy array
fs, aud = sp.io.wavfile.read('..\data\whistle_1.wav')

#computing the stft of our audio clip as well as plotting the spectrogram
stft, freq, time, spec = plt.specgram(aud,Fs = fs,cmap='magma')
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.colorbar()
plt.show()

