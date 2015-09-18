# think of as an extension of bagging for classification and regression trees
# boostrap samples
# boostrap variables

# Iris data
data(iris)
library(caret)
inTrain<-createDataPartition(y=iris$Species,p=0.7,list=F)
training<-iris[inTrain,]
testing<-iris[-inTrain,]

# Random forests
modelFit<-train(Species~.,method="rf",data=training,prox=T)
modelFit
summary(modelFit$finalModel)

# Getting a single tree
getTree(modelFit$finalModel,k=2)

# Class "centers"
  # prox means the proximity (or similarity) matrix
  # classCenter(x,label,prox,nNbr)
  # x : a matrix or data frame
  # label : group lables of the row in x
  # nNbr : number of nearest neighbors used to find the prototypes
  # classCenter return a matrix
  # training[,c(3,4)] means col of Petal.Length and Petal.Width
irisP<-classCenter(training[,c(3,4)],training$Species,modelFit$finalModel$prox)
  class(irisP)
irisP<-as.data.frame(irisP)
  colnames(irisP)
  # create new col naming "Species"
irisP$Species<-rownames(irisP)
  colnames(irisP)
  irisP
  # plot all data with x=Petal.Width y=Petal.Length
p<-qplot(Petal.Width,Petal.Length,col=Species,data=training)
  # plot center points
p+geom_point(aes(x=Petal.Width,y=Petal.Length,col=Species),size=5,shape=4,data=irisP)


# Predicting new values
pred<-predict(modelFit,testing)
testing$predRight<-pred==testing$Species
table(pred,testing$Species)

qplot(Petal.Width,Petal.Length,color=predRight,data=testing,main="newdata Predictions")