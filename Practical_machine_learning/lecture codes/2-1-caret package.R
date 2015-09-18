# Spam Example: Data splitting
library(lattice)
library(ggplot2)
library(caret)
# load package kernlab to get data spam
library(kernlab)
data(spam)
# list=T class(inTrain)=list
# list=F class(inTrain)=matrix
inTrain<-createDataPartition(y=spam$type,p=0.75,list=F)
training<-spam[inTrain,]
testing<-spam[-inTrain,]
dim(training)

# Spam Example: Fit a model
set.seed(32343)
# y~X means y is dependent variables,while X is independent variables
# . means all the other variables in the data frame
modelFit<-train(type~.,data=training,method="glm")
# demonstrate model
modelFit

# Spam Example: Final model
modelFit$finalModel

# Spam Example: Prediction
predictions<-predict(modelFit,newdata=testing)
predictions

# Spam Example: Confusion Matrix
confusionMatrix(predictions,testing$type)

