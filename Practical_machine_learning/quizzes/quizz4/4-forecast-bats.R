library(lubridate)  # For year() function below
dat = read.csv("gaData.csv")
training = dat[year(dat$date) < 2012,]
testing = dat[(year(dat$date)) > 2011,]
tstrain = ts(training$visitsTumblr)
tstest = ts(testing$visitsTumblr)
library(forecast)
fit<-bats(tstrain)
# h means Number of periods for forecasting 
forcast<-forecast(fit,h=length(testing$visitsTumblr))
# get lower and upper with the 95% prediction interval bounds
low<-forcast$lower[,2]
up<-forcast$upper[,2]
test<-testing$visitsTumblr
n<-length(test)
s<-0
for(i in 1:n){
  if(test[i]<=up[i]&&test[i]>=low[i]){
  s<-s+1
}
}
print(s/n)