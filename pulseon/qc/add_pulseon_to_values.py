#add the fbData & wellness table values to the existing pulseon values that have been collected.
data=open("/home/anna/device_validation/adjust_active_en_to_total_en/adjusted_data/Batch2.adjusted.EE.csv",'r').read().strip().split('\n')
pulseon_all=open("/home/anna/device_validation/pulseon/qc/pulseon.extracted.values.txt",'r').read().strip().split('\n')
outf=open('/home/anna/device_validation/pulseon/qc/Batch2.with.pulseon.wellness.fbData.txt','w')
time_to_pulseon=dict()
for line in pulseon_all[1::]:
    tokens=line.split('\t')
    time=tokens[0]
    time_to_pulseon[time]=line
outf.write(data[0]+'\t'+pulseon_all[0]+'\n')
for line in data[1::]:
    tokens=line.split('\t')
    timestamp=tokens[0][0:12]
    if timestamp in time_to_pulseon:
        #append!
        outf.write(line+'\t'+time_to_pulseon[timestamp]+'\n')
    else:
        outf.write(line+'\n')
        

