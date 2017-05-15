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

my_palette <- colorRampPalette(c("#006400", "#F7B52D", "red"))(n = 29)
colors = c(seq(0,0.05,length=10),seq(0.051,0.1,length=10),seq(0.11,0.181,length=10))
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
          main="Heart Rate BPM Device Error by Activity"
          )
colors = c(seq(0,0.10,length=10),seq(0.11,0.20,length=10),seq(0.21,1.062,length=10))
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
