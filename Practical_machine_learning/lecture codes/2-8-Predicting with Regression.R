# Example: Old faithful eruptions
library(caret)
library(lattice)
library(ggplot2)
data(faithful)
set.seed(333)
inTrain<-createDataPartition(y=faithful$waiting,p=0.5,list=F)
trainFaith<-faithful[inTrain,]
testFaith<-faithful[-inTrain,]
head(trainFaith)

# Eruption duration versus waiting time
plot(trainFaith$waiting,trainFaith$eruptions,pch=19,col="blue",xlab="Waiting",ylab="Duration")

# Fit a linear model
lm1<-lm(eruptions~waiting,data=trainFaith)
summary(lm1)

# Model fit
plot(trainFaith$waiting,trainFaith$eruptions,pch=19,col="blue",xlab="Waiting",ylab="Duration")
 # lwd control the thickness of the line
lines(trainFaith$waiting,lm1$fitted,lwd=3)

# Predict a new value
coef(lm1)[1]+coef(lm1)[2]*80
newdata<-data.frame(waiting=80)
predict(lm1,newdata)

# Plot predictions - training and test
par(mfrow=c(1,2))
plot(trainFaith$waiting,trainFaith$eruptions,pch=19,col="blue",xlab="Waiting",ylab="Duration")
lines(trainFaith$waiting,predict(lm1),lwd=3)
plot(testFaith$waiting,testFaith$eruptions,pch=19,col="blue",xlab="Waiting",ylab="Duration")
lines(testFaith$waiting,predict(lm1,newdata=testFaith),lwd=3)

# Get training set / test set errors
sqrt(sum((lm1$fitted-trainFaith$eruptions)^2))
sqrt(sum((predict(lm1,newdata=testFaith)-testFaith$eruptions)^2))

# Prediction intervals
pred1<-predict(lm1,newdata=testFaith,interval="prediction")
summary(pred1)
ord<-order(testFaith$waiting)
plot(testFaith$waiting,testFaith$eruptions,pch=19,col="blue",xlab="Waiting",ylab="Duration")
  # lty means line types(1~5),lwd means line widths
matlines(testFaith$waiting[ord],pred1[ord,],type="l",,col=c(1,2,3),lty=c(1,1,1),lwd=3)

# Same process with caret
modelFit<-train(eruptions~waiting,data=trainFaith,method="glm")
summary(modelFit$finalModel)