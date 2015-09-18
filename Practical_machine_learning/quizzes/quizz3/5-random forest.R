library(ElemStatLearn)
data(vowel.train)
data(vowel.test) 
library(caret)
set.seed(33833)
vowel.train$y<-factor(vowel.train$y)

modelFit<-train(y~.,data=vowel.train,method="rf")
varImp(modelFit)

## the following code can get correct answer ,while above code cannot
fit=randomForest(y~.,data=vowel.train,importance=T)
order(fit$importance[,13],decreasing=T)