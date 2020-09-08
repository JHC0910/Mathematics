import numpy as np
import matplotlib.pyplot as plt


def derivative(f,a,mode,h=0.01):
    if mode == 1:
        return (f(a+h)-f(a-h))/(2*h)
    elif mode == 2:
        return (f(a+h)-f(a))/h
    elif mode == 3:
        return (f(a)-f(a-h))/h
    else:
        print("Error!!")
    

x = np.linspace(0,10,1000)
f = lambda x: np.exp(-x)*np.cos(3*x)
y = f(x)
dydxm = derivative(f,x,1)
dydxf = derivative(f,x,2)
dydxb = derivative(f,x,3)





plt.figure(figsize=(12,5))
plt.plot(x,y,label='y=f(x)')
plt.plot(x,dydxm,label="Central Difference y=f'(x)")
plt.plot(x,dydxf,label="forward Difference y=f'(x)")
plt.plot(x,dydxb,label="backwards Difference y=f'(x)")
plt.legend()
plt.grid(True)

plt.show()


