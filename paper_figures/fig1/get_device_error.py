data=open('../../AshleyLab_device_validation_study_data_matrix_ALL.csv','r').read().strip().split('\n')
header=data[0].split('\t')
target_device='Basis'
target_metric="en"
indices=[]
for i in range(len(header)):
    if header[i].__contains__(target_device):
        if header[i].__contains__(target_metric): 
            indices.append(i)
values=[]
for line in data[1:len(data)]: 
    tokens=line.split('\t')
    for index in indices:
        values.append(tokens[index])
outf=open(target_device+"_"+target_metric+".ALL.TASKS.csv",'w')
outf.write('\n'.join(values))

