#formats data matrix into a dataframe for GEE
data=open('AshleyLab_device_validation_study_data_matrix_ALL.csv','r').read().strip().split('\n')
outf=open('full_df.tsv','w')
outf.write('Subject\tSex\tAge\tHeight\tWeight\tBMI\tSkin\tFitzpatrick\tWrist\tVO2max\tMetric\tActivity\tIntensity\tDevice\tError\n')
header=data[0].split('\t') 
for line in data[1::]:
    tokens=line.split('\t')
    subject=tokens[0]
    sex=tokens[1]
    age=tokens[2]
    height=tokens[3]
    weight=tokens[4]
    bmi=tokens[5]
    skin=tokens[6]
    fitzpatrick=tokens[7]
    wrist=tokens[8]
    vo2max=tokens[9]
    for i in range(10,len(tokens)):
        value=tokens[i]
        label=header[i].split('_') 
        metric=label[0]
        activity=label[1]
        device=label[2]
        if activity=="sit":
            intensity="0"
        elif activity=="walk1":
            activity="walk"
            intensity="1"
        elif activity=="walk2":
            activity="walk"
            intensity="2"
        elif activity=="run1":
            activity="run"
            intensity="3"
        elif activity=="run2":
            activity="run"
            intensity="4"
        elif activity=="bike1":
            activity="bike"
            intensity="3"
        elif activity=="bike2":
            activity="bike"
            intensity="4"
        elif activity=="max":
            intensity="5"
        outf.write('\t'.join([subject,sex,age,height,weight,bmi,skin,fitzpatrick,wrist,vo2max,metric,activity,intensity,device,value])+'\n')
        
            
