#!/usr/bin/python3

import numpy as np
from matplotlib import pyplot as plt

def bezier_curve(points, n, t):  
  if (n == 1):
    return (points[0])
  else:
    return (((1 - t) * bezier_curve(points[1:], n-1, t)[0]
            + t * bezier_curve(points[:-1], n-1, t)[0]),
            ((1 - t) * bezier_curve(points[1:], n-1, t)[1]
            + t * bezier_curve(points[:-1], n-1, t)[1]))

def bezier_call():
  p = [(100, 100), (250, 500), (400, 150), (500,400)]
  n = 4
  t = 0
  pfs = []
  while (t <= 1):
    pfs.append(bezier_curve(p, n, t))
    t += 0.01
  return pfs

data = np.array(bezier_call())
x,y = data.T
plt.scatter(x,y)
plt.show()
