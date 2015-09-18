# Why preprocess?
library(caret)
library(kernlab)
data(spam)
inTrain<-createDataPartition(y=spam$type,p=0.75,list=F)
training<-spam[inTrain,]
testing<-spam[-inTrain,]
hist(training$capitalAve,main="",xlab="ave. capital run length")
mean(training$capitalAve)
sd(training$capitalAve)

# Standardizing
trainCapAve<-training$capitalAve
trainCapAveS<-(trainCapAve-mean(trainCapAve))/sd(trainCapAve)
mean(trainCapAveS)
sd(trainCapAveS)

# Standardizing - test set
testCapAve<-testing$capitalAve
testCapAveS<-(testCapAve-mean(trainCapAve))/sd(trainCapAve)
mean(testCapAveS)
sd(testCapAveS)

# Standardizing - preProcess function
# Pre-processing transformation (centering, scaling etc.) 
  can be estimated from the training data 
  and applied to any data set with the same variables.
# training[,58] correspond to training$type,char type
pre0bj<-preProcess(training[,-58],method=c("center","scale"))
trainCapAveS<-predict(pre0bj,training[,-58])$capitalAve
mean(trainCapAveS)
sd(trainCapAveS)

# Standardizing - preProcess function
testCapAveS<-predict(pre0bj,testing[,-58])$capitalAve
mean(testCapAveS)
sd(testCapAveS)

# Standardizing - preProcess argument
set.seed(32343)
modelFit<-train(type~.,data=training,preProcess=c("center","scale"),method="glm")
modelFit