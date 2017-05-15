rm(list=ls())
library('gee')
library('data.table')
library('MuMIn')

data=data.frame(read.table('full_df.tsv',header=TRUE,sep='\t'))

#remove any rows with "NA" -- no device value recorded 
data=na.omit(data)
data$Error=abs(data$Error)
data$Activity=factor(data$Activity,levels=c("sit","walk","run","bike","max"))
hr=data[which(data$Metric=="hr"),]
en=data[which(data$Metric=="en"),]
en$Device=factor(en$Device,levels=c("Apple","Basis","Fitbit","Microsoft","PulseOn"))

#GLM model 
#hr_glm=glm(Error~Sex+Age+Height+Weight+BMI+Skin+Fitzpatrick+Wrist+VO2max+Activity+Intensity+Device,data=hr)
#en_glm=glm(Error~Sex+Age+Height+Weight+BMI+Skin+Fitzpatrick+Wrist+VO2max+Activity+Intensity+Device,data=en)

#Fit Generalized estimation equation (GEE) with independent correlation structure 
#hr_gee_ind=gee(Error~Sex+Age+Height+Weight+BMI+Skin+Fitzpatrick+Wrist+VO2max+Activity+Intensity+Device,data=hr,id=Subject,corstr="independence")
#en_gee_ind=gee(Error~Sex+Age+Height+Weight+BMI+Skin+Fitzpatrick+Wrist+VO2max+Activity+Intensity+Device,data=en,id=Subject,corstr="independence")

#Fit Generalized estimation equation (GEE) with exchangeable correlation structure 
hr_gee_exch=gee(Error~
                  Sex+
                  Age+
                  Sex:Age+
                  Height+
                  Weight+
                  BMI+
                  Skin+
                  Fitzpatrick+
                  Wrist+
                  VO2max+
                  Activity+
                  Intensity+
                  Device+
                  Activity:Device+
                  Intensity:Device
                ,data=hr,id=Subject,corstr="exchangeable")
en_gee_exch=gee(Error~
                  Sex+
                  Age+
                  Sex:Age+
                  Height+
                  Weight+
                  BMI+
                  Skin+
                  Fitzpatrick+
                  Wrist+
                  VO2max+
                  Activity+
                  Intensity+
                  Device+
                  Activity:Device+
                  Intensity:Device
                  ,data=en,id=Subject,corstr="exchangeable")

en_gee_exch_pval=2 * pnorm(abs(coef(summary(en_gee_exch))[,5]), lower.tail = FALSE)
en_results=data.frame(summary(en_gee_exch)$coefficients,en_gee_exch_pval)
hr_results=hr_results[order(hr_gee_exch_pval),]
en_results=en_results[order(en_gee_exch_pval),]

dd=pdredge(hr_gee_exch)
# Model average models with delta AICc < 4
model.avg(dd, subset = delta < 4)
#or as a 95% confidence set:
model.avg(dd, subset = cumsum(weight) <= .95) # get averaged coefficients
#'Best' model
hr_best=summary(get.models(dd, 1)[[1]])
hr_gee_exch_pval=2 * pnorm(abs(coef(hr_best)[,5]), lower.tail = FALSE)
hr_results=data.frame(hr_best$coefficients,hr_gee_exch_pval)
par(mar = c(3,5,6,4))
plot(dd, labAsExpr = TRUE)


dd=pdredge(en_gee_exch)
# Model average models with delta AICc < 4
model.avg(dd, subset = delta < 4)
#or as a 95% confidence set:
model.avg(dd, subset = cumsum(weight) <= .95) # get averaged coefficients
#'Best' model
en_best=summary(get.models(dd, 1)[[1]])
en_gee_exch_pval=2 * pnorm(abs(coef(en_best)[,5]), lower.tail = FALSE)
en_results=data.frame(en_best$coefficients,en_gee_exch_pval)
par(mar = c(3,5,6,4))
plot(dd, labAsExpr = TRUE)
