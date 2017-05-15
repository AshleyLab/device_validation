import sys
data=open(sys.argv[1],'r').read().strip().split('\n')
outf=open(sys.argv[2],'w') 
data_dict=dict()
header=data[0]
outf.write(header+'\n')

for line in data[1::]:
    tokens=line.split('\t')
    date=tokens[0][:-2]
    if date not in data_dict:
        data_dict[date]=tokens[1::] 
    else:
        if tokens.__contains__('NA'):
            continue
        data_dict[date]=tokens[1::]
keys=data_dict.keys()
keys.sort() 
for key in keys: 
    values=data_dict[key]
    outf.write(key+'\t'+'\t'.join([str(i) for i in values])+'\n')
    
            
    
