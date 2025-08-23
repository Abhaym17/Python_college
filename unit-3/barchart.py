#neccerey library for ploattinng(CHAR OR GRAPH)
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]
fig, ax = plt.subplots(figsize=(8, 5)) 
bars = ax.bar(x, y, color=["red","orange"], width=0.6, edgecolor='black')
ax.set_title('Fruit Sales in Q1', fontsize=16, fontweight='bold')
ax.set_xlabel('Fruit Type', fontsize=12)
ax.set_ylabel('Units Sold', fontsize=12)
ax.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()
