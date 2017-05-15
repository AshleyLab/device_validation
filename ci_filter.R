rm(list=ls())
library(data.table)
data=data.frame(read.table("/home/anna/device_validation/AshleyLab_device_validation_study_data_matrix_ALL.csv",header=T,sep='\t'))

#hr for bicycle task 
bikevars=c("hr_bike1_Microsoft","hr_bike1_PulseOn","hr_bike1_Mio","hr_bike1_Samsung","hr_bike2_Apple","hr_bike2_Basis","hr_bike2_Fitbit","hr_bike2_Microsoft","hr_bike2_PulseOn","hr_bike2_Mio","hr_bike2_Samsung")
hr_bike=na.omit(abs(unlist(data[bikevars])))
median_error_hr_bike=median(hr_bike)
qt_val_bike=qt(0.95,df=length(hr_bike)-1)*sd(hr_bike)/sqrt(length(hr_bike))

#bike error medians by device 
microsoft_hr_bike_error_median=median(na.omit(abs(unlist(data[c("hr_bike1_Microsoft","hr_bike2_Microsoft")]))))
pulseon_hr_bike_error_median=median(na.omit(abs(unlist(data[c("hr_bike1_PulseOn","hr_bike2_PulseOn")]))))
fitbit_hr_bike_error_median=median(na.omit(abs(unlist(data[c("hr_bike1_Fitbit","hr_bike2_Fitbit")]))))
samsung_hr_bike_error_median=median(na.omit(abs(unlist(data[c("hr_bike1_Samsung","hr_bike2_Samsung")]))))
mio_hr_bike_error_median=median(na.omit(abs(unlist(data[c("hr_bike1_Mio","hr_bike2_Mio")]))))
apple_hr_bike_error_median=median(na.omit(abs(unlist(data[c("hr_bike1_Apple","hr_bike2_Apple")]))))
basis_hr_bike_error_median=median(na.omit(abs(unlist(data[c("hr_bike1_Basis","hr_bike2_Basis")]))))

#hr for walking task 
walkvars=c("hr_walk1_Microsoft","hr_walk1_PulseOn","hr_walk1_Mio","hr_walk1_Samsung","hr_walk2_Apple","hr_walk2_Basis","hr_walk2_Fitbit","hr_walk2_Microsoft","hr_walk2_PulseOn","hr_walk2_Mio","hr_walk2_Samsung")
hr_walk=na.omit(abs(unlist(data[walkvars])))
median_error_hr_walk=median(hr_walk)
qt_val_walk=qt(0.95,df=length(hr_walk)-1)*sd(hr_walk)/sqrt(length(hr_walk))

#walk error medians by device 
microsoft_hr_walk_error_median=na.omit(abs(unlist(data[c("hr_walk1_Microsoft","hr_walk2_Microsoft")])))
qt_val_walk=qt(0.95,df=length(microsoft_hr_walk_error_median)-1)*sd(microsoft_hr_walk_error_median)/sqrt(length(microsoft_hr_walk_error_median))
pulseon_hr_walk_error_median=na.omit(abs(unlist(data[c("hr_walk1_PulseOn","hr_walk2_PulseOn")])))
qt_val_walk=qt(0.95,df=length(pulseon_hr_walk_error_median)-1)*sd(pulseon_hr_walk_error_median)/sqrt(length(pulseon_hr_walk_error_median))

fitbit_hr_walk_error_median=median(na.omit(abs(unlist(data[c("hr_walk1_Fitbit","hr_walk2_Fitbit")]))))
samsung_hr_walk_error_median=median(na.omit(abs(unlist(data[c("hr_walk1_Samsung","hr_walk2_Samsung")]))))
mio_hr_walk_error_median=median(na.omit(abs(unlist(data[c("hr_walk1_Mio","hr_walk2_Mio")]))))
apple_hr_walk_error_median=na.omit(abs(unlist(data[c("hr_walk1_Apple","hr_walk2_Apple")])))
qt_val_walk=qt(0.95,df=length(apple_hr_walk_error_median)-1)*sd(apple_hr_walk_error_median)/sqrt(length(apple_hr_walk_error_median))
basis_hr_walk_error_median=median(na.omit(abs(unlist(data[c("hr_walk1_Basis","hr_walk2_Basis")]))))

########ALL TASKS#####
fitbit=abs(as.numeric(unlist(na.omit(read.table("fig1/Fitbit_en.ALL.TASKS.csv",header=FALSE,sep='\t')))))
qt_val=qt(0.95,df=length(fitbit)-1)*sd(fitbit)/sqrt(length(fitbit))

apple=abs(as.numeric(unlist(na.omit(read.table("fig1/Apple_en.ALL.TASKS.csv",header=FALSE,sep='\t')))))
qt_val=qt(0.95,df=length(apple)-1)*sd(apple)/sqrt(length(apple))

basis=abs(as.numeric(unlist(na.omit(read.table("fig1/Basis_en.ALL.TASKS.csv",header=FALSE,sep='\t')))))
qt_val=qt(0.95,df=length(basis)-1)*sd(basis)/sqrt(length(basis))

microsoft=abs(as.numeric(unlist(na.omit(read.table("fig1/Microsoft_en.ALL.TASKS.csv",header=FALSE,sep='\t')))))
qt_val=qt(0.95,df=length(microsoft)-1)*sd(microsoft)/sqrt(length(microsoft))

pulseon=abs(as.numeric(unlist(na.omit(read.table("fig1/PulseOn_en.ALL.TASKS.csv",header=FALSE,sep='\t')))))
qt_val=qt(0.95,df=length(pulseon)-1)*sd(pulseon)/sqrt(length(pulseon))


##ENERGY 
walkvars=c("en_walk1_Microsoft","en_walk1_PulseOn","en_walk2_Apple","en_walk2_Basis","en_walk2_Fitbit","en_walk2_Microsoft","en_walk2_PulseOn")
en_walk=na.omit(abs(unlist(data[walkvars])))
median_error_en_walk=median(en_walk)
qt_val_walk=qt(0.95,df=length(en_walk)-1)*sd(en_walk)/sqrt(length(en_walk))

runvars=c("en_run1_Microsoft","en_run1_PulseOn","en_run2_Apple","en_run2_Basis","en_run2_Fitbit","en_run2_Microsoft","en_run2_PulseOn")
en_run=na.omit(abs(unlist(data[runvars])))
median_error_en_run=median(en_run)
qt_val_run=qt(0.95,df=length(en_run)-1)*sd(en_run)/sqrt(length(en_run))


sitvars=c("en_sit_Microsoft","en_sit_PulseOn","en_sit_Apple","en_sit_Basis","en_sit_Fitbit");
en_sit=na.omit(abs(unlist(data[sitvars])))
median_error_en_sit=median(en_sit)
qt_val_sit=qt(0.95,df=length(en_sit)-1)*sd(en_sit)/sqrt(length(en_sit))

