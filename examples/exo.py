import numpy as np
import matplotlib.pyplot as plt
import exopy

def nk_analytic(t, k: int, A: float, initial: float) -> float:
  f = 1.0 / (1 + A * t * initial / 2)
  nk = initial * f**2 * (1 - f)**(k - 1)
  return nk

t = np.logspace(start=np.log10(0.0001), stop=np.log10(100.0), num=1000)
nk = exopy.compute_nk_approx(steps=t, k_max=200, initial=200.0, A=0.001)

n_1 = nk[:, 1 - 1]
n_5 = nk[:, 5 - 1]
n_10 = nk[:, 10 - 1]
n_50 = nk[:, 50 - 1]

fig = plt.figure()
ax = plt.subplot(111)
plt.plot(t, n_1, 'g-', label='Numeric k=1')
plt.plot(t, nk_analytic(t, 1, A=0.001, initial=200.0), 'k-', label='Analytic k=1')
plt.plot(t, n_5, 'g-.', label='Numeric k=5')
plt.plot(t, nk_analytic(t, 5, A=0.001, initial=200.0), 'k-.', label='Analytic k=5')
plt.plot(t, n_10, 'g--', label='Numeric k=10')
plt.plot(t, nk_analytic(t, 10, A=0.001, initial=200.0), 'k--', label='Analytic k=10')
plt.plot(t, n_50, 'g:', label='Numeric k=50')
plt.plot(t, nk_analytic(t, 50, A=0.001, initial=200.0), 'k:', label='Analytic k=50')
ax.set_yscale('log')
ax.set_xscale('log')
ax.set_ylim(0.0000000001, 300)
ax.set_xlim(0.1, 100)
plt.xlabel('t')
plt.ylabel('$n_k$')
ax.grid()
plt.legend()

plt.show()
