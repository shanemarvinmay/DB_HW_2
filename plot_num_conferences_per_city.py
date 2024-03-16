import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

plt.figure().set_figwidth(400)
plt.figure().set_figheight(800)
df = pd.read_csv('num_conference_per_city/num_conferences_per_city_sorted.txt', sep='\t', names=['City', 'Conferences'], header=None)
df = df.head(10)
colors = [
    (31, 119, 180),  # blue
    (255, 127, 14),  # orange
    (44, 160, 44),   # green
    (214, 39, 40),   # red
    (148, 103, 189), # purple
    (140, 86, 75),   # brown
    (227, 119, 194), # pink
    (127, 127, 127), # gray
    (188, 189, 34),  # olive
    (23, 190, 207),  # cyan
]
colors = [(r / 255., g / 255., b / 255.) for r, g, b in colors]
plot = df.plot(
    kind='bar', 
    x='City', 
    y='Conferences', 
    figsize=(40, 40), 
    linewidth=3,
    fontsize=40,
    color=colors,
    legend=False
)
plot.set_title('Conferences per City', fontdict={'fontsize':50})
plot.set_xlabel('City', fontdict={'fontsize':45})
plot.set_ylabel('Conferences', fontdict={'fontsize':45})

plt.savefig('num_conferences_per_city.pdf')