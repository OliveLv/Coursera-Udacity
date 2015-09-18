# Spam Example: Data splitting
library(caret)
library(kernlab)
data(spam)
inTrain<-createDataPartition(y=spam$type,p=0.75,list=F)
training<-spam[inTrain,]
testing<-spam[-inTrain,]
dim(training)

# Spam Example: K-fold
set.seed(32323)
folds<-createFolds(y=spam$type,k=10,list=T,returnTrain=T)
# get length of each fold
sapply(folds,length)
# get part of elements of Fold01
folds[[1]][1:10]
folds[["Fold01"]][1:10]
folds$Fold01[1:10]

# Spam Example: Return test
set.seed(32323)
folds<-createFolds(y=spam$type,k=10,list=T,returnTrain=F)
sapply(folds,length)
folds[[1]][1:10]

# Spam Example: Resampling
set.seed(32323)
folds<-createResample(y=spam$type,times=10,list=T)
sapply(folds,length)
folds[[1]][1:10]

# Spam Example: Time Slices
set.seed(32323)
tme<-1:1000
# initialWindow--train set
# horizon--test set  means to predict next 10 data
folds<-createTimeSlices(y=tme,initialWindow=20,horizon=10)
names(folds)
folds$train[[1]]
folds$test[[1]]