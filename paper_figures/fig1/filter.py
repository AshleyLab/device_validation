d1=open('walk.hr.raw.csv','r').read().strip().split('\n')
d2=open('bike.hr.raw.csv','r').read().strip().split('\n')
d3=open('walk.en.raw.csv','r').read().strip().split('\n')
d4=open('bike.en.raw.csv','r').read().strip().split('\n')

outf_1=open('walk.hr.formatted.csv','w')
outf_2=open('bike.hr.formatted.csv','w')
outf_3=open('walk.en.formatted.csv','w')
outf_4=open('bike.en.formatted.csv','w')

#create filtered dictionary!
hr_walk=dict()
all_counts=[] 
for line in d1:
    counts=0 
    tokens=line.split('\t')
    hr_walk[tokens[0]]=[]
    for i in range(1,len(tokens)):
        if tokens[i]!="4": 
            hr_walk[tokens[0]].append(tokens[i])
            counts+=1
    all_counts.append(counts)
mincount=min(all_counts)
devices=hr_walk.keys()
outf_1.write('\t'.join(devices)+'\n')
for i in range(mincount):
    for d in devices:
        if d==devices[0]: 
            outf_1.write(hr_walk[d][i])
        else:
            outf_1.write('\t'+hr_walk[d][i])
    outf_1.write('\n')


hr_walk=dict()
all_counts=[] 
for line in d2:
    counts=0 
    tokens=line.split('\t')
    hr_walk[tokens[0]]=[]
    for i in range(1,len(tokens)):
        if tokens[i]!="4": 
            hr_walk[tokens[0]].append(tokens[i])
            counts+=1
    all_counts.append(counts)
mincount=min(all_counts)
devices=hr_walk.keys()
outf_2.write('\t'.join(devices)+'\n')
for i in range(mincount):
    for d in devices:
        if d==devices[0]: 
            outf_2.write(hr_walk[d][i])
        else:
            outf_2.write('\t'+hr_walk[d][i])
    outf_2.write('\n')



hr_walk=dict()
all_counts=[] 
for line in d2:
    counts=0 
    tokens=line.split('\t')
    hr_walk[tokens[0]]=[]
    for i in range(1,len(tokens)):
        if tokens[i]!="4": 
            hr_walk[tokens[0]].append(tokens[i])
            counts+=1
    all_counts.append(counts)
mincount=min(all_counts)
devices=hr_walk.keys()
outf_2.write('\t'.join(devices)+'\n')
for i in range(mincount):
    for d in devices:
        if d==devices[0]: 
            outf_2.write(hr_walk[d][i])
        else:
            outf_2.write('\t'+hr_walk[d][i])
    outf_2.write('\n')


hr_walk=dict()
all_counts=[] 
for line in d3:
    counts=0 
    tokens=line.split('\t')
    hr_walk[tokens[0]]=[]
    for i in range(1,len(tokens)):
        if tokens[i]!="4": 
            hr_walk[tokens[0]].append(tokens[i])
            counts+=1
    all_counts.append(counts)
mincount=min(all_counts)
devices=hr_walk.keys()
outf_3.write('\t'.join(devices)+'\n')
for i in range(mincount):
    for d in devices:
        if d==devices[0]: 
            outf_3.write(hr_walk[d][i])
        else:
            outf_3.write('\t'+hr_walk[d][i])
    outf_3.write('\n')


hr_walk=dict()
all_counts=[] 
for line in d4:
    counts=0 
    tokens=line.split('\t')
    hr_walk[tokens[0]]=[]
    for i in range(1,len(tokens)):
        if tokens[i]!="4": 
            hr_walk[tokens[0]].append(tokens[i])
            counts+=1
    all_counts.append(counts)
mincount=min(all_counts)
devices=hr_walk.keys()
outf_4.write('\t'.join(devices)+'\n')
for i in range(mincount):
    for d in devices:
        if d==devices[0]: 
            outf_4.write(hr_walk[d][i])
        else:
            outf_4.write('\t'+hr_walk[d][i])
    outf_4.write('\n')

