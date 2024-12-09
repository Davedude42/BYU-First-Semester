import re
import numpy as np
from matplotlib import pyplot as plt
from math import sqrt

with open('icarus.log', 'r') as file:
  text = file.read()
  
  dataStrings = re.findall("\\{.*\\}", text)

  data = [[float(n) for n in dataString[1:-1].replace(' ', '').split(',')] for dataString in dataStrings]

n = len(data)

t = []
y = []

dt = 0.1

def pythag(a, b, c):
  return sqrt(a**2 + b**2 + c**2)

magic_packet_n = 225

for i in range(275, n):
  t.append(float(i)*dt)

  data_point = data[i]
  norm_data_point = [n - data[magic_packet_n][j] for j, n in enumerate(data_point)]

  mag = pythag(*data_point[1:4])

  y.append([*data_point[1:4], mag])


plt.plot(t, y, "", label=["x", "y", "z", "mag"])
#plt.plot(t, vx, "", label="vx")
#plt.plot(t, rx, "", label="rx")
plt.legend(loc="upper left")
plt.show()