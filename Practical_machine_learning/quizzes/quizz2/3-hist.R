library(AppliedPredictiveModeling)
data(concrete)
library(caret)
set.seed(975)
inTrain = createDataPartition(mixtures$CompressiveStrength, p = 3/4)[[1]]
training = mixtures[ inTrain,]
testing = mixtures[-inTrain,]
par(mfrow=c(2,2))
hist(training$Superplasticizer)
hist((log10(training$Superplasticizer+1)))
hist((log10(training$Superplasticizer)))
