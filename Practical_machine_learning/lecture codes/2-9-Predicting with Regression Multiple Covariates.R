# Example : Wage data
library(ISLR)
library(ggplot2)
library(caret)
data(Wage)
Wage<-subset(Wage,select=-c(logwage))
summary(Wage)

# Get training/test sets
inTrain<-createDataPartition(y=Wage$wage,p=0.7,list=F)
training<-Wage[inTrain,]
testing<-Wage[-inTrain,]
dim(training)
dim(testing)

# Feature plot
featurePlot(x=training[,c("age","education","jobclass")],y=training$wage,plot="pairs")

# Plot age versus wage
qplot(age,wage,data=training)

# Plot age versus wage color by jobclass
qplot(age,wage,color=jobclass,data=training)

# Plot age versus wage color by education
qplot(age,wage,color=education,data=training)

# Fit a linear model
modelFit<-train(wage~age+jobclass+education,method="glm",data=training)
finalModel<-modelFit$finalModel
print(modelFit)

# Diagnostics  Õï¶Ï
  # residuals ²Ð²î
plot(finalModel,1,pch=19,cex=0.5,col="#00000010")

# Color by variables not used in the model
qplot(finalModel$fitted,finalModel$residuals,color=race,data=training)

# Plot by index
plot(finalModel$residuals,pch=19)

# Predicted versus truth in test set
pred<-predict(modelFit,testing)
qplot(wage,pred,color=year,data=testing)

# use all covariates
modelFitAll<-train(wage~.,data=training,method="lm")
pred<-predict(modelFitAll,testing)
qplot(wage,pred,data=testing)