library(AppliedPredictiveModeling)
data(segmentationOriginal)
library(caret)

# Subset the data to a training set and testing set based 
# on the Case variable in the data set.
training<-segmentationOriginal[segmentationOriginal$Case=="Train",]
testing<-segmentationOriginal[segmentationOriginal$Case=="Test",]

# Set the seed to 125 and fit a CART model with rpart method using
# all predictor variables and default caret settings
set.seed(125)
modelFit<-train(Class~.,data=training,method="rpart")

# print classification tree
# print(modelFit$finalModel)


# print classification tree
library(rattle)
fancyRpartPlot(modelFit$finalModel)


