from pymongo import MongoClient
import matplotlib
matplotlib.use('tkAgg')
from matplotlib import pyplot
mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(mongo_uri)

db = client.get_default_database()

customers = db['customers']
#count ref:
num_of_customers = customers.find()
count_ads = 0
count_wom = 0
count_events = 0
for ref in num_of_customers:
    if ref['ref'] == 'ads':
        count_ads += 1
    elif ref['ref'] == 'wom':
        count_wom += 1
    else:
        count_events += 1
print('''Number of customers group by refs:

ads : {0}
wom : {1}
events : {2}
'''.format(count_ads, count_wom, count_events))

#draw pie chart:
labels = ["ads", "wom", "events"]
values = [count_ads, count_wom, count_events]


pyplot.pie(values, labels=labels, shadow=True, autopct='%.2f%%')
pyplot.suptitle('percentage of each reference', fontsize=16)
pyplot.axis('equal')
pyplot.show()
