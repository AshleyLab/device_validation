def convert_state(state):
    if state.startswith('walk'):
        return 'walk'
    if state.startswith('run'):
        return 'run'
    if state.startswith('sit'):
        return 'sit'
    if state.startswith('bike'):
        return 'bike'
    if state.startswith('max'):
        return 'max'
    else:
        return None 

batch1=open('Batch_1_full_dataset.tsv','r').read().strip().split('\n')
batch2=open('Batch_2_full_dataset.tsv.WITHENERGY','r').read().strip().split('\n')
#get the delta from gold standard for each activity

device_activity_mean=dict()
headerdict=dict() 

header1=batch1[0].split('\t')
state_index=header1.index('state')
devices=set([])
metrics=set([])

for i in range(len(header1)):
    token=header1[i] 
    token=token.split('_')
    if len(token)>1:
        #keep it!
        device=token[0]
        devices.add(device) 
        metric=token[1]
        if metric=="Steps":
            continue #must skip, have no gold standard 
        metrics.add(metric) 
        if device not in headerdict:
            headerdict[device]=dict()
        if  device in headerdict:
            headerdict[device][metric]=i
print str(headerdict)

for line in batch1[1::]:
    tokens=line.split('\t')
    curstate=convert_state(tokens[state_index])
    if curstate==None:
        continue 
    for metric in metrics: 
        gold_standard_index=headerdict['GoldStandard'][metric]
        gold_standard_value=tokens[gold_standard_index]
        if gold_standard_value=="NA":
            continue 
        gold_standard_value=float(gold_standard_value) 
        for device in devices:
            if device=="GoldStandard":
                continue
            device_index=headerdict[device][metric]
            device_value=tokens[device_index]
            if device_value=="NA":
                continue
            device_value=float(device_value)
            if gold_standard_value==0:
                continue 
            device_error=abs(device_value-gold_standard_value)/gold_standard_value
            if device not in device_activity_mean:
                device_activity_mean[device]=dict()
            if metric not in device_activity_mean[device]: 
                device_activity_mean[device][metric]=dict()
            if curstate not in device_activity_mean[device][metric]:
                device_activity_mean[device][metric][curstate]=[]
            device_activity_mean[device][metric][curstate].append(device_error)
#repeat this same analysis for batch 2
#print str(device_activity_mean)
print "BATCH 2"
headerdict=dict() 

header1=batch2[0].split('\t')
state_index=header1.index('state')
devices=set([])
metrics=set([])

for i in range(len(header1)):
    token=header1[i] 
    token=token.split('_')
    if len(token)>1:
        #keep it!
        device=token[0]
        devices.add(device) 
        metric=token[1]
        if metric=="Steps":
            continue #must skip, have no gold standard 
        metrics.add(metric) 
        if device not in headerdict:
            headerdict[device]=dict()
        if  device in headerdict:
            headerdict[device][metric]=i
print str(headerdict)

for line in batch2[1::]:
    tokens=line.split('\t')
    curstate=convert_state(tokens[state_index])
    if curstate==None:
        continue 
    for metric in metrics: 
        gold_standard_index=headerdict['GoldStandard'][metric]
        gold_standard_value=tokens[gold_standard_index]
        if gold_standard_value=="NA":
            continue 
        gold_standard_value=float(gold_standard_value) 
        for device in devices:
            if device=="GoldStandard":
                continue
            if metric not in headerdict[device]:
                continue     
            device_index=headerdict[device][metric]
            device_value=tokens[device_index]
            if device_value=="NA":
                continue
            device_value=float(device_value)
            if gold_standard_value==0:
                continue 
            device_error=abs(device_value-gold_standard_value)/gold_standard_value
            if device not in device_activity_mean:
                device_activity_mean[device]=dict()
            if metric not in device_activity_mean[device]: 
                device_activity_mean[device][metric]=dict()
            if curstate not in device_activity_mean[device][metric]:
                device_activity_mean[device][metric][curstate]=[]
            device_activity_mean[device][metric][curstate].append(device_error)

print("GETTING HEATMAP AVERAGES!!")
for device in device_activity_mean:
    for metric in device_activity_mean[device]:
        for state in device_activity_mean[device][metric]:
            #get the mean value!!
            values=device_activity_mean[device][metric][state]
            meanval=sum(values)/len(values)
            device_activity_mean[device][metric][state]=meanval 

print("FORMATTING DATA FOR HEATMAP OUTPUT!!")
states=['sit','walk','run','bike','max']
devices=device_activity_mean.keys()

outf_hr=open('hr.heatmap','w')
outf_hr.write('Device\t'+'\t'.join(states)+'\n')
for device in devices:
    outf_hr.write(device)
    for state in states:
        outf_hr.write('\t'+str(round(device_activity_mean[device]['HR'][state],3)))
    outf_hr.write('\n')
    

outf_en=open('energy.heatmap','w')
outf_en.write('Device\t'+'\t'.join(states)+'\n')
for device in devices:
    outf_en.write(device)
    for state in states:
        if 'Energy' in device_activity_mean[device]: 
            outf_en.write('\t'+str(round(device_activity_mean[device]['Energy'][state],3)))
        else:
            outf_en.write('\t')
    outf_en.write('\n')
    

