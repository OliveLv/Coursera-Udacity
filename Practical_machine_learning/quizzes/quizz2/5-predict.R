library(caret)
library(AppliedPredictiveModeling)
set.seed(3433)
data(AlzheimerDisease)
adData = data.frame(diagnosis,predictors)
inTrain = createDataPartition(adData$diagnosis, p = 3/4)[[1]]
training = adData[ inTrain,]
testing = adData[-inTrain,]

# Create a training data set consisting of only the predictors 
# with variable names beginning with IL and the diagnosis
IL<-grep("IL_",colnames(training))
n<-length(IL)
for(i in 1:(n-1)){
  if(i==1){
    newTrain<-data.frame(training[[IL[i]]])
    newTest<-data.frame(testing[[IL[i]]])
  }
  else{
    newTrain<-cbind(newTrain,training[[IL[i]]])
    newTest<-cbind(newTest,testing[[IL[i]]])
  }
}


colnames(newTrain)<-colnames(training)[IL[1:(n-1)]]
newTrain<-cbind(newTrain,diagnosis=training$diagnosis)

colnames(newTest)<-colnames(testing)[IL[1:(n-1)]]
newTest<-cbind(newTest,diagnosis=testing$diagnosis)

# Non-PCA 
modelFit<-train(diagnosis~.,method="glm",data=newTrain)
confusionMatrix(newTest$diagnosis,predict(modelFit,newTest))

# PCA
ctrl <- trainControl(preProcOptions = list(thresh = 0.8))
modelFit2<-train(diagnosis~.,method="glm",preProcess="pca",data=newTrain,trControl=ctrl)
confusionMatrix(newTest$diagnosis,predict(modelFit2,newTest))
