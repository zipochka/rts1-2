import numpy as np
import matplotlib.pyplot as plt
#import seaborn as sns

n = 8
omega = 1100
N = 256

x = np.zeros(N)

for i in range(1, n + 1):
    A = np.random.random()
    phi = np.random.random()

    for t in range(N):
        x[t] += A * np.sin(omega / i * (t + 1) + phi)

plt.figure(figsize=(8, 4))
plt.title("Pseudo-random variable")
plt.plot(range(N), x, "r")
# plt.scatter(range(N), x) plt.show()

Mx = np.sum(x) / N
Dx = np.sum((x - Mx) ** 2) / (N - 1)

plt.figure(figsize=(8, 4))
plt.title("Pseudo-random variable")
plt.plot(range(N), x, "r")  # random variable plt.plot(range(N), [Mx,]*N, "g")	# Mx
plt.plot(range(N), [Mx + np.sqrt(Dx), ] * N, "b")  # Upper sqrt(Dx)
plt.plot(range(N), [Mx - np.sqrt(Dx), ] * N, "b")  # Lower sqrt(Dx) plt.show()

n_R = N // 2 - 1
R = np.zeros(n_R)
for tau in range(N // 2 - 1):
    for t in range(N // 2 - 1):
          R[tau] += (x[t] - Mx) * (x[t + tau] - Mx) / (N - 1)

plt.figure(figsize=(8, 4))
plt.title("Autocorrelation function")
plt.plot(range(n_R), R, "r")  # random variable plt.show()

y = np.zeros(N)

for i in range(1, n + 1):
# a, phi = a_phi[i-1]
    a, phi = np.random.random(), np.random.random()
    for t in range(N):
        y[t] += a * np.sin(omega / i * (t + 1) + phi)

n_R = N // 2 - 1
Rxy = np.zeros(n_R)
for tau in range(N // 2 - 1):
    for t in range(N // 2 - 1):
        Rxy[tau] += (x[t] - Mx) * (y[t + tau] - Mx) / (N - 1)

plt.figure(figsize=(8, 4))
plt.title("Autocorrelation function")
plt.plot(range(n_R), Rxy, "r")  # random variable
plt.show()
