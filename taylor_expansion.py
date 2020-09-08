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



def df(f,a,mode,n):
    if n == 0:
        return f(a)
    elif n == 1:
        return derivative(f,a,mode,h=0.01)
    elif n > 1:
        s0 = f
        for i in range(1,n+1):
            s1 = derivative(s0,a,mode,h=0.01)
            s0 = s1
            i += 1
            return s1


x = np.linspace(0,10,1000)
f = lambda x: x**2
y = f(x)

T1 = f(2)+df(f,2,1,1)*(x-2)
T2 = f(2)+df(f,2,1,1)*(x-2)+(df(f,2,1,2)/2)*(x-2)**2


plt.figure(figsize=(12,5))
plt.plot(x,y,label='y=f(x)')
plt.plot(x,T1,label="first-order approximation")
plt.plot(x,T2,label="second-order approximation")
plt.legend()
plt.grid(True)

plt.show()
