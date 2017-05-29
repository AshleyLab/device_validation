import pdb

def convert_state(state):
    if state=="walk1":
        return "walk1"
    if state=="walk2":
        return "walk2"
    if state=="run1":
        return "run1"
    if state=="run2":
        return "run2"
    if state=="bike1":
        return "bike1"
    if state=="bike2":
        return "bike2"
    if state.startswith('sit'):
        return 'sit'
    if state.startswith('max'):
        return 'max'
    else:
        return None 

batch1=open('Batch_1_full_dataset.tsv','r').read().strip().split('\n')
batch2=open('Batch_2_full_dataset.tsv.WITHENERGY','r').read().strip().split('\n')
placeholder="NA" # value to use instead of NA so that clustering in R and heatmap.2 is possible! 
#get the delta from gold standard for each activity

device_activity_mean=dict()
headerdict=dict() 

header1=batch1[0].split('\t')
state_index=header1.index('state')
subject_index=header1.index('subject') 
devices=set([])
metrics=set([])
subjects=set([]) 
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
#print str(headerdict)

for line in batch1[1::]:
    tokens=line.split('\t')
    curstate=convert_state(tokens[state_index])
    subject=tokens[subject_index].split('_')[0]
    subjects.add(subject) 
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
            device_error=(device_value-gold_standard_value)/gold_standard_value
            device_error=round(device_error,3)
            #device_error=abs(device_error)
            if subject not in device_activity_mean:
                device_activity_mean[subject]=dict() 
            if device not in device_activity_mean[subject]:
                device_activity_mean[subject][device]=dict()
            if metric not in device_activity_mean[subject][device]: 
                device_activity_mean[subject][device][metric]=dict()
            if curstate not in device_activity_mean[subject][device][metric]:
                device_activity_mean[subject][device][metric][curstate]=device_error
#repeat this same analysis for batch 2
#print str(device_activity_mean)
print "BATCH 2"
headerdict=dict() 

header1=batch2[0].split('\t')
state_index=header1.index('state')
subject_index=header1.index('subject')
devices_old=devices
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
    subject=tokens[subject_index].split('_')[0]
    subjects.add(subject) 
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
            device_error=(device_value-gold_standard_value)/gold_standard_value
            device_error=round(device_error,3) 
            #device_error=abs(device_error) 
            if subject not in device_activity_mean:
                device_activity_mean[subject]=dict() 
            if device not in device_activity_mean[subject]:
                device_activity_mean[subject][device]=dict()
            if metric not in device_activity_mean[subject][device]: 
                device_activity_mean[subject][device][metric]=dict()
            if curstate not in device_activity_mean[subject][device][metric]:
                device_activity_mean[subject][device][metric][curstate]=device_error


print("FORMATTING DATA FOR HEATMAP OUTPUT!!")
states=['sit','walk1','walk2','run1','run2','bike1','bike2','max'] 
#devices=device_activity_mean.keys()
#devices=devices.union(devices_old)
devices=['Apple','Basis','Fitbit','Microsoft','PulseOn','Mio','Samsung']

print str(devices)
#pdb.set_trace() 
subjects=list(subjects)

outf_hr=open('hr.heatmap.bySubject','w')
outf_hr.write('Subject')
for state in states:
    for device in devices:
        outf_hr.write('\t'+state+"_"+device)
outf_hr.write('\n')


print str(device_activity_mean['8']) 

for subject in subjects:
    outf_hr.write(subject) 
    for state in states:
        for device in devices:
            if device in device_activity_mean[subject]:
                try:
                    if state in device_activity_mean[subject][device]['HR']:
                        outf_hr.write('\t'+str(device_activity_mean[subject][device]['HR'][state]))
                    else:
                        outf_hr.write('\t'+placeholder)
                except:
                    outf_hr.write('\t'+placeholder)
            else:
                outf_hr.write('\t'+placeholder)
    outf_hr.write('\n')
    


outf_en=open('en.heatmap.bySubject','w')
outf_en.write('Subject')
for state in states:
    for device in devices:
        outf_en.write('\t'+state+"_"+device)
outf_en.write('\n')

for subject in subjects:
    outf_en.write(subject) 
    for state in states:
        for device in devices:
            if device in device_activity_mean[subject]:
                try:
                    if state in device_activity_mean[subject][device]['Energy']:
                        outf_en.write('\t'+str(device_activity_mean[subject][device]['Energy'][state]))
                    else:
                        outf_en.write('\t'+placeholder)
                except:
                    outf_en.write('\t'+placeholder) 
            else:
                outf_en.write('\t'+placeholder) 
    outf_en.write('\n')
    


