rm(list=ls())
source('helpers.R')
library(data.table)
library(gplots)
hr_data=data.frame(read.table('hr.heatmap.bySubject',header=TRUE,sep=','))
dev=hr_data$Subject
en_data=data.frame(read.table('en.heatmap.bySubject',header=TRUE,sep=','))
en=en_data$Subject

hr_data$Subject=NULL
en_data$Subject=NULL 

my_palette <- colorRampPalette(c("#006400", "#F7B52D", "red","gray"))(n=39)
colors = c(seq(0,0.05,length=10),seq(0.051,0.1,length=10),seq(0.11,3,length=10),seq(3.01,4.01,length=10))
hr_mat=data.matrix(hr_data,rownames.force=NA)
rownames(hr_mat)=dev 
en_mat=data.matrix(en_data,rownames.force=NA)
rownames(en_mat)=en

p1<-heatmap.2(hr_mat,
              Rowv=NA,
              Colv=TRUE,
              colsep=FALSE,
              rowsep=FALSE,
              dendrogram="none",
              trace="none",
              density.info="none",
              col=my_palette,
              breaks=colors,
              margin=c(10,5),
              xlab="Activity_Device",
              ylab="Subject",
              key.title="Error Relative to Gold Standard",
              key.xlab="abs(GS-Device)/GS",
              main="Heart Rate BPM Device Error by Activity"
)
colors = c(seq(0,0.10,length=10),seq(0.11,0.20,length=10),seq(0.21,3,length=10),seq(3.01,4.01,length=10))
p2<-heatmap.2(en_mat,
              Rowv=NA,
              Colv=TRUE,
              colsep=FALSE,
              rowsep=FALSE,
              dendrogram="none",
              trace="none",
              density.info="none",
              col=my_palette,
              breaks=colors,
              margin=c(10,5),
              key.title="Error Relative to Gold Standard",
              key.xlab="abs(GS-Device)/GS",
              main="Energy KCal Device Error by Activity",
              xlab="Activity_Device",
              ylab="Subject"
)
