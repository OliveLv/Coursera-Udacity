# Load example data
library(ISLR)
library(lattice)
library(ggplot2)
library(caret)
data(Wage)
inTrain<-createDataPartition(y=Wage$wage,p=0.7,list=F)
training<-Wage[inTrain,]
testing<-Wage[-inTrain,]

# Common covariates to add,dummy variables
table(training$jobclass)
# dummy variables means ÐéÄâ±äÁ¿
dummies<-dummyVars(wage~jobclass,data=training)
head(predict(dummies,newdata=training))

# Removing zero covariates
nsv<-nearZeroVar(training,saveMetrics=T)
 # showing freqence occurence for a word....
nsv

# Spline basis
library(splines)
bsBasis<-bs(training$age,df=3)
bsBasis

# Fitting curves with splines
lm1<-lm(wage~bsBasis,data=training)
plot(training$age,training$wage,pch=19,cex=0.5)
points(training$age,predict(lm1,newdata=training),col="red",pch=19,cex=0.5)
 # using linear regression model
lm2<-lm(wage~age,data=training)
points(training$age,predict(lm2,newdata=training),col="blue",pch=19,cex=0.5)

# Splines on the test set
predict(bsBasis,age=testing$age)