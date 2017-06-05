#splits the pulseon percent error values into two groups based on whether watch was one per arm or 2 per arm.
one_vs_two_arm=open("device_position.tsv",'r').read().strip().split('\n')
pulseon_errors=open('pulseon.tsv','r').read().strip().split('\n') 
outf=open('one_vs_two_arm_error_pulseon.tsv','w')

subject_split=dict()
subject_split['one']=dict()
subject_split['two']=dict() 

for line in one_vs_two_arm[1::]:
    tokens=line.split('\t')
    subject=tokens[0]
    device=tokens[1]
    one_arm=tokens[4]
    if device=="Pulseon":
        if one_arm=="x":
            subject_split['one'][subject]=1
        else:
            subject_split['two'][subject]=1

error_dict=dict()
error_dict['one']=[]
error_dict['two']=[]
for line in pulseon_errors:
   tokens=line.split('\t')
   subject=tokens[0]
   error=tokens[3]
   if subject in subject_split['one']:
       error_dict['one'].append(error)
   else:
       error_dict['two'].append(error)
outf.write('one'+'\t'+'\t'.join(error_dict['one'])+'\n')
outf.write('two'+'\t'+'\t'.join(error_dict['two'])+'\n')            
