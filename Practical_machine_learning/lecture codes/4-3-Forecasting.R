# time series data
# Google data
library(quantmod)
from.dat<-as.Date("01/01/08",format="%m/%d/%y")
to.dat<-as.Date("12/31/13",format="%m/%d/%y")
getSymbols("GOOG",src="google",from=from.dat,to=to.dat)

data.file<-file.path("goog.csv")
GOOG<-read.csv(data.file,head=T,sep=',')
head(GOOG)

# Summarize monthly and store as time series
 # convert to a monthly time series
mGoog<-to.monthly(GOOG)
 # get open prices monthly
googOpen<-Op(mGoog)
ts1<-ts(googOpen,frequency=12)
plot(ts1,xlab="Years+1",ylab="GOOG")

# Decompose a time series into parts,decomposition includes Trend,Seasonal,Cyclic
plot(decompose(ts1),xlab="Years+1")

# Training and test sets
ts1Train<-window(ts1,start=1,end=5)
ts1Test<-window(ts1,start=5,end=(7-0.01))
ts1Train

# Simple moving average
plot(ts1Train)
lines(ma(ts1Train,order=3),col="red")

# Exponential soomthing
est1<-est(ts1Train,model="MMM")
fcast<-forecast(est)
plot(fcast)
lines(ts1Test,col="red")

# Geg the accuracy
accuracy(fcast,ts1Test)
 