rm(list=ls())
source("~/device_validation/helpers.R")
data=read.table("All.adjusted.EE.error.csv",header=TRUE,sep='\t')
library(ggplot2)
#subset data by activities & correction factor 
unc_sit_data=data[data$Activity=="sit" & data$Correction=="uncorrected",]
rs_sit_data=data[data$Activity=="sit" & data$Correction=="roza_shizgal",]
hb_sit_data=data[data$Activity=="sit" & data$Correction=="harris_benedict",]

unc_walk_data=data[data$Activity=="walk" & data$Correction=="uncorrected",]
rs_walk_data=data[data$Activity=="walk" & data$Correction=="roza_shizgal",]
hb_walk_data=data[data$Activity=="walk" & data$Correction=="harris_benedict",]

unc_run_data=data[data$Activity=="run" & data$Correction=="uncorrected",]
rs_run_data=data[data$Activity=="run" & data$Correction=="roza_shizgal",]
hb_run_data=data[data$Activity=="run" & data$Correction=="harris_benedict",]

unc_bike_data=data[data$Activity=="bike" & data$Correction=="uncorrected",]
rs_bike_data=data[data$Activity=="bike" & data$Correction=="roza_shizgal",]
hb_bike_data=data[data$Activity=="bike" & data$Correction=="harris_benedict",]

unc_max_data=data[data$Activity=="max" & data$Correction=="uncorrected",]
rs_max_data=data[data$Activity=="max" & data$Correction=="roza_shizgal",]
hb_max_data=data[data$Activity=="max" & data$Correction=="harris_benedict",]


p1=ggplot(unc_sit_data,aes(Device,ErrorPercent))+
  geom_boxplot()+
  ylim(c(-1,1))+
  ggtitle("Sit, Uncorrected")+
  ylab("(Kcal device - Gold_standard)/\nGold_Standard")

p2=ggplot(unc_walk_data,aes(Device,ErrorPercent))+
  geom_boxplot()+
  ylim(c(-1,1))+
  ggtitle("Walk, Uncorrected")+
  ylab("(Kcal device - Gold_standard)/\nGold_Standard")

p3=ggplot(unc_run_data,aes(Device,ErrorPercent))+
  geom_boxplot()+
  ylim(c(-1,1))+
  ggtitle("Run, Uncorrected")+
  ylab("(Kcal device - Gold_standard)/\nGold_Standard")

p4=ggplot(unc_bike_data,aes(Device,ErrorPercent))+
  geom_boxplot()+
  ylim(c(-1,1))+
  ggtitle("Bike, Uncorrected")+
  ylab("(Kcal device - Gold_standard)/\nGold_Standard")

p5=ggplot(unc_max_data,aes(Device,ErrorPercent))+
  geom_boxplot()+
  ylim(c(-1,1))+
  ggtitle("Max, Uncorrected")+
  ylab("(Kcal device - Gold_standard)/\nGold_Standard")


p6=ggplot(rs_sit_data,aes(Device,ErrorPercent))+
  geom_boxplot()+
  ylim(c(-1,1))+
  ggtitle("Sit, Roza-Shizgal Correction")+
  ylab("(Kcal device - Gold_standard)/\nGold_Standard")

p7=ggplot(rs_walk_data,aes(Device,ErrorPercent))+
  geom_boxplot()+
  ylim(c(-1,1))+
  ggtitle("Walk, Roza-Shizgal Correction")+
  ylab("(Kcal device - Gold_standard)/\nGold_Standard")

p8=ggplot(rs_run_data,aes(Device,ErrorPercent))+
  geom_boxplot()+
  ylim(c(-1,1))+
  ggtitle("Run, Roza-Shizgal Correction")+
  ylab("(Kcal device - Gold_standard)/\nGold_Standard")

p9=ggplot(rs_bike_data,aes(Device,ErrorPercent))+
  geom_boxplot()+
  ylim(c(-1,1))+
  ggtitle("Bike, Roza-Shizgal Correction")+
  ylab("(Kcal device - Gold_standard)/\nGold_Standard")

p10=ggplot(rs_max_data,aes(Device,ErrorPercent))+
  geom_boxplot()+
  ylim(c(-1,1))+
  ggtitle("Max, Roza-Shizgal Correction")+
  ylab("(Kcal device - Gold_standard)/\nGold_Standard")


p11=ggplot(hb_sit_data,aes(Device,ErrorPercent))+
  geom_boxplot()+
  ylim(c(-1,1))+
  ggtitle("Sit, Harris-Benedict Correction")+
  ylab("(Kcal device - Gold_standard)/\nGold_Standard")

p12=ggplot(hb_walk_data,aes(Device,ErrorPercent))+
  geom_boxplot()+
  ylim(c(-1,1))+
  ggtitle("Walk, Harris-Benedict Correction")+
  ylab("(Kcal device - Gold_standard)/\nGold_Standard")

p13=ggplot(hb_run_data,aes(Device,ErrorPercent))+
  geom_boxplot()+
  ylim(c(-1,1))+
  ggtitle("Run, Harris-Benedict Correction")+
  ylab("(Kcal device - Gold_standard)/\nGold_Standard")

p14=ggplot(hb_bike_data,aes(Device,ErrorPercent))+
  geom_boxplot()+
  ylim(c(-1,1))+
  ggtitle("Bike, Harris-Benedict Correction")+
  ylab("(Kcal device - Gold_standard)/\nGold_Standard")

p15=ggplot(hb_max_data,aes(Device,ErrorPercent))+
  geom_boxplot()+
  ylim(c(-1,1))+
  ggtitle("Max, Harris-Benedict Correction")+
  ylab("(Kcal device - Gold_standard)/\nGold_Standard")

multiplot(p1,p6,p11,
          p2,p7,p12,
          p3,p8,p13,
          p4,p9,p14,
          p5,p10,p15,cols=5)
