#Roza and Shizgal in 1984
#weight in kilo
#height in cm
#age in years
import argparse

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


def parse_args():
    parser=argparse.ArgumentParser("Convert active calories to total calories")
    parser.add_argument("--raw_data")
    parser.add_argument("--metadata")
    parser.add_argument("--outf")
    return parser.parse_args() 

def make_metadata_dict(metadata_file):
    data=open(metadata_file,'r').read().strip().split('\n')
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
    

def main():
    args=parse_args()
    metadata_dict=make_metadata_dict(args.metadata)
    raw_data=open(args.raw_data,'r').read().strip().split('\n')
    header=raw_data[0].split('\t')
    energy_indices=[]
    for entry in header:
        if entry.endswith('Energy'):
            energy_indices.append(header.index(entry))
    outf=open(args.outf,'w')
    outf.write(header[0]) 
    for header_index in range(1,len(header)):
        if header_index not in energy_indices:
            outf.write('\t'+header[header_index])
        else:
            outf.write('\t'+header[header_index]+'\t'+header[header_index]+'.roza_shizgal_bmr'+'\t'+header[header_index]+'.harris_benedict_bmr')
    outf.write('\n') 
    for line in raw_data[1::]:
        tokens=line.split('\t')
        subject=tokens[1]        
        outstring=tokens[0]+'\t'+tokens[1]
        for token_index in range(2,len(tokens)):
            if token_index in energy_indices:
                if tokens[token_index]=="NA":
                    outstring=outstring+'\t'+tokens[token_index] +'\t'+tokens[token_index]+'\t'+tokens[token_index]
                else:
                    #perform correction
                    corrected_roza_shizgal=roza_shizgal(float(tokens[token_index]),metadata_dict[subject.split('_')[0]])
                    corrected_harris_benedict=harris_benedict(float(tokens[token_index]),metadata_dict[subject.split('_')[0]])
                    outstring=outstring+'\t'+str(tokens[token_index])+'\t'+str(corrected_roza_shizgal)+'\t'+str(corrected_harris_benedict)
            else:
                #add to output directly
                outstring=outstring+'\t'+tokens[token_index] 
        outf.write(outstring+'\n')
        

if __name__=="__main__":
    main() 
