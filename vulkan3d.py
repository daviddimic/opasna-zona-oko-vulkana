#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')
line, = ax.plot([], [], lw=2)

# Podesavanja koordinatnih osa
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_zlim(0, 2.5)
# z-osa
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Parametri kosog hica
g = 9.81
v0 = 3
h = 1.5
# Kljucne tacke maksimuma
Hmax = h + v0**2/(2*g)
Dmax_sq = (v0**2/g)**2 + 2*h*v0**2/g
Dmax = np.sqrt(Dmax_sq)

y = np.zeros(100)

def plot_podnozje():
    t = np.linspace(0, 2*np.pi, 100)
    x = Dmax*np.cos(t)
    z = Dmax*np.sin(t) 
    ax.plot(x, z, y, label = 'podnozje')

def plot_hitac(alpha):
    """
    Iscrtavanje parabole kosog hica u x-z ravni sa uglom alpha
    """
    #Dt - vreme kada telo pada na zemlju
    Dt = (v0*np.sin(alpha) + np.sqrt((v0**2)*(np.sin(alpha))**2 + 2*g*h))/g
    t = np.linspace(0, Dt, 100)
    x = v0*t*np.cos(alpha)
    z = v0*t*np.sin(alpha) - g*t**2/2 + h
    ax.plot(x, y, z)

def plot_parabola():
    """
    Crtanje parabole opasne oblasti u x-z ravni
    """
    x = np.linspace(-Dmax,Dmax,100)
    z = -(Hmax/Dmax_sq)*x**2 + Hmax
    ax.plot(x, y, z, label = 'granica oblasti u x-z ravni')

def plot_paraboloid():
    """
    Iscrtavanje paraboloida opasne oblasti
    """
    X = np.arange(-Dmax, Dmax, 0.1)
    Y = np.arange(-Dmax, Dmax, 0.1)
    X, Y = np.meshgrid(X, Y)
    Z = Hmax - (X**2 + Y**2)/(Dmax_sq/Hmax)
    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, 
                            linewidth=0, antialiased=False, 
                            alpha=0.3)
    # color bar
    fig.colorbar(surf, shrink = 0.5, aspect = 5)

plot_podnozje()
plot_paraboloid()
plot_parabola()
plot_hitac(np.pi/1.8)
plot_hitac(np.pi/2)
plot_hitac(np.pi/4)
plot_hitac(np.pi/6)
plot_hitac(np.pi)

ax.legend(loc='upper left')
plt.show()
