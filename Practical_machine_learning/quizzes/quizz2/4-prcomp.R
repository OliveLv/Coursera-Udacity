library(caret)
library(AppliedPredictiveModeling)
set.seed(3433)
data(AlzheimerDisease)
adData = data.frame(diagnosis,predictors)
inTrain = createDataPartition(adData$diagnosis, p = 3/4)[[1]]
training = adData[ inTrain,]
testing = adData[-inTrain,]
IL<-grep("IL",colnames(training))
n<-length(IL)
for(i in 1:(n-1)){
  if(i==1)newdata<-data.frame(training[[IL[i]]])
  else
    newdata<-cbind(newdata,training[[IL[i]]])
}
colnames(newdata)<-colnames(training)[IL[1:(n-1)]]
#prComp<-prcomp(newdata)
#summary(prComp)

preProc<-preProcess(newdata,method="pca",thresh=0.8)
preProc$numComp