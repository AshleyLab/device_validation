import numpy 
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

data=open("../AshleyLab_device_validation_study_data_matrix_ALL.csv",'r').read().strip().split('\n')
header=data[0].split('\t')
index_dict=dict()
for index in range(len(header)):
    token=header[index].split('_')
    if len(token)<3:
        continue
    metric=token[0]
    state=convert_state(token[1])
    device=token[2]
    if metric not in index_dict:
        index_dict[metric]=dict()
    if state not in index_dict[metric]:
        index_dict[metric][state]=dict()
    if device not in index_dict[metric][state]:
        index_dict[metric][state][device]=[index]
    else:
        index_dict[metric][state][device].append(index)
print "created index dict"
value_dict=dict()
#populate categories
for metric in index_dict:
    value_dict[metric]=dict()
    for state in index_dict[metric]:
        value_dict[metric][state]=dict()
        for device in index_dict[metric][state]:
            value_dict[metric][state][device]=[]

for line in data[1::]:
    tokens=line.split('\t')
    for metric in index_dict:
        for state in index_dict[metric]:
            for device in index_dict[metric][state]:
                for index in index_dict[metric][state][device]:
                    val=tokens[index]
                    if val!="NA":
                        value_dict[metric][state][device].append(abs(float(val)))
print "populated dictionary of values"
#take the medians!
for metric in value_dict:
    for state in value_dict[metric]:
        for device in value_dict[metric][state]:
            if len(value_dict[metric][state][device])>0: 
                median_val=numpy.median(value_dict[metric][state][device])
                value_dict[metric][state][device]=median_val
            else:
                value_dict[metric][state][device]="NA" 

print "got median values"
#format output files
states=['sit','walk','run','bike','max']
devices=["Apple","Basis","Fitbit","Microsoft","PulseOn","Mio","Samsung"]
outputf_header=["Device","Sitting","Walking","Running","Bicycle","Max"]
device_map=dict()
device_map["Apple"]="Apple Watch"
device_map["Basis"]="Basis Peak"
device_map["Fitbit"]="Fitbit Surge"
device_map["Microsoft"]="Microsoft Band"
device_map["PulseOn"]="PulseOn"
device_map["Mio"]="MIO Alpha 2"
device_map["Samsung"]="Samsung Gear S2"

for metric in value_dict:
    outf=open(metric+'.heatmap','w')
    outf.write('\t'.join(outputf_header)+'\n')
    for device in devices:
        outf.write(device_map[device])
        for state in states:
            outf.write("\t"+str(value_dict[metric][state][device]))
        outf.write('\n')
