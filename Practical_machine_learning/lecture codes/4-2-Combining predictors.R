# Example with Wage data
# Create training,test and validation sets
library(ISLR)
data(Wage)
library(ggplot2)
library(caret)
Wage<-subset(Wage,select=-c(logwage))

# Create a building data set and validataion set
inBuild<-createDataPartition(y=Wage$wage,p=0.7,list=F)
validation<-Wage[-inBuild,]
buildData<-Wage[inBuild,]
inTrain<-createDataPartition(y=buildData$wage,p=0.7,list=F)
training<-buildData[inTrain,]
testing<-buildData[-inTrain,]

# Build two different models
mod1<-train(wage~.,method="glm",data=training)
mod2<-train(wage~.,method="rf",data=training,trControl=trainControl(method="cv"),number=3)

# Predict on the testing set
pred1<-predict(mod1,testing)
pred2<-predict(mod2,testing)
qplot(pred1,pred2,color=wage,data=testing)

# gam Generalized Additive Model using Splines
getModelInfo("gam")
# Fit a model that combines predictors
predDF<-data.frame(pred1,pred2,wage=testing$wage)
combModFit<-train(wage~.,method="gam",data=predDF)
combPred<-predict(combModFit,predDF)

# Testing errors
sqrt(sum((pred1-testing$wage)^2))
sqrt(sum((pred2-testing$wage)^2))
sqrt(sum((combPred-testing$wage)^2))

# Predict on validation data set
pred1V<-predict(mod1,validation)
pred2V<-predict(mod2,validation)
predVDF<-data.frame(pred1=pred1V,pred2=pred2V)
combPredV<-predict(combModFit,predVDF)

# Evaluate on validation
sqrt(sum((pred1V-validation$wage)^2))
sqrt(sum((pred2V-validation$wage)^2))
sqrt(sum((combPredV-validation$wage)^2))