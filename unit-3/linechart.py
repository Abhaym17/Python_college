import matplotlib.pyplot as plt 

x = [0.1,0.2,0.6,0.8,0.9]
y = [50,60,80,90,20]

plt.plot ( x,y,marker="o", linestyle="--",markersize="8", markerfacecolor="orange", markeredgecolor="orange")
plt.xlabel('year')
plt.ylabel('sales')
plt.grid(True)
plt.show()