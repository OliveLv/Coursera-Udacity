# Example £º Iris Data
data(iris)
library(ggplot2)
names(iris)
table(iris$Species)

# Create training and test set
library(caret)
inTrain<-createDataPartition(y=iris$Species,p=0.7,list=F)
training=iris[inTrain,]
testing=iris[-inTrain,]
dim(training)
dim(testing)

# Iris petal widths/sepal width
qplot(Petal.Width,Sepal.Length,color=Species,data=training)

# Iris petal widths/sepal width
library(caret)
 # rpart for doing a regression and classification algorithm
modelFit<-train(Species~.,method="rpart",data=training)
print(modelFit$finalModel)

# Plot tree
plot(modelFit$finalModel,uniform=T,main="Classification Tree")
text(modelFit$finalModel,use.n=T,all=T,cex=.8)

# Prettier plots
library(rattle)
fancyRpartPlot(modelFit$finalModel)

# Predicting new values
predict(modelFit,newdata=testing)
