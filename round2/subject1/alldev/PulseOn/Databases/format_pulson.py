import sys 
import datetime 
#fbData=open('/srv/gsfs0/projects/ashley/common/device_validation/fbData.csv','r').read().split('\n')
#while '' in fbData: 
#    fbData.remove('') 
#wellness=open('/srv/gsfs0/projects/ashley/common/device_validation/wellness.csv','r').read().split('\n')
wellness=open('pulseon2.csv').read().split('\n')
while '' in wellness: 
    wellness.remove('')
import pdb 
#tstart=sys.argv[1] 
#tstart=datetime.datetime.strptime(tstart,"%Y%m%d%H%M"); 
#tend=sys.argv[2] 
#tend=datetime.datetime.strptime(tend,"%Y%m%d%H%M"); 
#print str(tstart) 
#print str(tend) 
outf=open(sys.argv[1],'w') 
outf.write('Date\tHeartRate\tCalories\tSteps\n') 
entries=dict() 
numentries=dict() 
for line in wellness[1::]: 
    tokens=line.split('\t') 
    ts=int(tokens[0])/1000 
    dt=datetime.datetime.fromtimestamp(ts)
    print str(dt) 
    hr=float(tokens[1]) 
    if hr<15: 
        continue 
    steps=float(tokens[3])+float(tokens[5])+float(tokens[7])
    calories=float(tokens[8]) 
    curtime=datetime.datetime.strftime(dt,"%Y%m%d%H%M")
    #pdb.set_trace() 
    if curtime not in entries: 
        entries[curtime]=[hr,steps,calories] 
        numentries[curtime]=1 
    else: 
        entries[curtime][0]+=hr 
        entries[curtime][1]+=steps 
        entries[curtime][2]+=calories 
        numentries[curtime]+=1 
print str(numentries) 
timekeys=entries.keys() 
timekeys.sort() 
for key in timekeys: 
    timeval=key+'00-0700'
    meanhr=entries[key][0]/numentries[key] 
    meansteps=entries[key][1]/numentries[key] 
    meancal=entries[key][2]/numentries[key] 
    outf.write(timeval+'\t'+str(meanhr)+'\t'+str(meancal)+'\t'+str(meansteps)+'\n')
