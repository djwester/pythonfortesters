#For this activity use the data in the jsonperdata.json file and for
#each dictionary in the data section, compare the sum of averageResolve,
# averageConnect,averageTransfer and averageClosing to the averageTotal
#If the difference between the sum of all the other averages to the 
#average total is more than 1 second print out the difference along with the
#starting time stamp
import json

with open('jsonperfdata.json','r') as f:
    datastore = json.load(f)

for datapoint in datastore['data']:
    summation = datapoint['averageResolve'] + datapoint['averageConnect'] + datapoint['averageTransfer'] + datapoint['averageClosing']
    total = datapoint['averageTotal']
    if abs(summation-total) > 1:
        print ('At time %s:'%datapoint['startPeriod'])
        print ('The sum was %s and the total was %s\n'%(summation,total))