rm(list=ls())
source('helpers.R')
library(ggplot2)
library(data.table)
library(reshape2)

# hr_walk=data.frame(read.table('walk.hr.formatted.csv',header=T,sep='\t'))
# hr_bike=data.frame(read.table('bike.hr.formatted.csv',header=T,sep='\t'))
# en_walk=data.frame(read.table('walk.en.formatted.csv',header=T,sep='\t'))
# en_bike=data.frame(read.table('bike.en.formatted.csv',header=T,sep='\t'))
data=data.frame(read.table("/home/anna/device_validation/AshleyLab_device_validation_study_data_matrix_ALL.csv",header=T,sep='\t'))

microsoft_hr_walk_error=100*abs(unlist(data[c("hr_walk1_Microsoft","hr_walk2_Microsoft")]))
pulseon_hr_walk_error=100*abs(unlist(data[c("hr_walk1_PulseOn","hr_walk2_PulseOn")]))
fitbit_hr_walk_error=100*abs(unlist(data[c("hr_walk1_Fitbit","hr_walk2_Fitbit")]))
samsung_hr_walk_error=100*abs(unlist(data[c("hr_walk1_Samsung","hr_walk2_Samsung")]))
mio_hr_walk_error=100*abs(unlist(data[c("hr_walk1_Mio","hr_walk2_Mio")]))
apple_hr_walk_error=100*abs(unlist(data[c("hr_walk1_Apple","hr_walk2_Apple")]))
basis_hr_walk_error=100*abs(unlist(data[c("hr_walk1_Basis","hr_walk2_Basis")]))
hr_walk=data.frame(cbind(microsoft_hr_walk_error,pulseon_hr_walk_error,fitbit_hr_walk_error,samsung_hr_walk_error,mio_hr_walk_error,apple_hr_walk_error,basis_hr_walk_error))
names(hr_walk)=c("Microsoft","PulseOn","Fitbit","Samsung","Mio","Apple","Basis")
row.names(hr_walk)=NULL
d=melt(hr_walk)
p1=ggplot(d,aes(factor(d$variable,levels=c("Apple","Basis","Fitbit","Microsoft","PulseOn","Mio","Samsung")),d$value))+
  geom_boxplot(fill="#ffffcc",notch=FALSE,lwd=2)+
  coord_flip()+
  geom_hline(yintercept=5,colour="#006400",linetype="longdash",size=2)+
  geom_hline(yintercept=10,colour="#F7B52D",linetype="longdash",size=2)+
  ylim(0,100)+
  theme_bw(70)+
  xlab("")+
  ylab("")+
  scale_x_discrete(labels=c("Apple Watch", "Basis Peak", "Fitbit Surge", "Microsoft Band","PulseOn", "MIO Alpha 2", "Samsung Gear S2"))


microsoft_hr_bike_error=100*abs(unlist(data[c("hr_bike1_Microsoft","hr_bike2_Microsoft")]))
pulseon_hr_bike_error=100*abs(unlist(data[c("hr_bike1_PulseOn","hr_bike2_PulseOn")]))
fitbit_hr_bike_error=100*abs(unlist(data[c("hr_bike1_Fitbit","hr_bike2_Fitbit")]))
samsung_hr_bike_error=100*abs(unlist(data[c("hr_bike1_Samsung","hr_bike2_Samsung")]))
mio_hr_bike_error=100*abs(unlist(data[c("hr_bike1_Mio","hr_bike2_Mio")]))
apple_hr_bike_error=100*abs(unlist(data[c("hr_bike1_Apple","hr_bike2_Apple")]))
basis_hr_bike_error=100*abs(unlist(data[c("hr_bike1_Basis","hr_bike2_Basis")]))

