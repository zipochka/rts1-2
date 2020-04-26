import numpy as np
import matplotlib.pyplot as plt
import time
#import seaborn as sns

n = 8
omega = 1100
rezXX=[]
rezXY=[]
for N in range (2,512):
    x = np.zeros(N)

    for i in range(1, n + 1):
        A = np.random.random()
        phi = np.random.random()

        for t in range(N):
            x[t] += A * np.sin(omega / i * (t + 1) + phi)

    Mx = np.sum(x) / N
    Dx = np.sum((x - Mx) ** 2) / (N - 1)

    n_R = N // 2 - 1
    start=time.time()
    Rxx = np.zeros(n_R)
    for tau in range(N // 2 - 1):
        for t in range(N // 2 - 1):
              Rxx[tau] += (x[t] - Mx) * (x[t + tau] - Mx) / (N - 1)
    end=time.time()+1
    rezXX.append(end-start)

    y = np.zeros(N)

    for i in range(1, n + 1):
    # a, phi = a_phi[i-1]
        a, phi = np.random.random(), np.random.random()
        for t in range(N):
            y[t] += a * np.sin(omega / i * (t + 1) + phi)

    n_R = N // 2 - 1
    start=time.time()
    Rxy = np.zeros(n_R)
    for tau in range(N // 2 - 1):
        for t in range(N // 2 - 1):
            Rxy[tau] += (x[t] - Mx) * (y[t + tau] - Mx) / (N - 1)
    end=time.time()+1
    rezXY.append(end-start)

rez=[]
for i in range(len(rezXX)):
    rez.append( rezXX[i]*100/rezXY[i])

plt.figure()
plt.title("rez")
plt.plot(range(2,512),rez)
plt.show()


