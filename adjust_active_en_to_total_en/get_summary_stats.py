import argparse
import pdb
def parse_args():
    parser=argparse.ArgumentParser("Calculate error summary statistics for devices")
    parser.add_argument("--inputf")
    parser.add_argument("--outf")
    return parser.parse_args()

def main():
    args=parse_args()
    data=open(args.inputf,'r').read().strip().split('\n')
    header=data[0].split('\t')
    device_index=header.index('Device')
    activity_index=header.index('Activity')
    correction_index=header.index('Correction')
    kcal_index=header.index("ErrorKcal")
    percent_index=header.index("ErrorPercent")
    
    percent_error_dict=dict()
    kcal_error_dict=dict()
    percent_error_dict['all']=[]
    kcal_error_dict['all']=[]
    devices=set([])
    activities=set([]) 
    for line in data[1::]:
        tokens=line.split('\t')
        cur_device=tokens[device_index]
        cur_activity=tokens[activity_index]
        cur_correction=tokens[correction_index]
        kcal_value=float(tokens[kcal_index])
        percent_value=float(tokens[percent_index])
        #print(str(cur_device))
        #print(str(percent_value))
        #print(str(cur_activity))
        devices.add(cur_device)
        activities.add(cur_activity)
        if cur_device not in percent_error_dict:
            percent_error_dict[cur_device]=dict()
        if cur_activity not in percent_error_dict[cur_device]:
            percent_error_dict[cur_device][cur_activity]=dict()
        if cur_correction not in percent_error_dict[cur_device][cur_activity]: 
            percent_error_dict[cur_device][cur_activity][cur_correction]=[percent_value]
        else:
            percent_error_dict[cur_device][cur_activity][cur_correction].append(percent_value)
        if cur_device not in kcal_error_dict:
            kcal_error_dict[cur_device]=dict()
        if cur_activity not in kcal_error_dict[cur_device]:
            kcal_error_dict[cur_device][cur_activity]=dict()
        if cur_correction not in kcal_error_dict[cur_device][cur_activity]: 
            kcal_error_dict[cur_device][cur_activity][cur_correction]=[kcal_value]
        else:
            kcal_error_dict[cur_device][cur_activity][cur_correction].append(kcal_value)
        #percent_error_dict['all'].append(percent_value)
        #kcal_error_dict['all'].append(kcal_value)
    outf=open(args.outf+'.percent','w')
    activities=list(activities)
    devices=list(devices)
    pdb.set_trace() 
    import numpy as np 
    outf.write('Uncorrected:\n')
    outf.write('\t'+'\t'.join(activities)+'\n')
    for device in devices:
        outf.write(device)
        for activity in activities:
            cur_median=round(np.median(np.abs(percent_error_dict[device][activity]['uncorrected'])),3)
            outf.write('\t'+str(cur_median))
        outf.write('\n')

    outf.write('Roza-Shizgal:\n')
    for device in devices:
        outf.write(device)
        for activity in activities:
            cur_median=round(np.median(np.abs(percent_error_dict[device][activity]['roza_shizgal'])),3)
            outf.write('\t'+str(cur_median))
        outf.write('\n')

    outf.write('Harris-Benedict:\n') 
    for device in devices:
        outf.write(device)
        for activity in activities:
            cur_median=round(np.median(np.abs(percent_error_dict[device][activity]['harris_benedict'])),3)
            outf.write('\t'+str(cur_median))
        outf.write('\n')
    outf=open(args.outf+'.kcal','w')
    outf.write('Uncorrected:\n')
    outf.write('\t'+'\t'.join(activities)+'\n')
    for device in devices:
        outf.write(device)
        for activity in activities:
            cur_median=round(np.median(np.abs(kcal_error_dict[device][activity]['uncorrected'])),3)
            outf.write('\t'+str(cur_median))
        outf.write('\n')

    outf.write('Roza-Shizgal:\n')
    for device in devices:
        outf.write(device)
        for activity in activities:
            cur_median=round(np.median(np.abs(kcal_error_dict[device][activity]['roza_shizgal'])),3)
            outf.write('\t'+str(cur_median))
        outf.write('\n')

    outf.write('Harris-Benedict:\n') 
    for device in devices:
        outf.write(device)
        for activity in activities:
            cur_median=round(np.median(np.abs(kcal_error_dict[device][activity]['harris_benedict'])),3)
            outf.write('\t'+str(cur_median))
        outf.write('\n')

    
if __name__=="__main__":
    main() 
