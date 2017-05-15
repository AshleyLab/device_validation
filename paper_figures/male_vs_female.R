rm(list=ls())
library(dplyr)
library(tidyr)
library(ggplot2)
data=read.csv("/home/anna/device_validation/AshleyLab_device_validation_study_data_matrix_ALL.csv",sep="\t")
data=data[,1:66]
data[,11:66]=abs(data[,11:66])
gathered=gather(data,label,measurement,-ID,-Sex,-Age,-Height,-Weight,-BMI,-Skin,-Fitzpatrick,-Wrist,-V02max)
gathered$measurement=100*gathered$measurement 
p1<-ggplot(gathered,aes(Sex,measurement))+
  geom_boxplot(width=0.4,fill = "#93CCEA", colour = "black" )+
  theme_bw(20)+
  xlab("")+
  ylab("Percent Error:\n100*(gold standard bpm - device bpm)/\n(gold standard bpm)")+
  ggtitle("Heart Rate Aggregate Error")
  guides(fill=FALSE)
