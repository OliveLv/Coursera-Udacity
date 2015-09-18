set.seed(3523)
library(AppliedPredictiveModeling)
library(caret)
data(concrete)
inTrain = createDataPartition(concrete$CompressiveStrength, p = 3/4)[[1]]
training = concrete[ inTrain,]
testing = concrete[-inTrain,]
set.seed(233)
modelFit<-train(CompressiveStrength~.,method="lasso",data=training)
modelFit$finalModel
plot(modelFit$finalModel,xvar="penalty")