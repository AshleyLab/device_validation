rm(list=ls())
source('colormap.r')
library('ellipse')
ashdevices=read.csv("/home/anna/device_validation/AshleyLab_device_validation_study_data_matrix_ALL.csv",sep="\t")
ashdemog=ashdevices[,1:10]
type_measure=c("hr","en")
type_exercise=c("sit","walk1","walk2","run1","run2","bike1","bike2","max")
type_device=sort(c("Fitbit","Microsoft","PulseOn","Mio","Samsung","Apple","Basis"))
legend_vals=sort(c("Fitbit Surge","Microsoft Band","PulseOn","MIO Alpha 2","Samsung Gear S2","Apple Watch","Basis Peak"))
demogs=c("Sex", "Age", "Height", "Weight", "BMI", "Skin", "Fitzpatrick", "Wrist", "V02max")
datal=as.list(type_device);names(datal)=type_device
for(dev in type_device){
  subl=paste("hr",type_exercise,dev,sep="_")
  datal[[dev]]=data.matrix(ashdevices[,subl])
}
exmat=do.call("rbind",datal)
N=nrow(datal[[1]])
exdemog=ashdemog[rep(seq(N),7),]
exdemog$device=factor(rep(type_device,rep(N,7)))
colnames(exmat)=type_exercise
exframe=data.frame(exdemog,exercise=I(exmat[,-8]))
exframe=na.omit(exframe)
exsvd=svd(exframe$exercise)
pcsd=exsvd$d;names(pcsd)=paste("PC",1:7,sep="")
lds=exsvd$v;dimnames(lds)=list(colnames(exframe$exercise),paste("PC",1:7,sep=""))
lds[,1]=lds[,1]*-1
pcs=scale(exsvd$u,FALSE,1/exsvd$d);colnames(pcs)=paste("PC",1:7,sep="");pcs[,1]=pcs[,1]*-1
par(mfrow=c(1,1),cex.axis=2,cex.lab=2,cex.main=2,cex.sub=2)
plot(pcs[,1:2],col=mit.colors[as.numeric(exframe$device)],pch=19,cex=2,xlim=c(-1,1.5),ylim=c(-1,1.5))
legend("topright",col=mit.colors[1:7],pch=19,legend=legend_vals,cex=2)

for(i in seq(type_device)){
  tdev=type_device[i]
  cmat=cov(pcs[exframe$device==tdev,c(1,2)])
  cent=apply(pcs[exframe$device==tdev,c(1,2)],2,mean)
  ell=ellipse(cmat,centre=cent,lwd=6)
  lines(ell,col=mit.colors[i],lwd=6)
}