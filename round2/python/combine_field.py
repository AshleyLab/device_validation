import sys
field=sys.argv[1]
files=sys.argv[2::]
print str(field)
print str(files)
allvals=dict()
devices=set()
for f in files:
    data=open(f,'r').read().strip().split('\n')
    header=data[0].split('\t')
    if field not in header:
        continue
    field_index=header.index(field)
    print str(f)+"\t"+str(field_index) 
    for line in data[1::]:
        tokens=line.split('\t')
        time=tokens[0]
        #print str(tokens) 
        val=tokens[field_index]
        if time not in allvals:
            allvals[time]=dict()
        allvals[time][f]=val
        devices.add(f)
        
outf=open(field+'.combined.txt','w')
devices=list(devices)
outf.write('TIME'+'\t'+'\t'.join([str(i) for i in devices])+'\n')
keys=allvals.keys()
keys.sort() 
for time in keys: 
    outf.write(time)
    for device in devices:
        if device in allvals[time]:
            outf.write('\t'+str(allvals[time][device]))
        else:
            outf.write('\t')
    outf.write('\n')
    
