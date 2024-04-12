import matplotlib.pyplot as plt
import numpy as np

y = lambda x: 2*x**6-8*x**3+9*x**2+54*x-3
print("y:", y)
x = np.linspace(-5, 5, 42)
print(' x y(x)')
for temp in x :
    print ( temp, y(temp))

xmax = max(x,key=y)
print('Xmax = ',xmax,end=' ')

fmax = max(y(x))
print('Ymax = ',fmax)

xmin = min(x,key=y)
print('Xmin = ',xmin,end=' ')

fmin = min(y(x))
print('Ymin = ',fmin)


fig = plt.subplots()


plt.plot(x, y(x))


plt.show()