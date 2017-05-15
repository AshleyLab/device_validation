rm(list=ls())
source('helpers.R')
library(ggplot2)
data=read.table("AshleyLab_device_validation_study_data_matrix_ALL.csv",header=TRUE,sep='\t')
p1<-ggplot(data,aes(x=data$Sex))+
  geom_bar()+
  theme_bw(20)+
  xlab("Sex")+
  ylab("Number of Subjects")

p2<-ggplot(data,aes(x=data$Age))+
  geom_histogram()+
  theme_bw(20)+
  xlab("Age")+
  ylab("Number of Subjects")

p3<-ggplot(data,aes(x=data$Height),fill=data$Height)+
  geom_density(fill="blue",alpha=0.5)+
  theme_bw(20)+
  xlab("Height")


p4<-ggplot(data,aes(x=data$Weight))+
geom_density(fill="blue",alpha=0.5)+
  theme_bw(20)+
  xlab("Weight")+
  ylab("density")


p5<-ggplot(data,aes(x=data$Skin))+
geom_density(fill="blue",alpha=0.5)+
  theme_bw(20)+
  xlab("Wrist Skin Tone")+
  ylab("density")


p6<-ggplot(data,aes(x=data$V02max))+
geom_density(fill="blue",alpha=0.5)+
  theme_bw(20)+
  xlab("VO2 max")+
  ylab("density")

multiplot(p1,p2,p3,p4,p5,p6,cols=3)