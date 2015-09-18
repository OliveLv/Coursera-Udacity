library(pgmm)
data(olive)
olive = olive[,-1]
modelFit<-train(Area~.,data=olive,method="rpart")
newdata=as.data.frame(t(colMeans(olive)))
predict(modelFit,newdata)