# Example: Wage data
library(ISLR)
library(ggplot2)
library(caret)
data(Wage)
summary(Wage)
 
# Get training/test sets
inTrain<-createDataPartition(y=Wage$wage,p=0.7,list=F)
training<-Wage[inTrain,]
testing<-Wage[-inTrain,]
dim(training)

# Feature plot (caret package)
featurePlot(x=training[,c("age","education","jobclass")],y=training$wage,plot="pairs")
# Qplot (ggplot2 package)
qplot(age,wage,data=training)
# Qplot with color (ggplot2 package)
qplot(age,wage,color=jobclass,data=training)
# Add regression smoothers (ggplot2 package)
qq<-qplot(age,wage,color=education,data=training)
qq+geom_smooth(method="lm",formula=y~x)
# cut2,making factors (Hmisc package)
cutWage<-cut2(training$wage,g=3)
table(cutWage)
# Boxplots with cut2
p1<-qplot(cutWage,age,data=training,fill=cutWage,geom="boxplot")
p1
# Boxplots with points overlayed
p2<-qplot(cutWage,age,data=training,fill=cutWage,geom=c("boxplot","jitter"))
grid.arrange(p1,p2,ncol=2)
# tables
t1<-table(cutWage,training$jobclass)
t1
prop.table(t1,1)
# Density plots
qplot(wage,color=education,data=training,geom="density")




