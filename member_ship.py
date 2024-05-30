import matplotlib.pyplot as plt
import numpy as np


def triangular(x, a, b, c):
    return np.maximum(0, np.minimum((x - a) / (b - a), (c - x) / (c - b)))


def gaussian(x, mean, sigma):
    return np.exp(-0.5 * ((x - mean) / sigma) ** 2)


def trapezoidal(x, a, b, c, d):
    return np.maximum(0, np.minimum(np.minimum((x - a) / (b - a), (d - x) / (d - c)), 1))


x = np.linspace(0, 10, 500)

a_tri = 2
b_tri = 5
c_tri = 8
mean_gauss = 5
sigma_gauss = 1.5
a_trap = 1
b_trap = 3
c_trap = 7
d_trap = 9

triangular_membership = triangular(x, a_tri, b_tri, c_tri)
gaussian_membership = gaussian(x, mean_gauss, sigma_gauss)
trapezoidal_membership = trapezoidal(x, a_trap, b_trap, c_trap, d_trap)

plt.figure(figsize=(10, 6))
plt.plot(x, triangular_membership, label='Triangular')
plt.plot(x, gaussian_membership, label='Gaussian')
plt.plot(x, trapezoidal_membership, label='Trapezoidal')
plt.title('Membership Functions')
plt.xlabel('X')
plt.ylabel('Membership Degree')
plt.legend()
plt.grid(True)
plt.show()
