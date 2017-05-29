import argparse
import pdb
def parse_args():
    parser=argparse.ArgumentParser("Calculate error summary statistics for devices")
    parser.add_argument("--inputf")
    parser.add_argument("--outf")
    return parser.parse_args()


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
    percent_error_collapsed_dict=dict()
    kcal_error_collapsed_dict=dict()
    
    devices=set([])
    activities=set([])
    collapsed_activities=set([])
    for line in data[1::]:
        tokens=line.split('\t')
        cur_device=tokens[device_index]
        cur_activity=tokens[activity_index]
        cur_activity_collapsed=convert_state(cur_activity) 
        cur_correction=tokens[correction_index]
        kcal_value=float(tokens[kcal_index])
        percent_value=float(tokens[percent_index])
        devices.add(cur_device)
        activities.add(cur_activity)
        collapsed_activities.add(cur_activity_collapsed) 
        
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

        #generate collapsed summary by activities
        if cur_device not in percent_error_collapsed_dict:
            percent_error_collapsed_dict[cur_device]=dict()
        if cur_activity_collapsed not in percent_error_collapsed_dict[cur_device]:
            percent_error_collapsed_dict[cur_device][cur_activity_collapsed]=dict()
        if cur_correction not in percent_error_collapsed_dict[cur_device][cur_activity_collapsed]: 
            percent_error_collapsed_dict[cur_device][cur_activity_collapsed][cur_correction]=[percent_value]
        else:
            percent_error_collapsed_dict[cur_device][cur_activity_collapsed][cur_correction].append(percent_value)
        if cur_device not in kcal_error_collapsed_dict:
            kcal_error_collapsed_dict[cur_device]=dict()
        if cur_activity_collapsed not in kcal_error_collapsed_dict[cur_device]:
            kcal_error_collapsed_dict[cur_device][cur_activity_collapsed]=dict()
        if cur_correction not in kcal_error_collapsed_dict[cur_device][cur_activity_collapsed]: 
            kcal_error_collapsed_dict[cur_device][cur_activity_collapsed][cur_correction]=[kcal_value]
        else:
            kcal_error_collapsed_dict[cur_device][cur_activity_collapsed][cur_correction].append(kcal_value)

        
            
    outf=open(args.outf+'.percent','w')
    activities=list(activities)
    devices=list(devices)
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

    #collapased activities
    outf=open(args.outf+'.percent.collapsed','w')
    activities=list(collapsed_activities)
    devices=list(devices)
    import numpy as np 
    outf.write('Uncorrected:\n')
    outf.write('\t'+'\t'.join(activities)+'\n')
    for device in devices:
        outf.write(device)
        for activity in activities:
            cur_median=round(np.median(np.abs(percent_error_collapsed_dict[device][activity]['uncorrected'])),3)
            outf.write('\t'+str(cur_median))
        outf.write('\n')

    outf.write('Roza-Shizgal:\n')
    for device in devices:
        outf.write(device)
        for activity in activities:
            cur_median=round(np.median(np.abs(percent_error_collapsed_dict[device][activity]['roza_shizgal'])),3)
            outf.write('\t'+str(cur_median))
        outf.write('\n')

    outf.write('Harris-Benedict:\n') 
    for device in devices:
        outf.write(device)
        for activity in activities:
            cur_median=round(np.median(np.abs(percent_error_collapsed_dict[device][activity]['harris_benedict'])),3)
            outf.write('\t'+str(cur_median))
        outf.write('\n')
        
    outf=open(args.outf+'.kcal.collapased','w')
    outf.write('Uncorrected:\n')
    outf.write('\t'+'\t'.join(activities)+'\n')
    for device in devices:
        outf.write(device)
        for activity in activities:
            cur_median=round(np.median(np.abs(kcal_error_collapsed_dict[device][activity]['uncorrected'])),3)
            outf.write('\t'+str(cur_median))
        outf.write('\n')

    outf.write('Roza-Shizgal:\n')
    for device in devices:
        outf.write(device)
        for activity in activities:
            cur_median=round(np.median(np.abs(kcal_error_collapsed_dict[device][activity]['roza_shizgal'])),3)
            outf.write('\t'+str(cur_median))
        outf.write('\n')

    outf.write('Harris-Benedict:\n') 
    for device in devices:
        outf.write(device)
        for activity in activities:
            cur_median=round(np.median(np.abs(kcal_error_collapsed_dict[device][activity]['harris_benedict'])),3)
            outf.write('\t'+str(cur_median))
        outf.write('\n')

    
if __name__=="__main__":
    main() 
