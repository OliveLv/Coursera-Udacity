# boosting method in R
# gbm boosting with trees
# mboost model based boosting
# ada statistical boosting based on additive logistic regression
# gamBoost for boosting generalized additive models

# Wage example
library(ISLR)
data(Wage)
library(ggplot2)
library(caret)
Wage<-subset(Wage,select=-c(logwage))
inTrain<-createDataPartition(y=Wage$wage,p=0.7,list=F)
training<-Wage[inTrain,]
testing<-Wage[-inTrain,]

# Fit the model
modelFit<-train(wage~.,method="gbm",data=training,verbose=F)
print(modelFit)

# Plot the results
qplot(predict(modelFit,testing),testing$wage)