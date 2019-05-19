#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

# Parametri kosog hica
g = 9.81
v0 = 5
h = 1.5
# Kljucne tacke maksimuma
Hmax = h + v0**2/(2*g)
Dmax_sq = (v0**2/g)**2 + 2*h*v0**2/g
Dmax = np.sqrt(Dmax_sq)

def plot_tacke():
    ax.plot(0, Hmax, 'o', color='black', label = 'Hmax')
    ax.plot(Dmax, 0, 'o', color='red', label = 'Dmax')
    ax.plot(-Dmax, 0, 'o', color='blue', label = '-Dmax')

def plot_hitac(alpha):
    """
    Iscrtavanje parabole kosog hica sa uglom alpha
    i tackama kada dostize max visina i max domet
    """
    # Dt je vreme kada telo pada na zemlju
    Dt = (v0*np.sin(alpha) + np.sqrt((v0**2)*(np.sin(alpha))**2 + 2*g*h))/g
    t = np.linspace(0, Dt, 100)
    x = v0*t*np.cos(alpha)
    y = v0*t*np.sin(alpha) - g*t**2/2 + h
    
    # Tacke max visine i max dometa
    D = v0*np.cos(alpha)*Dt
    ax.plot(D, 0, 'o', label = 'D (%0.2g, %0.2g)' % (D, 0))
    Hx = v0**2*np.sin(2*alpha)/(2*g)
    Hy = h + v0**2*np.sin(alpha)**2/(2*g)
    ax.plot(Hx, Hy, 'o', label = 'H (%0.2g, %0.2g)' % (Hx, Hy))
    ax.plot(x, y, label = '%0.2f deg' % (alpha*180/np.pi))

def plot_parabola():
    """
    Crtanje parabole opasne oblasti
    """
    x = np.linspace(-Dmax,Dmax,100)
    y = -(Hmax/Dmax_sq)*x**2 + Hmax
    ax.plot(x, y, label = 'granica oblasti')

plot_tacke()
plot_parabola()
plot_hitac(np.pi/2)
plot_hitac(np.pi/3)
plot_hitac(np.arctan(1/np.sqrt(1+2*h*g/v0**2)))
plot_hitac(np.pi/4)

ax.legend(loc='upper right')
plt.show()
