# -*- coding: utf-8 -*-

# This is a small python script that aims at validating a set of averaging algorithms for wrapped data on the interval [0,M[, where M is an integer

from math import floor,pi,atan
from cmath import exp,sqrt



### Custom Functions ###

def mod(a,b): # Modulo operator is redefined and wraps a in [0,b[
    return a-b*floor(a/b)

def angle(z): # Returns the phase of a complex number in [0,2*pi]
    x = z.real
    y = z.imag
    phi2 = atan(y/x)
    if (x>=0):
        if (y>=0):
            phi = phi2
        else:
            phi = 2*pi + phi2
    else:
        phi = pi + phi2
    return phi



### Algorithms ###

# Algorithm 1
def algo1(a,b,M): # We unwrap when the derivative exceeds a threshold
    c = mod((a+b+M*(abs(a-b)>(M/2)))/2,M)
    return mod(c,M)

# Algorithm 2
def algo2(a,b,M): # We center b around a to reintroduce the idea of cyclicity
    a2 = a
    b2 = mod(b+a+M/2,M)-a-M/2 # /!\ M/2 is changed in 0
    c2 = (a2+b2)/2
    c = mod(c2,M)
    return c

# Algorithm 3
def algo3(a,b,M): # We go a step further by using complex representation
    z1 = exp(1j*a*2*pi/M)
    z2 = exp(1j*b*2*pi/M)
    if (a+b==M) and (abs(a-b)<=M/2): # When the sum is congruent to M, we need to resolve an ambiguity
        c = M/2
    else:
        c = angle(sqrt(z1*z2))*M/(2*pi)
    return mod(c,M)



### Basic Tests Functions ###

# Checking custom modulo function
def testMod():
    print('\nTesting custom modulo function...')
    data = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    res = []
    for elt in data:
        res.append(mod(elt,3))
    print(data,'\n',res)
    return

# Checking custom Angle function
def testAngle():
    print('\nTesting custom angle function...')
    ref = [0, pi/6, pi/4, pi/3, pi/2, 2*pi/3, 3*pi/4, pi, 5*pi/4, 4*pi/3, 3*pi/2, 7*pi/4]
    for elt in ref:
        print(elt,angle(exp(1j*elt)))
    return

# Checking algorithms accuracy
def testAlgos():
    print('\nTesting algorithms...')
    M = 360
    data = [[0,10],[10,100],[160,200],[250,350],[10,340],[100,300],[355,5]]
    ref = [5,55,180,300,355,20,0]
    res1,res2,res3 = [],[],[]

    for pair in data:
        [a,b] = pair
        res1.append(algo1(a,b,M))
        res2.append(algo2(a,b,M))
        res3.append(algo3(a,b,M))

    print('REFERENCE ',ref,'\n','ALGO 1 ',res1,'\n','ALGO 2 ',res2,'\n','ALGO 3 ',res3)
    return


#testMod()
#testAngle()
testAlgos()



