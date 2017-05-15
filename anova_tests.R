rm(list=ls())
source('helpers.R')
library(data.table)
library(ggplot2)
library(plyr)
hr=data.frame(read.table("heartrate.txt",header=T,sep='\t'))
hr$State=factor(hr$State,levels=c("sit","walk","run","bike","max"))
en=data.frame(read.table("energy.txt",header=T,sep='\t'))
en$State=factor(en$State,levels=c("sit","walk","run","bike","max"))
#percent difference from gold standard 
hr$percentdiff=hr$Error/hr$GoldStandard
en$percentdiff=en$Error/en$GoldStandard 
en$percentdiff[en$percentdiff %in% -Inf]=-1 
en$percentdiff[en$percentdiff %in% Inf]=1


#HEART RATE 
apple=hr[hr$Device %in% "Apple_HR",]
basis=hr[hr$Device %in% "Basis_HR",]
microsoft=hr[hr$Device %in% "Microsoft_HR",]
fitbit=hr[hr$Device %in% "Fitbit_HR",]
samsung=hr[hr$Device %in% "Samsung_HR",]
mio=hr[hr$Device %in% "Mio_HR",]
pulseon=hr[hr$Device %in% "Pulseon_HR",]

#ANOVA SEX 
aov1=aov(percentdiff~Sex,data=apple)
tk1=TukeyHSD(aov1,conf.level=0.95)

aov2=aov(percentdiff~Sex,data=basis)
tk2=TukeyHSD(aov2,conf.level=0.95)

aov3=aov(percentdiff~Sex,data=microsoft)
tk3=TukeyHSD(aov3,conf.level=0.95)

aov4=aov(percentdiff~Sex,data=fitbit)
tk4=TukeyHSD(aov4,conf.level=0.95)

aov5=aov(percentdiff~Sex,data=samsung)
tk5=TukeyHSD(aov5,conf.level=0.95)

aov6=aov(percentdiff~Sex,data=mio)
tk6=TukeyHSD(aov6,conf.level=0.95)

aov7=aov(percentdiff~Sex,data=pulseon)
tk7=TukeyHSD(aov7,conf.level=0.95)

#ANOVA ARM 
aov1=aov(percentdiff~Arm,data=apple)
tk1=TukeyHSD(aov1,conf.level=0.95)

aov2=aov(percentdiff~Arm,data=basis)
tk2=TukeyHSD(aov2,conf.level=0.95)

aov3=aov(percentdiff~Arm,data=microsoft)
tk3=TukeyHSD(aov3,conf.level=0.95)

aov4=aov(percentdiff~Arm,data=fitbit)
tk4=TukeyHSD(aov4,conf.level=0.95)

aov5=aov(percentdiff~Arm,data=samsung)
tk5=TukeyHSD(aov5,conf.level=0.95)

aov6=aov(percentdiff~Arm,data=mio)
tk6=TukeyHSD(aov6,conf.level=0.95)

aov7=aov(percentdiff~Arm,data=pulseon)
tk7=TukeyHSD(aov7,conf.level=0.95)


#ANOVA POSITION 
aov1=aov(percentdiff~Pos,data=apple)
tk1=TukeyHSD(aov1,conf.level=0.95)

aov2=aov(percentdiff~Pos,data=basis)
tk2=TukeyHSD(aov2,conf.level=0.95)

aov3=aov(percentdiff~Pos,data=microsoft)
tk3=TukeyHSD(aov3,conf.level=0.95)

aov4=aov(percentdiff~Pos,data=fitbit)
tk4=TukeyHSD(aov4,conf.level=0.95)

aov5=aov(percentdiff~Pos,data=samsung)
tk5=TukeyHSD(aov5,conf.level=0.95)

aov6=aov(percentdiff~Pos,data=mio)
tk6=TukeyHSD(aov6,conf.level=0.95)

aov7=aov(percentdiff~Pos,data=pulseon)
tk7=TukeyHSD(aov7,conf.level=0.95)

#ENERGY
apple=en[en$Device %in% "Apple_Energy",]
basis=en[en$Device %in% "Basis_Energy",]
microsoft=en[en$Device %in% "Microsoft_Energy",]
fitbit=en[en$Device %in% "Fitbit_Energy",]
pulseon=en[en$Device %in% "PulseOn_Energy",]

#ANOVA SEX 
aov1=aov(percentdiff~Sex,data=apple)
tk1=TukeyHSD(aov1,conf.level=0.95)

aov2=aov(percentdiff~Sex,data=basis)
tk2=TukeyHSD(aov2,conf.level=0.95)

aov3=aov(percentdiff~Sex,data=microsoft)
tk3=TukeyHSD(aov3,conf.level=0.95)

aov4=aov(percentdiff~Sex,data=fitbit)
tk4=TukeyHSD(aov4,conf.level=0.95)

aov5=aov(percentdiff~Sex,data=pulseon)
tk5=TukeyHSD(aov5,conf.level=0.95)
p1<-ggplot(basis,aes(Sex,percentdiff))+
  geom_boxplot()+
  xlab('Biological Sex')+
  ylab('Gold Standard Kcal - Basis Kcal/\nGold Standard Kcal')+
  ylim(-1,1)+
  ggtitle("Basis Energy Percent Error for Males vs Females")+
  theme_bw(20)


browser() 
#ANOVA ARM 
aov1=aov(percentdiff~Arm,data=apple)
tk1=TukeyHSD(aov1,conf.level=0.95)

aov2=aov(percentdiff~Arm,data=basis)
tk2=TukeyHSD(aov2,conf.level=0.95)

aov3=aov(percentdiff~Arm,data=microsoft)
tk3=TukeyHSD(aov3,conf.level=0.95)

aov4=aov(percentdiff~Arm,data=fitbit)
tk4=TukeyHSD(aov4,conf.level=0.95)

aov5=aov(percentdiff~Arm,data=pulseon)
tk5=TukeyHSD(aov5,conf.level=0.95)


#ANOVA POSITION 
aov1=aov(percentdiff~Pos,data=apple)
tk1=TukeyHSD(aov1,conf.level=0.95)

aov2=aov(percentdiff~Pos,data=basis)
tk2=TukeyHSD(aov2,conf.level=0.95)

aov3=aov(percentdiff~Pos,data=microsoft)
tk3=TukeyHSD(aov3,conf.level=0.95)

aov4=aov(percentdiff~Pos,data=fitbit)
tk4=TukeyHSD(aov4,conf.level=0.95)

aov5=aov(percentdiff~Pos,data=pulseon)
tk5=TukeyHSD(aov5,conf.level=0.95)

