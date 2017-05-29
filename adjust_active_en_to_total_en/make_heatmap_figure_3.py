import pdb

def make_metadata_dict(data):
    header=data[0].split('\t')
    metadata_dict=dict()
    for line in data[1::]:
        tokens=line.split('\t')
        subject=tokens[0]
        metadata_dict[subject]=dict()
        for i in range(1,len(tokens)):
            field=header[i]
            value=tokens[i]
            metadata_dict[subject][field]=value
    return metadata_dict 

def roza_shizgal(active_energy,subject_metadata):
    age=float(subject_metadata['Age'])
    height=float(subject_metadata['Height'])
    weight=float(subject_metadata['Weight'])
    sex=subject_metadata['Sex']
    
    if sex=="Male":
        bmr=88.362+(13.397*weight)+(4.799*height)-(5.677*age)
    elif sex=="Female":
        bmr=447.593+(9.247*weight)+(3.098*height)-(4.330*age)
    else:
        raise Exception("Invalid entry!:"+str(subject_metadata))
    return  (bmr/1440.0)+ active_energy



#Harris Benedict equation revised by Mifflin and St. Jeor in 1990
def harris_benedict(active_energy,subject_metadata):
    age=float(subject_metadata['Age'])
    height=float(subject_metadata['Height'])
    weight=float(subject_metadata['Weight'])
    sex=subject_metadata['Sex']    
    if sex=="Male":
        bmr=(10*weight)+(6.25*height)-(5*age)+5
    elif sex=="Female":
        bmr=(10*weight)+(6.25*height)-(5*age)-161
    else:
        raise Exception("Invalid entry!:"+str(subject_metadata))
    return (bmr/1440.0)+active_energy 



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

batch1=open('../raw_data/Batch_1_full_dataset.tsv','r').read().strip().split('\n')
batch2=open('../raw_data/Batch_2_full_dataset.tsv.WITHENERGY','r').read().strip().split('\n')
metadata1=open("../raw_data/Batch1_metadata.csv",'r').read().strip().split('\n')
metadata2=open("../raw_data/Batch2_metadata.csv",'r').read().strip().split('\n')
metadata=metadata1+metadata2[1::]
metadata_dict=make_metadata_dict(metadata)

#build metadata dictionary

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
            #get the corrected device value!!!
            roza_shizgal_corrected=roza_shizgal(device_value,metadata_dict[subject])
            harris_benedict_corrected=harris_benedict(device_value,metadata_dict[subject])
            device_error=(device_value-gold_standard_value)/gold_standard_value
            rs_device_error=(roza_shizgal_corrected-gold_standard_value)/gold_standard_value 
            hb_device_error=(harris_benedict_corrected-gold_standard_value)/gold_standard_value
            device_error=round(device_error,3)
            rs_device_error=round(rs_device_error,3)
            hb_device_error=round(hb_device_error,3)
            kcal_error=device_value-gold_standard_value
            rs_kcal_error=roza_shizgal_corrected-gold_standard_value
            hb_kcal_error=harris_benedict_corrected-gold_standard_value
            #device_error=abs(device_error)
            if subject not in device_activity_mean:
                device_activity_mean[subject]=dict() 
            if device not in device_activity_mean[subject]:
                device_activity_mean[subject][device]=dict()
            if metric not in device_activity_mean[subject][device]: 
                device_activity_mean[subject][device][metric]=dict()
            if curstate not in device_activity_mean[subject][device][metric]:
                device_activity_mean[subject][device][metric][curstate]=[device_error,rs_device_error,hb_device_error,kcal_error,rs_kcal_error,hb_kcal_error]
                
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
            roza_shizgal_corrected=roza_shizgal(device_value,metadata_dict[subject])
            harris_benedict_corrected=harris_benedict(device_value,metadata_dict[subject])
            device_error=(device_value-gold_standard_value)/gold_standard_value
            device_error=round(device_error,3)
            rs_device_error=(roza_shizgal_corrected-gold_standard_value)/gold_standard_value 
            hb_device_error=(harris_benedict_corrected-gold_standard_value)/gold_standard_value
            device_error=round(device_error,3)
            rs_device_error=round(rs_device_error,3)
            hb_device_error=round(hb_device_error,3)
            kcal_error=device_value-gold_standard_value
            rs_kcal_error=roza_shizgal_corrected-gold_standard_value
            hb_kcal_error=harris_benedict_corrected-gold_standard_value
            
            #device_error=abs(device_error) 
            if subject not in device_activity_mean:
                device_activity_mean[subject]=dict() 
            if device not in device_activity_mean[subject]:
                device_activity_mean[subject][device]=dict()
            if metric not in device_activity_mean[subject][device]: 
                device_activity_mean[subject][device][metric]=dict()
            if curstate not in device_activity_mean[subject][device][metric]:
                device_activity_mean[subject][device][metric][curstate]=[device_error,rs_device_error,hb_device_error,kcal_error,rs_kcal_error,hb_kcal_error]


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
        for metric in ['percent','kcal']: 
            for correction in ['uncorrected','RozaShizgal','HarrisBenedict']:
                outf_en.write('\t'+state+"_"+device+'_'+metric+'_'+correction)
outf_en.write('\n')

for subject in subjects:
    outf_en.write(subject) 
    for state in states:
        for device in devices:
            if device in device_activity_mean[subject]:
                try:
                    if state in device_activity_mean[subject][device]['Energy']:
                        outf_en.write('\t'+'\t'.join([str(i) for i in device_activity_mean[subject][device]['Energy'][state]]))
                    else:
                        outf_en.write('\t'+'\t'.join([placeholder]*3))
                except:
                    outf_en.write('\t'+'\t'.join([placeholder]*3)) 
            else:
                outf_en.write('\t'+'\t'.join([placeholder]*3)) 
    outf_en.write('\n')
    


