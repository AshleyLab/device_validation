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

#Skin Tone -Fitzpatrick scale ##################################################################################
cortestresults=ddply(hr, .(Device), summarise,
      corr=(cor.test(percentdiff, Fitzpatrick,
                     alternative="two.sided", method="pearson")), name=names(corr) )
write.csv(cortestresults,file="fitzpatrick_hr_correlation.tsv")
cortestresults=ddply(en, .(Device), summarise,
                     corr=(cor.test(percentdiff, Fitzpatrick,
                                    alternative="two.sided", method="pearson")), name=names(corr) )
write.csv(cortestresults,file="fitzpatrick_en_correlation.tsv")

#Skin Tone -Von Luschan scale ##################################################################################
cortestresults=ddply(hr, .(Device), summarise,
                     corr=(cor.test(percentdiff, Skin,
                                    alternative="two.sided", method="pearson")), name=names(corr) )
write.csv(cortestresults,file="vonluschan_hr_correlation.tsv")
cortestresults=ddply(en, .(Device), summarise,
                     corr=(cor.test(percentdiff, Skin,
                                    alternative="two.sided", method="pearson")), name=names(corr) )
write.csv(cortestresults,file="vonluschan_en_correlation.tsv")

#BMI##################################################################################
cortestresults=ddply(hr, .(Device), summarise,
                     corr=(cor.test(percentdiff, BMI,
                                    alternative="two.sided", method="pearson")), name=names(corr) )
write.csv(cortestresults,file="BMI_hr_correlation.tsv")
cortestresults=ddply(en, .(Device), summarise,
                     corr=(cor.test(percentdiff, BMI,
                                    alternative="two.sided", method="pearson")), name=names(corr) )
write.csv(cortestresults,file="BMI_en_correlation.tsv")
#Age ##################################################################################
cortestresults=ddply(hr, .(Device), summarise,
                     corr=(cor.test(percentdiff, Age,
                                    alternative="two.sided", method="pearson")), name=names(corr) )
write.csv(cortestresults,file="age_hr_correlation.tsv")
cortestresults=ddply(en, .(Device), summarise,
                     corr=(cor.test(percentdiff, Age,
                                    alternative="two.sided", method="pearson")), name=names(corr) )
write.csv(cortestresults,file="age_en_correlation.tsv")

#Wrist ##################################################################################
cortestresults=ddply(hr, .(Device), summarise,
                     corr=(cor.test(percentdiff, Wrist,
                                    alternative="two.sided", method="pearson")), name=names(corr) )
write.csv(cortestresults,file="wrist_hr_correlation.tsv")
cortestresults=ddply(en, .(Device), summarise,
                     corr=(cor.test(percentdiff, Wrist,
                                    alternative="two.sided", method="pearson")), name=names(corr) )
write.csv(cortestresults,file="wrist_en_correlation.tsv")

#V02 ##################################################################################
cortestresults=ddply(hr, .(Device), summarise,
                     corr=(cor.test(percentdiff, V02max,
                                    alternative="two.sided", method="pearson")), name=names(corr) )
write.csv(cortestresults,file="v02max_hr_correlation.tsv")
cortestresults=ddply(en, .(Device), summarise,
                     corr=(cor.test(percentdiff, V02max,
                                    alternative="two.sided", method="pearson")), name=names(corr) )
write.csv(cortestresults,file="v02max_en_correlation.tsv")
