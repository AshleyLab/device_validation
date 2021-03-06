rm(list=ls())
source('helpers.R')
library(data.table)
library(ggplot2)
library(plyr)
library(BlandAltmanLeh)
hr=data.frame(read.table("heartrate.txt",header=T,sep='\t'))
hr$State=factor(hr$State,levels=c("sit","walk","run","bike","max"))
en=data.frame(read.table("energy.txt",header=T,sep='\t'))
en$State=factor(en$State,levels=c("sit","walk","run","bike","max"))

#percent difference from gold standard 
hr$percentdiff=hr$Error/hr$GoldStandard
en$percentdiff=en$Error/en$GoldStandard 
en$percentdiff[en$percentdiff %in% -Inf]=-1 
en$percentdiff[en$percentdiff %in% Inf]=1

#device mean analysis across activity states 
mean_hr=hr[which(hr$Device %in% "device_mean"),]
mean_en=en[which(en$Device %in% "device_mean"),]
mean_hr$DeviceMeasured=mean_hr$GoldStandard-mean_hr$Error
mean_en$DeviceMeasured=mean_en$GoldStandard-mean_en$Error

ba.stats <- bland.altman.stats(mean_hr$DeviceMeasured, mean_hr$GoldStandard)
plot(ba.stats$means, ba.stats$diffs, col=mean_hr$State, 
     sub=paste("critical difference is", round(ba.stats$critical.diff,4)),
     main="Heart Rate BPM (Averaged Across Devices) vs Gold Standard",ylim=c(-100,100),pch=16,xlab="Means", ylab="Diffs")
abline(h = ba.stats$lines, lty=c(2,3,2), col=c("lightblue","blue","lightblue"), 
       lwd=c(3,2,3))
legend(x = "topright", legend = c("sit","walk","run","bike","max"), fill = 1:5)
browser() 
ba.stats <- bland.altman.stats(mean_en$DeviceMeasured, mean_en$GoldStandard)
plot(ba.stats$means, ba.stats$diffs, col=mean_en$State, 
     sub=paste("critical difference is", round(ba.stats$critical.diff,4)),
     main="Energy in Kcal (Averaged Across Devices) vs Gold Standard",pch=16,xlab="Means", ylab="Diffs")
abline(h = ba.stats$lines, lty=c(2,3,2), col=c("lightblue","blue","lightblue"), 
       lwd=c(3,2,3))
legend(x = "topright", legend = c("sit","walk","run","bike","max"), fill = 1:5)
browser() 
p1<-ggplot(mean_hr,aes(State,Error))+
  geom_boxplot()+
  xlab('Activity State')+
  ylab('Gold Standard BPM - \nMean Device BPM')+
  ylim(-50,50)+
  ggtitle("Heart Rate Error (BPM)")+
  theme_bw(20)

p2<-ggplot(mean_hr,aes(State,percentdiff))+
  geom_boxplot()+
  xlab('Activity State')+
  ylab('(Gold Standard BPM - Mean Device BPM)/\nGold Standard BPM')+
  ylim(-.5,.5)+
  ggtitle("Heart Rate Error as Fraction of Gold Standard")+
  theme_bw(20)


p3<-ggplot(mean_en,aes(State,Error))+
  geom_boxplot()+
  xlab('Activity State')+
  ylab('Gold Standard Kcal -\n Mean Device Kcal')+
  ylim(-10,10)+
  ggtitle("Energy Error (Kcal)")+
  theme_bw(20)

p4<-ggplot(mean_en,aes(State,percentdiff))+
  geom_boxplot()+
  xlab('Activity State')+
  ylab('(Gold Standard Kcal - Mean Device Kcal)/\nGold Standard Kcal')+
  ylim(-.5,.5)+
  ggtitle("Energy Error as Fraction of Gold Standard")+
  theme_bw(20)
multiplot(p1,p2,p3,p4,cols=2)



#TABLE SUMMARY
hr_percent_diff_summary=ddply(mean_hr,~State,summarise,mean=mean(percentdiff),sd=sd(percentdiff))
hr_bpm_diff_summary=ddply(mean_hr,~State,summarise,mean=mean(Error),sd=sd(Error))
energy_percent_diff_summary=ddply(mean_en,~State,summarise,mean=mean(percentdiff),sd=sd(percentdiff))
energy_kcal_diff_summary=ddply(mean_en,~State,summarise, mean=mean(Error),sd=sd(Error))
write.csv(hr_percent_diff_summary,file="hr_percent_diff.tsv",sep='\t')
write.csv(hr_bpm_diff_summary,file="hr_bpm_diff.tsv",sep='\t')
write.csv(energy_percent_diff_summary,file="energy_percent_diff.tsv",sep='\t')
write.csv(energy_kcal_diff_summary,file="energy_kcal_diff.tsv",sep='\t')
