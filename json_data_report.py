import json

#read in the data
with open('jsonperfdata.json','r') as f:
    datastore = json.load(f)

avgTransferTimes = []
avgConnectTimes = []
startingDateStamps = []
for datapoint in datastore['data']:
    avgTransferTimes.append(datapoint['averageTransfer'])
    avgConnectTimes.append(datapoint['averageConnect'])
    startingDateStamps.append(datapoint['startPeriod'])


with open('outputFile.csv','w') as f:
    f.write('time,avg transfer,avg connect\n')
    for time,transfer,connect in zip(startingDateStamps,avgTransferTimes,avgConnectTimes):
        f.write('%s,%s,%s\n'%(time,transfer,connect))