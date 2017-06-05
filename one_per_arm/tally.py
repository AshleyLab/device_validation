#this script tallies the number of devices with one-per-arm vs two-per-arm
data=open('device_position.tsv','r').read().strip().split('\n')
counts=dict()
for line in data:
    tokens=line.split('\t')
    device=tokens[1]
    if device not in counts:
        counts[device]=dict()
        counts[device]['one']=0
        counts[device]['two']=0
    isone=tokens[4]
    if isone=="x":
        counts[device]['one']+=1
    else:
        counts[device]['two']+=1
outf=open('tally.tsv','w')
outf.write('Device\tOnePerWrist\tTwoPerWrist\n')
for device in counts:
    outf.write(device+'\t'+str(counts[device]['one'])+'\t'+str(counts[device]['two'])+'\n')
