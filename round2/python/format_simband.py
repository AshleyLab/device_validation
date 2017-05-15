import sys
import json
import datetime
import pytz

data=open(sys.argv[1],'r').read().strip()
data=json.loads(data)
data=data['data']
outf=open(sys.argv[2],'w') 
print(len(data))
entries=dict() 
for entry in data:
    datatype=entry['data']['payload']['field']
    #print datatype
    if datatype=="heartRateCollection":
        ts=int(entry['ts'])/1000
        dt=datetime.datetime.fromtimestamp(ts)
        curtime=datetime.datetime.strftime(dt,"%Y%m%d%H%M")
        #timezonelocal=pytz.timezone('US/Pacific')
        #utc=pytz.utc
        #timeLocal=utc.localize(dt).astimezone(timezonelocal)
        value=entry['data'][datatype]
        entries[curtime]=value
keys=entries.keys()
keys.sort()
for key in keys: 
    outf.write(key+'\t'+str(entries[key])+'\n')
    
    
