#rm(ls=dir())
rm(list=ls())
library(ggplot2)
library(data.table)
library(zoo)
source('helpers.R')
data=data.frame(read.table("errors.txt",header=TRUE,sep='\t'))
data=na.aggregate(data)
id_vals=data$ID
data$ID=NULL
pr=prcomp(data)
#scores=prcomp(data)$x[,1:3]
#scores=data.frame(scores)
#names(scores)=c("PC1","PC2","PC3")
#pc1.2 <- qplot(x=PC1, y=PC2, data=scores) +
#  theme(legend.position="none")
#pc1.3 <- qplot(x=PC1, y=PC3, data=scores, colour=factor(sample.groups)) +
#  theme(legend.position="none")
#pc2.3 <- qplot(x=PC2, y=PC3, data=scores, colour=factor(sample.groups)) +
#  theme(legend.position="none")
#library(devtools)
#install_github("ggbiplot", "vqv")

#library(ggbiplot)
source('ggbiplot.R')
g1 <- ggbiplot(pr, 
              choices=c(1,2),
              obs.scale = 1, 
              var.scale = 1,
              labels=factor(id_vals),
              circle=TRUE,
              labels.size=5,
              varname.size=5,
              varname.adjust=2,
              varname.abbrev = FALSE)+
  theme_bw(20)

g2 <- ggbiplot(pr, 
              choices=c(1,3),
              obs.scale = 1, 
              var.scale = 1,
              labels=factor(id_vals),
              circle=TRUE,
              labels.size=5,
              varname.size=5,
              varname.adjust=2,
              varname.abbrev = FALSE)+
  theme_bw(20)

g3 <- ggbiplot(pr, 
              choices=c(2,3),
              obs.scale = 1, 
              var.scale = 1,
              labels=factor(id_vals),
              circle=TRUE,
              labels.size=5,
              varname.size=5,
              varname.adjust=2,
              varname.abbrev = FALSE)+
  theme_bw(20)

#multiplot(g1,g2,g3,cols=3)