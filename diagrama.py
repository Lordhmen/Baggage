import tkinter as tk

import matplotlib
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.pyplot import Figure

from data_base import *

matplotlib.use('TkAgg')  # choose backend
root = tk.Tk()
root.title('Диаграмма')
# fra = tk.Frame(root, width=1000, height=1000, bg='#fff')
# fra.pack()
top = tk.Frame(root)
top.pack()
fig = matplotlib.pyplot.Figure(dpi=80)
# fig.set_figheight(10)
# fig.set_figwidth(10)
# fig.set_size_inches(6, 8)
canvas = FigureCanvasTkAgg(fig, top)
canvas.get_tk_widget().pack()
Gender = []
Sales = []
file = "data_base.txt"
data_base = create_date_base(file)
data_base.sort(key=lambda x: int(x[4]))
print(data_base)
h = 1
for i in data_base:
    # Gender.append(i[0] + " " + i[1] + " " + i[2])
    Gender.append(h)
    h += 1
    Sales.append(int(i[4]))
data = {
    'Gender': Gender,
    'Sales': Sales,
}
df = pd.DataFrame(data)
x = 'Gender'
y = 'Sales'
new_df = df[[x, y]].groupby(x).sum()
ax = fig.add_subplot(111)
# ax.set_title('Основы анатомии matplotlib')
# ax.set_xlabel('ось абцис (XAxis)')
# ax.set_ylabel('ось ординат (YAxis)')
# matplotlib.pyplot.xticks(ticks=Gender, rotation=50, horizontalalignment='left')
new_df.plot(kind='bar', legend=False, ax=ax)

root.mainloop()
