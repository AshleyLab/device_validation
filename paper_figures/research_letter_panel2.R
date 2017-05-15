#generate a single heatmap w/ energy expenditure & HR data in
rm(list=ls())
source('helpers.R')
library(data.table)
library(gplots)
data=data.frame(read.table("combined.heatmap",header=TRUE,sep='\t'))
dev=data$Device 
data$Device=NULL
data=100*data
my_palette <- colorRampPalette(c("#0072B2", "#009E73", "#F0E442","#E69F00","#D55E00"))(n = 59)
colors = c(seq(0,5,length=10),seq(6,10,length=10),seq(11,20,length=10),seq(21,50,length=20),seq(51,100,length=10))
mat=data.matrix(data,rownames.force=NA)
rownames(mat)=dev 
row_annotation <- c("blue","blue","blue","blue","blue","blue","blue","#FF9900","#FF9900","#FF9900","#FF9900","#FF9900")
row_annotation <- as.matrix(row_annotation)    
colnames(row_annotation) <- c("Hr vs Energy")

p1<-heatmap.2(mat,
          dendrogram="none",
          Colv=NA,
          Rowv=NA,
          col=my_palette,
          breaks=colors,
          keysize = 0.5,
          trace="none",
          density.info="none",
          margin=c(15,30),
          cexRow=4,
          cexCol=4,
          key.title="Error Relative to Gold Standard",
          key.xlab="abs(GS-Device)/GS",
          key.par=list(cex.main=5),
          RowSideColors = row_annotation
          )
