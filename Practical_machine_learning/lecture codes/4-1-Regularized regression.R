# function in caret ridge lasso relaxo
# Prostate cancer
library(ElemStatLearn)
data(prostate)
str(prostate)

# Another issue for high-dimensional data
small=prostate[1:5,]
lm(lpsa~.,data=small)