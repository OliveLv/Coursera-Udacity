# Iris example ignoring species labels
data(iris)
library(ggplot2)
inTrain<-createDatePartition(y=iris$Species,p=0.7,list=F)
training<-iris[inTrain,]
testing<-iris[-inTrain,]

# Cluster with k-means
 summary(training)
 # exist substaitial NAs
train<-training[!is.na(training$Species),]
kMeans1<-kmeans(subset(train,select=-c(Species)),center=3)
train$clusters<-as.factor(kMeans1$cluster)
qplot(Petal.Width,Petal.Length,color=clusters,data=train)

# Compare to real tables
table(kMeans1$cluster,train$Species)

# Build predictor
modFit<-train(clusters~.,data=subset(train,select=-c(Species)),method="rpart")
table(predict(modFit,train),train$Species)

# Apply on test
testClusterPred<-predict(modFit,testing)
table(testClusterPred,testing$Species)
