# data("AirPassengers")
# str(AirPassengers)
# data=read.csv(file="http://eric.univ-lyon2.fr/~jjacques/Download/DataSet/varicelle.csv")
# plot(data$x)
# varicelle<-ts(data$x,start=c(1931,1),end=c(1972,6),freq=12)
# plot(varicelle)
# mean(varicelle)
# var(varicelle)
# tmp=acf(varicelle,type="cov",plot = FALSE)
# tmp$acf[1:3,1,1]
# plot(tmp)
# tmp=acf(varicelle,type="cor",plot = FALSE)
# tmp$acf[1:3,1,1]
# plot(tmp)
# serie=2*(1:100)+4
# par(mfrow=c(1,2))
# plot(ts(serie))
# acf(serie)
# serie=cos(2*pi/12*(1:100))
# par(mfrow=c(1,2))
# plot(ts(serie))
# acf(serie)
# tmp=pacf(varicelle,type="cor",plot = FALSE)
# tmp$acf[1:3,1,1]
# plot(tmp)


## exercice
## import des donnees du fichier varicelle.csv
data<-read.csv(file="http://eric.univ-lyon2.fr/~jjacques/Download/DataSet/varicelle.csv")
attach(data)

head(data)

# transform en serie temporelle
str(data)

