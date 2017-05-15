import sys 
import math 
import datetime

#dirname =sys.argv[1]
data=open(sys.argv[1],'r').read().strip().split('\n') 
tstart=sys.argv[2]
tstart=datetime.datetime.strptime(tstart,"%Y%m%d%H%M"); 
outf=open(sys.argv[3],'w')
outf.write('Date\tHeartRate\n')
hr_dict=dict() 
for line in data: 
    tokens=line.split('\t') 
    time=math.floor(float(tokens[0]))
    print str(line)
    hr=float(tokens[1]) 
    if hr < 20: 
        continue 
    if time not in hr_dict: 
        hr_dict[time]=[hr]
    else: 
        hr_dict[time].append(hr) 
    
timevals=hr_dict.keys() 
timevals.sort() 
for val in timevals: 
    meanhr=sum(hr_dict[val])/len(hr_dict[val])
    ts=tstart+datetime.timedelta(minutes=val) 
    tstring=datetime.datetime.strftime(ts,"%Y%m%d%H%M")
    outf.write(tstring+'00-0700'+'\t'+str(meanhr)+'\n')

