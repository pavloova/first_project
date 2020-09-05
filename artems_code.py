import math as m
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import astro_constants as constants

star_rad = float(input())
star_temp = float(input())
star_lumin = 4 * constants.pi * star_rad**2 * constants.stef_bolz * star_temp**4
S_inner = 4.19 * 10**(-8) * star_temp**2 - 2.319 * 10**(-4) + 1.268
r_inner = m.sqrt(star_lumin/S_inner)
S_outer = 6.19 * 10**(-9) * star_temp**2 - 1.319 * 10**(-5) + 0.234
r_outer = m.sqrt(star_lumin/S_outer)

fig = plt.figure()
ax = fig.add_subplot(111)
line1, = ax.plot([], [], color = 'g')
line2, = ax.plot([], [], color = 'g')
#plan1, = ax.plot([], [], color = 'b')
#plan2, = ax.plot([], [], color = 'b')
#plan3, = ax.plot([], [], color = 'b')
#plan4, = ax.plot([], [], color = 'b')
#....
# вот здесь хотелось бы решить вопрос c произвольным количеством планет и звезд, пока не знаю как

def update1():
fi = np.linspace(0, 2*np.pi, 1000)
x1 = r_inner * np.cos(fi)
y1 = r_inner * np.sin(fi)
return x1, y1,

def update2():
fi = np.linspace(0, 2*np.pi, 1000)
x2 = r_outer * np.cos(fi)
y2 = r_outer * np.sin(fi)
return x2, y2

def animate(i):
x1, y1 = update1()
x2, y2 = update2()
line1.set_data(x1, y1)
line2.set_data(x2, y2)
ax.set_xlim(-60000000000000, 60000000000000)
ax.set_ylim(-60000000000000, 60000000000000)
#ax.axis('equal')
#zone, = ax.fill_between(x2, y1, y2, color = 'g') # данный объект должен отвечать за заполнение пространства межда двумя зелеными границами для отображения зоны обитаемости
ax.grid()
ax.set_title("Зона обитаемости")
return line1, line2 #zone
ani = animation.FuncAnimation(fig, animate, frames = 500, interval = 10)
ani.save("habitable_zone.mp4")
