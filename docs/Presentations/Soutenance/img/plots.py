from cProfile import label
from turtle import color
import matplotlib.pyplot as plt
import numpy as np

"""baseline = [84.47, 87.77, 88.35, 89.07]
static = [79.69, 79.27, 84.23, 82.40]
pp_pswr = [85.10, 87.84, 89.23, 85.31]

baseline_com = [0, 0, 0, 0]
static_com = [73.99, 70.14, 66.77, 43.03]
pp_pswr_com = [79.42, 79.52, 77.28, 65.02]

width = 0.2

x = ["100", "400", "900", "1600"]

# Nbr of spikes

fig, ax = plt.subplots()
ax.bar(np.arange(4) - 0.3,baseline, width, label="Baseline", color="gray")
ax.bar(np.arange(4) - 0.1,static, width, label="Seuil statique", color="orange")
ax.bar(np.arange(4) + 0.1,pp_pswr, width, label="PP & DSWR", color="green")
#plt.ticklabel_format(useOffset=False)
plt.xticks(np.arange(4), x)
plt.xlabel("# neurones")
#for bars in ax.containers:
#    ax.bar_label(bars)
plt.ylabel("Taux de reconnaissance (%)")
ax.legend()
plt.title("Taux de reconnaissance")
plt.grid(linestyle = '--')
plt.savefig("Reconnaissance.svg")
#plt.show()


fig, ax = plt.subplots()
ax.bar(np.arange(4) - 0.3,baseline_com, width, label="Baseline", color="gray")
ax.bar(np.arange(4) - 0.1,static_com, width, label="Seuil statique", color="orange")
ax.bar(np.arange(4) + 0.1,pp_pswr_com, width, label="PP & DSWR", color="green")
#plt.ticklabel_format(useOffset=False)
plt.xticks(np.arange(4), x)
plt.xlabel("# neurones")
#for bars in ax.containers:
#    ax.bar_label(bars)
plt.ylabel("Compression (%)")
ax.legend()
plt.title("Taux de Compression")
plt.grid(linestyle = '--')
plt.savefig("Compression.svg")
#plt.show()"""


width = 0.2

x = ["1", "3"]

baseline = [85.31, 89.65]
static = [65.02, 80.80]

fig, ax = plt.subplots()
ax.bar(np.arange(2) - 0.1,baseline, width, label="Taux de reconnaissance", color="orange")
ax.bar(np.arange(2) + 0.1,static, width, label="Taux de Compression", color="green")
#plt.ticklabel_format(useOffset=False)
plt.xticks(np.arange(2), x)
plt.xlabel("Périodes d'entraînement")
#for bars in ax.containers:
#    ax.bar_label(bars)
plt.ylabel("Pourcentage (%)")
ax.legend()
plt.title("Performance et taux de compression (1600 neurones)")
plt.grid(linestyle = '--')
plt.savefig("Compression1600.svg")
#plt.show()