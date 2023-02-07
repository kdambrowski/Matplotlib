import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1, 100)  # tworzenie macierzy od <0 do 1 co 0,1>
y = np.ones(100)  # stworzenie macierzy z samych 1 x 100

fig, ax = plt.subplots(figsize=(18, 18))  # stworzenie kontenerka o wymiarach 15 x 15 cali
for i in x:
    plt.scatter(x, y * i, s=5, c='black')  # tworzy wykres kropkowy w którym każdy y(czyli 1)
    # jest mnożony 100 razy przez każdą liczbę tworząc macierz 100x100

for i in x[:20]:
    plt.scatter(0, i, c='red', s=20, marker='s')  # tworzy te czerwone kropki

for i in x[:15]:
    plt.scatter(0, i, c='yellow', s=100, alpha=.4, marker='s')  # tworzy to żółte podświetlenie

for i in x[-5:]:
    plt.scatter(y * i, x, c='orange', s=80, alpha=.2, marker='s')

for i in x[:85]:
    plt.scatter(x[-5], i, c='pink', s=80, alpha=.6, marker='s')

ax.set_title('Bayens Theory', fontsize=24)
ax.set_xlabel('Frequency', fontsize=14)
ax.set_ylabel('Propability of event', fontsize=14)

plt.show()