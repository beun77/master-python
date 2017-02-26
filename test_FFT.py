from math import *
import numpy as np
import matplotlib.pyplot as plt


def FFT(X,L,direction): # Cooley-Tukey DFT algorithm

    # We first pad the signal to a power of two length for improved performances
    L = 2**(ceil(log2(L)))
    X = np.append(X,np.zeros((1,L-X.size)))
    print(X)
    Y = np.zeros(L,dtype=np.complex64)


    print(L)
    indexes = range(0,L)
    for k in indexes:

        if L > 2: # We split the computation into two smaller DFTs
            
            Ek = FFT(X[0:L-1:2],floor(L/2),direction)
            Ok = FFT(X[1:L:2],floor(L/2),direction)
            
            # And we use use symmetry considerations when storing the result
            if direction == 'direct':
                Y[] = Ek+Ok
                Y[+floor(L/2)] = Ek - Ok*np.exp(1j*2*pi*K/floor(L/2))
            elif direction == 'inverse':
                Y[] = Ek+Ok
                Y[+floor(L/2)] = Ek + Ok*np.exp(1j*2*pi*K/floor(L/2))
            else:
                raise NameError('Unsupported direction')
            indexes.remove(k)
            indexes.remove(k+floor(L/2))

        else: # We compute the elementary DFT
            
            N = np.linspace(0,L-1,L)
            for k in range(0,L):
                if direction == 'direct':
                    Y[k] = np.sum(X*np.exp(-1j*2*pi*N*k/L))
                elif direction == 'inverse':
                    Y[k] = np.sum(X*np.exp(1j*2*pi*N*k/L))/L
                else:
                    raise NameError('Unsupported direction')
    
    return Y


t = np.linspace(0,6,100)
X = np.sin(2*np.pi*t)*(1+.2*np.cos(75*pi*t))

Y = FFT(X,100,'direct')
Y = np.abs(FFT)

plt.plot(t,X)
plt.show()

plt.plot(Y)
plt.show()