hr_bike=data.frame(cbind(microsoft_hr_bike_error,pulseon_hr_bike_error,fitbit_hr_bike_error,samsung_hr_bike_error,mio_hr_bike_error,apple_hr_bike_error,basis_hr_bike_error))
names(hr_bike)=c("Microsoft","PulseOn","Fitbit","Samsung","Mio","Apple","Basis")
row.names(hr_bike)=NULL
d2=melt(hr_bike)
p2=ggplot(d2,aes(factor(d2$variable,levels=c("Apple","Basis","Fitbit","Microsoft","PulseOn","Mio","Samsung")),d2$value))+
  geom_boxplot(fill="#ffffcc",lwd=2)+
  coord_flip()+
  scale_y_reverse( lim=c(100,0))+
  geom_hline(yintercept=5,colour="#006400",linetype="longdash",size=2)+
  geom_hline(yintercept=10,colour="#F7B52D",linetype="longdash",size=2)+
  geom_hline(yintercept=0,colour="#000000",size=2)+
  theme_bw(70)+
  xlab("")+
  ylab("")+
  scale_x_discrete(labels=c("Apple Watch", "Basis Peak", "Fitbit Surge", "Microsoft Band","PulseOn", "MIO Alpha 2", "Samsung Gear S2"))

  


microsoft_en_walk_error=100*abs(unlist(data[c("en_walk1_Microsoft","en_walk2_Microsoft")]))
pulseon_en_walk_error=100*abs(unlist(data[c("en_walk1_PulseOn","en_walk2_PulseOn")]))
fitbit_en_walk_error=100*abs(unlist(data[c("en_walk1_Fitbit","en_walk2_Fitbit")]))
apple_en_walk_error=100*abs(unlist(data[c("en_walk1_Apple","en_walk2_Apple")]))
basis_en_walk_error=100*abs(unlist(data[c("en_walk1_Basis","en_walk2_Basis")]))
en_walk=data.frame(cbind(microsoft_en_walk_error,pulseon_en_walk_error,fitbit_en_walk_error,apple_en_walk_error,basis_en_walk_error))
names(en_walk)=c("Microsoft","PulseOn","Fitbit","Apple","Basis")
row.names(en_walk)=NULL
d3=melt(en_walk)
p3=ggplot(d3,aes(factor(d3$variable,levels=c("Apple","Basis","Fitbit","Microsoft","PulseOn")),d3$value))+
  geom_boxplot(fill="#ffffcc",notch=FALSE,lwd=2)+
  coord_flip()+
  geom_hline(yintercept=5,colour="#006400",linetype="longdash",size=2)+
  geom_hline(yintercept=10,colour="#F7B52D",linetype="longdash",size=2)+
  ylim(0,100)+
  theme_bw(70)+
  xlab("")+
  ylab("")+
  scale_x_discrete(labels=c("Apple Watch", "Basis Peak", "Fitbit Surge", "Microsoft Band","PulseOn"))

  


microsoft_en_bike_error=100*abs(unlist(data[c("en_bike1_Microsoft","en_bike2_Microsoft")]))
pulseon_en_bike_error=100*abs(unlist(data[c("en_bike1_PulseOn","en_bike2_PulseOn")]))
fitbit_en_bike_error=100*abs(unlist(data[c("en_bike1_Fitbit","en_bike2_Fitbit")]))
apple_en_bike_error=100*abs(unlist(data[c("en_bike1_Apple","en_bike2_Apple")]))
basis_en_bike_error=100*abs(unlist(data[c("en_bike1_Basis","en_bike2_Basis")]))

en_bike=data.frame(cbind(microsoft_en_bike_error,pulseon_en_bike_error,fitbit_en_bike_error,apple_en_bike_error,basis_en_bike_error))
names(en_bike)=c("Microsoft","PulseOn","Fitbit","Apple","Basis")
row.names(en_bike)=NULL
d4=melt(en_bike)
p4=ggplot(d4,aes(factor(d4$variable,levels=c("Apple","Basis","Fitbit","Microsoft","PulseOn")),d4$value))+
  geom_boxplot(fill="#ffffcc",lwd=2)+
  coord_flip()+
  scale_y_reverse( lim=c(100,0))+
  geom_hline(yintercept=5,colour="#006400",linetype="longdash",size=2)+
  geom_hline(yintercept=10,colour="#F7B52D",linetype="longdash",size=2)+
  geom_hline(yintercept=0,colour="#000000",size=2)+
  theme_bw(70)+
  xlab("")+
  ylab("")+
  scale_x_discrete(labels=c("Apple Watch", "Basis Peak", "Fitbit Surge", "Microsoft Band","PulseOn"))



  
multiplot(p2,p4,p1,p3,cols=2)