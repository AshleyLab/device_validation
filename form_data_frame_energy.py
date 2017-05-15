import sys
activity=open(sys.argv[1],'r').read().split('\n')
while '' in activity:
    activity.remove('')
metadata=open(sys.argv[2],'r').read().split('\n')
while '' in metadata:
    metadata.remove('')

#combine data frames!
outf=open(sys.argv[3],'w')
activity_header=activity[0].split('\t')
subject_index=activity_header.index('subject')
state_index=activity_header.index('state')
gs_index = activity_header.index('GoldStandard_Energy')
device_indices=[]
device_index_dict=dict() 
for i in range(len(activity_header)):
    if (activity_header[i].endswith('_Energy')) and (i!=gs_index):
        device_indices.append(i)
        device_index_dict[i]=activity_header[i]
print str(device_indices) 
subject_dict=dict()

for i in range(1,len(activity)): 
    tokens=activity[i].split('\t')
    subject=tokens[subject_index].split('_')[0] 
    state=tokens[state_index]
    if subject not in subject_dict:
        subject_dict[subject]=dict()
    makeRecord=False 
    #is this the last entry for this state?
    if i == (len(activity)-1):
        #yes
        makeRecord=True 
    else:
        next_state=activity[i+1].split('\t')[state_index] 
        if next_state!=state:
            makeRecord=True
    if makeRecord==False:
        continue
    #convert to known state
    if state.startswith('sit'):
        state='sit'
    elif state.startswith('walk'):
        state='walk'
    elif state.startswith('run'):
        state='run'
    elif state.startswith('bike'):
        state='bike'
    elif state.startswith('max'):
        state='max'
    else:
        continue #Not a valid state name!!
    if state not in subject_dict[subject]:
        subject_dict[subject][state]=dict()
    #get the delta for each watch!
    errors=[] 
    try: 
        goldstandard=float(tokens[gs_index]) 
    except:
        print "could not record gs value:"+str(tokens[gs_index])
        continue
    for j in device_indices:
        device_name=device_index_dict[j]
        try:
            measurement=float(tokens[j])
        except:
            print "could not record device measurement:"+str(tokens[j])
            continue
        error=goldstandard-measurement
        errors.append(error) 
        subject_dict[subject][state][device_name]=error
    if len(errors)==0:
            continue
    mean_error=sum(errors)/len(errors)
    subject_dict[subject][state]['device_mean']=mean_error
    subject_dict[subject][state]['gold_standard']=goldstandard 
print str(subject_dict) 
#Add in the metadata 
metadata_header=metadata[0].split('\t')
subject_index = metadata_header.index('ID')
for line in metadata[1::]:
    tokens=line.split('\t')
    subject=tokens[subject_index]
    #print str(subject) 
    if subject in subject_dict: 
        subject_dict[subject]['metadata']=tokens[1::]
#print str(subject_dict) 
#write the output file!
outf.write('Subject\tState\tDevice\tError\tGoldStandard\t'+'\t'.join(metadata_header[1::])+'\n')
for subject in subject_dict:
    for state in subject_dict[subject]:
        if state == 'metadata':
            continue 
        for device in subject_dict[subject][state]:
            if device !="gold_standard": 
                if 'metadata' not in subject_dict[subject]:
                    print subject + '\t'+str(subject_dict[subject])
                gs=subject_dict[subject][state]['gold_standard'] 
                outf.write(subject+'\t'+state+'\t'+device+'\t'+str(subject_dict[subject][state][device])+'\t'+str(gs)+'\t'+str('\t'.join(subject_dict[subject]['metadata']))+'\n')

