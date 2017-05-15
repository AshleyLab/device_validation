import sys
stats=['statistic','p.value','estimate']
inputs=sys.argv[2::]
outputf=sys.argv[1]
hr_dict=dict()
en_dict=dict()
covariates=[] 
for f in inputs:
    f_tokens=f.split('_')
    covariate=f_tokens[0]
    covariates.append(covariate) 
    metric=f_tokens[1]
    data=open(f,'r').read().replace('\"','').replace(',','\t').split('\n')
    while '' in data:
        data.remove('')
    for line in data[1::]:
        tokens=line.split('\t')
        watch=tokens[1]
        stat=tokens[3]
        if stat in stats:
            val=round(float(tokens[2]),3) 
            if metric=="hr": 
                if watch not in hr_dict:
                    hr_dict[watch]=dict()
                if covariate not in hr_dict[watch]:
                    hr_dict[watch][covariate]=dict()
                hr_dict[watch][covariate][stat]=val
            else:
                if watch not in en_dict:
                    en_dict[watch]=dict()
                if covariate not in en_dict[watch]:
                    en_dict[watch][covariate]=dict()
                en_dict[watch][covariate][stat]=val
#print str(en_dict) 
#record output files !!
outf_hr=open(outputf+'_hr.SUMMARY.tsv','w')
outf_en=open(outputf+'_en.SUMMARY.tsv','w')
outf_hr.write('Watch')
outf_en.write('Watch')
for covariate in covariates:
    outf_hr.write('\t'+covariate+'\t\t')
    outf_en.write('\t'+covariate+'\t\t')
outf_hr.write('\n')
outf_en.write('\n')
outf_hr.write('statistic')
outf_en.write('statistic') 
for covariate in covariates:
    for stat in stats:
        outf_hr.write('\t'+stat)
        outf_en.write('\t'+stat) 
outf_hr.write('\n')
outf_en.write('\n')
for watch in hr_dict:
    outf_hr.write(watch)
    for covariate in covariates: 
        for stat in stats:
            outf_hr.write('\t'+str(hr_dict[watch][covariate][stat]))
    outf_hr.write('\n')

for watch in en_dict:
    outf_en.write(watch)
    for covariate in covariates: 
        for stat in stats:
            outf_en.write('\t'+str(en_dict[watch][covariate][stat]))
    outf_en.write('\n')

