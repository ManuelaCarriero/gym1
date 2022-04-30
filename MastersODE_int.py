# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 10:39:07 2022

@author: asus
"""

"""
Master equations (i.e. ODE) system integration
for number of molecules N = 3
"""
############################Just to refresh the memory####################
from scipy.integrate import odeint
import numpy as np
#import matplotlib.pylab as plt
import matplotlib.pyplot as plt
import seaborn as sns

# derivative
def logistic(state, time, α, β):
    N = state
    δN = α*N - β*N**2
    return δN

# time steps
time = np.linspace(0, 1, 2**7+1)

# starting status
N0 = 0.1

# parameters
α = 10
β = 1

np.linspace(0, 1, 2**3+1)

res = odeint(logistic, y0=N0, t=time, args=(α, β))

res.shape

#sns.despine?

fig, ax = plt.subplots()
ax.plot(time, res, label="population")
ax.set_xlabel("time (a.u.)")
ax.set_ylabel("population (a.u.)")
ax.axhline(α/β, label='carrying capacity', color='gray', linewidth=3, linestyle='--')
ax.legend()
sns.despine(fig, trim=True, bottom=True, left=True)

##################################################

def Master_Equations(state, time, r1, r2, r3, g0, g1, g2):
    P0, P1, P2, P3 = state
    δP0 = r1*P1 - g0*P0
    δP1 = g0*P0 + r2*P2 -r1*P1 - g1*P1
    δP2 = g1*P1 + r3*P3 - r2*P2 - g2*P2
    δP3 = g2*P2 - r3*P3 
    return δP0, δP1,δP2, δP3

# time steps
time = np.linspace(0, 1, 2**7+1)

# starting status
state0 = (1.0, 0.001, 0.0, 0.0)

# parameters
r1 = 0.1
r2 = 0.3
r3 = 0.4
g0 = 100
g1 = 100
g2 = 100

res = odeint(Master_Equations, y0=state0, t=time, args=(r1, r2, r3, g0, g1, g2))

P0_hat, P1_hat, P2_hat, P3_hat = res.T

fig= plt.figure()
ax= fig.add_subplot(1,1,1)
ax.plot(time, P0_hat, label='$P_{0}$')
ax.plot(time, P1_hat, label='$P_{1}$')
ax.plot(time, P2_hat, label='$P_{2}$')
ax.plot(time, P3_hat, label='$P_{3}$')
ax.set_xlim(0.0,0.2)
ax.set_title(r'$r_1={}, r_2={}, r_3={}, g_0={}, g_1={}, g_2={}$'.format(r1, r2, r3, g0, g1, g2), 
          fontsize=15)
plt.legend()

# Try varying the parameters