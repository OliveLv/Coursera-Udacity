# the basic idea of bagging is to resample data,refit nonlinear model,
# then average those model fits together over resamples to get a smooth 
# model fit

# Ozone data
library(ElemStatLearn)
data(ozone,package="ElemStatLearn")
ozone<-ozone[order(ozone$ozone),]
head(ozone)

# Bagged loess
ll<-matrix(NA,nrow=10,ncol=155)
for(i in 1:10){
   ss<-sample(1:dim(ozone)[1],replace=T)
   ozone0<-ozone[ss,]
   ozone0<-ozone0[order(ozone0$ozone),]
   # a smooth curve,span is a measure of how smooth that fit will be
   loess0<-loess(temperature~ozone,data=ozone0,span=0.2)
   ll[i,]<-predict(loess0,newdata=data.frame(ozone=1:155))
}

plot(ozone$ozone,ozone$temperature,pch=19,cex=0.5)
for(i in 1:10){
   lines(1:155,ll[i,],col="grey",lwd=2)
}
  # the bagged loess curve
lines(1:155,apply(ll,2,mean),col="red",lwd=2)

# Bagging in caret , method= bagEarth,treebag,bagFDA
# More bagging in caret
library(caret)
predictors<-data.frame(ozone=ozone$ozone)
temperature<-ozone$temperature
treebag<-bag(predictors,temperature,B=10,bagControl=bagControl(
                   fit=ctreeBag$fit,
                   predict=ctreeBag$pred,
                   aggregate=ctreeBag$aggregate))

# Example of custom bagging(continued)
plot(ozone$ozone,temperature,col="lightgrey",pch=19)
  # the red dots represent the fit from a single conditional regression tree
points(ozone$ozone,predict(treebag$fits[[1]]$fit,predictors),pch=19,col="red")
  # the blue dots .....average of these ten conditional regression trees
points(ozone$ozone,predict(treebag,predictors),pch=19,col="blue")

# Parts of bagging
ctreeBag$fit
ctreeBag$pred
ctreeBag$aggregate