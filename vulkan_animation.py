#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')
line, = ax.plot([], [], lw=2)

# Podesavanja koordinatnih osa
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_zlim(0, 2)

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

def plot_paraboloid():
    """
    Iscrtavanje paraboloida nebezbedne oblasti
    """
    X = np.arange(-Dmax, Dmax, 0.1)
    Y = np.arange(-Dmax, Dmax, 0.1)
    X, Y = np.meshgrid(X, Y)
    Z = Hmax - (X**2 + Y**2)/(Dmax_sq/Hmax)
    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0,
                           antialiased=False, alpha=0.3)
    # color bar
    fig.colorbar(surf, shrink = 0.5, aspect = 5)

def init():
    """
    Inicijalizacija animacije
    """
    line.set_data([], [])
    line.set_3d_properties([])
    return line,

def animate(i):
    """
    Funkcija koja se poziva pri svakom frejmu animacije
    """
    alpha = i/100
    #Dt - vreme kada telo pada na zemlju
    Dt = (v0*np.sin(alpha) + np.sqrt((v0**2)*(np.sin(alpha))**2 + 2*g*h))/g
    t = np.linspace(0, Dt, 100)
    x = v0*t*np.cos(alpha)
    z = v0*t*np.sin(alpha) - g*t*t/2 + h

    line.set_data(x, y)
    line.set_3d_properties(z)
    line.set_color('red')
    return line,

def plot_parabola():
    """
    Crtanje parabole nebezbedne oblasti u x-z ravni
    """
    x = np.linspace(-Dmax,Dmax,100)
    z = -(Hmax/Dmax_sq)*x**2 + Hmax
    ax.plot(x, y, z, label = 'granica oblasti u x-z ravni')

# Animacija
anim = animation.FuncAnimation(fig, animate, init_func = init,
                               frames = 300, interval = 20, blit = True)

plot_podnozje()
plot_parabola()
plot_paraboloid()

ax.legend(loc='upper left')

# Cuvanje animacije u mp4 formatu
#anim.save('img/vulkan_animation.mp4', fps=60, extra_args=['-vcodec', 'libx264'])

plt.show()
