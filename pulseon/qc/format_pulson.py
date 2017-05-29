import sys 
import datetime 
fbData=open('fbData.csv','r').read().strip().split('\n')
wellness=open("wellness.csv",'r').read().strip().split('\n')
outf=open('pulseon.extracted.values.txt','w') 
outf.write('Date\tfbDataHeartRate\tfbDataCalories\tfbDataCaloriesCumulative\twellnessHeartRate\twellnessCalories\n') 
entries=dict() 
for line in fbData[1::]:
    tokens=line.split(',') 
    ts=int(tokens[0])/1000 
    dt=datetime.datetime.fromtimestamp(ts)
    ts=datetime.datetime.strftime(dt,"%Y%m%d%H%M%S")        
    hr=tokens[1]
    en=float(tokens[2])
    cumulative_en=tokens[3]
    if hr>0:
        entries[ts]=dict()
        entries[ts]['fbDataHR']=hr
        entries[ts]['fbDataEN']=en
        entries[ts]['fbDataENCUM']=cumulative_en
for line in wellness[1::]:
    tokens=line.split(',')
    ts=int(tokens[0])/1000
    dt=datetime.datetime.fromtimestamp(ts)
    ts=datetime.datetime.strftime(dt,"%Y%m%d%H%M%S")        
    hr=tokens[1]
    en=float(tokens[8])
    if en > 0:
        if ts not in entries:
            entries[ts]=dict()
        entries[ts]['wellHR']=hr
        entries[ts]['wellEN']=en
timekeys=entries.keys() 
timekeys.sort() 
for key in timekeys: 
    outf.write(key)
    if 'fbDataHR' in entries[key]:
        outf.write('\t'+str(entries[key]['fbDataHR']))
    else:
        outf.write('\tNA')
    if 'fbDataEN' in entries[key]:
        outf.write('\t'+str(entries[key]['fbDataEN']))
    else:
        outf.write('\tNA')
    if 'fbDataENCUM' in entries[key]:
        outf.write('\t'+str(entries[key]['fbDataENCUM']))
    else:
        outf.write('\tNA')
    if 'wellHR' in entries[key]:
        outf.write('\t'+str(entries[key]['wellHR']))
    else:
        outf.write('\tNA')
    if 'wellEN' in entries[key]:
        outf.write('\t'+str(entries[key]['wellEN']))
    else:
        outf.write('\tNA')
    outf.write('\n')
    
