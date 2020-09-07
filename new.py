import math as m
import matplotlib.pyplot as plt
import numpy as np
from physicalconstants import stefbol
from matplotlib.animation import FuncAnimation
fig, ax = plt.subplots()
planet, = plt.plot([],[],'r-',label='habitable zone',ms=3)

star_rad =13920000000 #float(input())
star_temp =5772 #float(input())
star_lumin = 4 * m.pi * star_rad**2 * stefbol * star_temp**4
S_inner = 4.19 * 10**(-8) * star_temp**2 - 2.319 * 10**(-4) + 1.268
rinner = m.sqrt(star_lumin/S_inner)
S_outer = 6.19 * 10**(-9) * star_temp**2 - 1.319 * 10**(-5) + 0.234
router = m.sqrt(star_lumin/S_outer)
r=13920000000000
rkoiper=750000000000000

fi = np.linspace(0, 2*np.pi, 1000)
a= 579092270000000
e=0.8056
b=a*m.sqrt(1-e**2)

xmerc=a*np.sin(fi)
ymerc=b*np.cos(fi)
x = r * np.cos(fi) - c
y = r * np.sin(fi)
x1 = rinner * np.cos(fi)
y1 = rinner * np.sin(fi)
x2 = router * np.cos(fi)
y2 = router * np.sin(fi)
x3 = rkoiper * np.cos(fi)
y3 = rkoiper * np.sin(fi)

plt.fill_between(x3, y3, color = 'b')
plt.fill_between(x2, y2, color = 'g')
plt.fill_between(x1, y1, color = 'r')
plt.fill_between(x, y, color = 'black')
plt.axis('equal')
plt.plot(x2,y2)
plt.plot(x1,y1)
plt.plot(x3,y3)
plt.plot(xmerc,ymerc,color= 'black',lw=3)
plt.show()
