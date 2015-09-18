# Spam Example
library(caret)
library(kernlab)
data(spam)
inTrain<-createDataPartition(y=spam$type,p=0.75,list=F)
training<-spam[inTrain,]
testing<-spam[-inTrain,]
modelFit<-train(type~.,data=training,method="glm")

# show default configure of function train
args(train.default)
args(trainControl)