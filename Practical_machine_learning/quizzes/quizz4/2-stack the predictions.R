library(caret)
library(gbm)
set.seed(3433)
library(AppliedPredictiveModeling)
data(AlzheimerDisease)
adData = data.frame(diagnosis,predictors)
inTrain = createDataPartition(adData$diagnosis, p = 3/4)[[1]]
training = adData[ inTrain,]
testing = adData[-inTrain,]
set.seed(62433)
mod1<-train(diagnosis~.,method="rf",data=training)
mod2<-train(diagnosis~.,method="gbm",data=training)
mod3<-train(diagnosis~.,method="lda",data=training)
pred1<-predict(mod1,testing)
pred2<-predict(mod2,testing)
pred3<-predict(mod3,testing)
confusion1<-confusionMatrix(pred1,testing$diagnosis)
confusion2<-confusionMatrix(pred2,testing$diagnosis)
confusion3<-confusionMatrix(pred3,testing$diagnosis)
comb<-data.frame(pred1,pred2,pred3,diagnosis=testing$diagnosis)
combMod<-train(diagnosis~.,method="rf",data=comb)
combPred<-predict(combMod,comb)
confusion4<-confusionMatrix(combPred,testing$diagnosis)
confusion1
confusion2
confusion3
confusion4
