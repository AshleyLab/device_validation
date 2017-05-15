data=open('energy.txt','r').read().split('\n')
while '' in data:
    data.remove('')
pos=open('watch_positions.txt','r').read().split('\n')
while '' in pos:
    pos.remove('')

pos_dict=dict()
for line in pos[1::]:
    tokens=line.split('\t')
    subject=tokens[0]
    device=tokens[1]
    arm=tokens[2]
    pos=tokens[3]
    if subject not in pos_dict:
        pos_dict[subject]=dict()
    pos_dict[subject][device]=[arm,pos]
outf=open('energy.pos.txt','w')
header=data[0]+'\tArm\tPos\n'
outf.write(header)
for line in data[1::]:
    tokens=line.split('\t')
    subject=tokens[0]
    device=tokens[2].split('_')[0]
    if subject in pos_dict:
        if device in pos_dict[subject]:
            outf.write(line+'\t'+pos_dict[subject][device][0]+'\t'+pos_dict[subject][device][1]+'\n')
        else:
            outf.write(line+'\tNA\tNA\n')
            
