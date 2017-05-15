data=open('full_df.tsv','r').read().strip().split('\n')
hr_dict=dict()
en_dict=dict()
header=data[0].split('\t')
for line in data[1::]:
    tokens=line.split('\t')
    subject=tokens[0]
    metric=tokens[10]
    activity=tokens[11]
    intensity=tokens[12]
    device=tokens[13]
    if tokens[14]=="NA":
        continue 
    error=float(tokens[14])
    if metric=="hr":
        if abs(error)<0.10:
            continue 
        if device not in hr_dict:
            hr_dict[device]=dict()
        if activity not in hr_dict[device]:
            hr_dict[device][activity]=dict()
        if intensity not in hr_dict[device][activity]:
            hr_dict[device][activity][intensity]=dict()
        hr_dict[device][activity][intensity][subject]=error
    if metric=="en":
        if abs(error)<0.30:
            continue 
        if device not in en_dict:
            en_dict[device]=dict()
        if activity not in en_dict[device]:
            en_dict[device][activity]=dict()
        if intensity not in en_dict[device][activity]:
            en_dict[device][activity][intensity]=dict()
        en_dict[device][activity][intensity][subject]=error

outf_hr=open('hr_chart.tsv','w')
outf_en=open('en_chart.tsv','w')
subjects=[str(i) for i in range(1,61)]
outf_hr.write('Device\tActivity\tIntensity\t'+'\t'.join(subjects)+'\n')
for device in hr_dict:
    for activity in hr_dict[device]:
        for intensity in hr_dict[device][activity]:
            outf_hr.write(device+'\t'+activity+'\t'+intensity)
            for subject in subjects:
                if subject in hr_dict[device][activity][intensity]:
                    outf_hr.write('\t'+str(round(hr_dict[device][activity][intensity][subject],3)))
                else:
                    outf_hr.write('\t')
            outf_hr.write('\n')

outf_en.write('Device\tActivity\tIntensity\t'+'\t'.join(subjects)+'\n')
for device in en_dict:
    for activity in en_dict[device]:
        for intensity in en_dict[device][activity]:
            outf_en.write(device+'\t'+activity+'\t'+intensity)
            for subject in subjects:
                if subject in en_dict[device][activity][intensity]:
                    outf_en.write('\t'+str(round(en_dict[device][activity][intensity][subject],3)))
                else:
                    outf_en.write('\t')
            outf_en.write('\n')

