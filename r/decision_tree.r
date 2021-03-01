library(rpart)
data(iris)

iris.rp=rpart(Species~.,data=iris,method="class")
plot(iris.rp,uniform=T,branch=0,margin=0.1,main="ClassificationTree")
text(iris.rp,use.n=T,fancy=T,col="blue")
library()