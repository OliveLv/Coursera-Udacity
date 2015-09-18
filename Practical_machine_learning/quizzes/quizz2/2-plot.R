library(AppliedPredictiveModeling)
data(concrete)
library(caret)
library(Hmisc)
set.seed(975)
inTrain = createDataPartition(mixtures$CompressiveStrength, p = 3/4)[[1]]
training = mixtures[ inTrain,]
testing = mixtures[-inTrain,]
c<-colnames(training)

n<-length(c)
print(n)
par(mfrow=c(3,3))
for(i in 1:(n)){
print(i)
  plot(training$CompressiveStrength,col=cut2(training[[i]]),xlab=c[i],ylab="y") 
}