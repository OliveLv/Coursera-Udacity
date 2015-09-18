# Naive bayes
# Example : Iris data
data(iris)
library(ggplot2)
names(iris)
table(iris$Species)

# Create training and test sets
library(caret)
inTrain<-createDataPartition(y=iris$Species,p=0.7,list=F)
training<-iris[inTrain,]
testing<-iris[-inTrain,]
dim(training)
dim(testing)

# Build predictions
  # lda linear discriminate analysis 
modlda<-train(Species~.,data=training,method="lda")
  # naive bayes regression
modnb<-train(Species~.,data=training,method="nb")
plda<-predict(modlda,testing)
pnb<-predict(modnb,testing)
   # means result of lda and nb are similar
table(plda,pnb)

# Comparision of results
equalPredictions<-(plda==pnb)
qplot(Petal.Width,Sepal.Width,color=equalPredictions,data=testing)