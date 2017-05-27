# get adjusted percent error in energy expenditure (both kcal/min & percent relative to gold standard)
import argparse
import pdb 
def parse_args():
    parser=argparse.ArgumentParser("Get adjusted percent error in energy expenditure both kcal/min & percent relative to gs")
    parser.add_argument("--inputf")
    parser.add_argument("--outf")
    return parser.parse_args() 

def main():
    args=parse_args()
    data=open(args.inputf,'r').read().strip().split('\n')
    outf=open(args.outf,'w')
    header=data[0].split('\t')
    #get header indices for gold standard, uncorrected energy, corrected energy 
    gs_index=header.index("GoldStandard_Energy")
    uncorrected=[]
    harris_benedict_corrected=[]
    roza_shizgal_corrected=[]
    for entry in header:
        if entry.endswith('Energy'):
            if entry.startswith("Gold"):
                continue
            else:
                uncorrected.append(header.index(entry))
        elif entry.endswith("harris_benedict_bmr"):
            harris_benedict_corrected.append(header.index(entry))
        elif entry.endswith("roza_shizgal_bmr"):
            roza_shizgal_corrected.append(header.index(entry))
    subject_dict=dict()
    for line_index in range(1,len(data)):
        line=data[line_index]
        tokens=line.split('\t')
        activity=tokens[2]
        if activity.startswith('sit'):
            activity='sit'
        elif activity.startswith('walk'):
            activity='walk'
        elif activity.startswith("run"):
            activity='run'
        elif activity.startswith("bike"):
            activity="bike"
        elif activity.startswith("max"):
            activity="max"
        else:
            continue 
        subject=tokens[1]
        if subject not in subject_dict:
            subject_dict[subject]=dict()
        if activity not in subject_dict[subject]:
            subject_dict[subject][activity]=dict()
        if "uncorrected" not in subject_dict[subject][activity]:
            subject_dict[subject][activity]["uncorrected"]=dict()
            subject_dict[subject][activity]["harris_benedict"]=dict()
            subject_dict[subject][activity]["roza_shizgal"]=dict()
        try:
            gs=float(tokens[gs_index])
        except:
            continue
        if gs==0:
            continue 
        for uncorrected_index in uncorrected:
            try:
                uncorrected_val=float(tokens[uncorrected_index])
            except:
                continue #the value is not a valid float (probably NA) 
            uncorrected_delta=uncorrected_val - gs
            uncorrected_percent_delta=uncorrected_delta/gs
            subject_dict[subject][activity]["uncorrected"][header[uncorrected_index]]=[uncorrected_val,uncorrected_delta,uncorrected_percent_delta]
        for index in harris_benedict_corrected: 
            try:
                corrected_val=float(tokens[index])
            except:
                continue #the value is not a valid float (probably NA) 
            corrected_delta=corrected_val - gs
            corrected_percent_delta=corrected_delta/gs
            subject_dict[subject][activity]["harris_benedict"][header[index]]=[corrected_val,corrected_delta,corrected_percent_delta]
        for index in roza_shizgal_corrected: 
            try:
                corrected_val=float(tokens[index])
            except:
                continue #the value is not a valid float (probably NA) 
            corrected_delta=corrected_val - gs
            corrected_percent_delta=corrected_delta/gs
            subject_dict[subject][activity]["roza_shizgal"][header[index]]=[corrected_val,corrected_delta,corrected_percent_delta]
    #write the output file
    outf.write("subject\tactivity\tcorrection\tdevice\terror\n")
    for subject in subject_dict:
        for activity in subject_dict[subject]:
            for correction in subject_dict[subject][activity]:
                for device in subject_dict[subject][activity][correction]:
                    output=subject+'\t'\
                            +activity+'\t'\
                            +correction+'\t'\
                            +device.split('_')[0]+'\t'\
                            +'\t'.join([str(i) for i in subject_dict[subject][activity][correction][device]])+'\n'
                    outf.write(output)
                    
    
    
if __name__=="__main__":
    main()
    
