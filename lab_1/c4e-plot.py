import matplotlib
matplotlib.use('tkAgg')

from matplotlib import pyplot

#1. prepare data
labels = ['Web', 'Ios', 'Android', 'react Native']
values = [40, 20, 25, 15]
colors = ['red', 'green', 'gold', 'purple']
explode = [0, 0.2, 0, 0.2]

#2. plot
pyplot.pie(values, labels=labels, colors=colors, explode=explode, shadow=True, autopct='%1.0f%%')
pyplot.axis('equal')



#3. show
pyplot.show()
