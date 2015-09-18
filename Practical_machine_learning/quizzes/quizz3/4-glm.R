library(ElemStatLearn)
data(SAheart)
set.seed(8484)
train = sample(1:dim(SAheart)[1],size=dim(SAheart)[1]/2,replace=F)
trainSA = SAheart[train,]
testSA = SAheart[-train,]

missClass=function(values,prediction){
 sum(((prediction > 0.5)*1) != values)/length(values)
}
set.seed(13234)
modelFit<-train(chd~age+alcohol+obesity+tobacco+typea+ldl,data=trainSA,method="glm")
pred<-predict(modelFit,testSA)
missClass(testSA$chd,pred)

pred<-predict(modelFit,trainSA)
missClass(trainSA$chd,pred)