rm(list=ls())
source('helpers.R')
library(data.table)
library(gplots)

hr_data=data.frame(read.table('hr.heatmap',header=TRUE,sep='\t'))
dev=hr_data$Device
en_data=data.frame(read.table('energy.heatmap',header=TRUE,sep='\t'))
en=en_data$Device

hr_data$Device=NULL
en_data$Device=NULL 
hr_data=100*hr_data
en_data=100*en_data
my_palette <- colorRampPalette(c("blue", "#FFFFFF", "#FF9900"))(n = 29)
colors = c(seq(0,5,length=10),seq(6,10,length=10),seq(11,14,length=10))
hr_mat=data.matrix(hr_data,rownames.force=NA)
rownames(hr_mat)=dev 
en_mat=data.matrix(en_data,rownames.force=NA)
rownames(en_mat)=en

p1<-heatmap.2(hr_mat,
          dendrogram="none",
          Colv=NA,
          Rowv=NA,
          col=my_palette,
          breaks=colors,
          trace="none",
          density.info="none",
          margin=c(10,15),
          cexRow=2,
          cexCol=2,
          key.title="Error Relative to Gold Standard",
          key.xlab="abs(GS-Device)/GS",
          main="Heart Rate BPM Device Error by Activity",
          key.par=list(cex.main=5)
          )
colors = c(seq(0,15,length=10),seq(16,20,length=10),seq(21,109.1,length=10))
p2<-heatmap.2(en_mat,
          dendrogram="none",
          Colv=NA,
          Rowv=NA,
          col=my_palette,
          trace="none",
          density.info="none",
          breaks=colors,
          margin=c(10,15),
          cexRow=2,
          cexCol=2,
          key.title="Error Relative to Gold Standard",
          key.xlab="abs(GS-Device)/GS",
          main="Energy KCal Device Error by Activity"
)
