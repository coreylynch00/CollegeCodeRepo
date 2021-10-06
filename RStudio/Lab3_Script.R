######################################################
### Question 1 - Generating a R script
######################################################

x =seq(2,20,2) # vector with even numbers from 1 to 20
x[1:5] # print the first 5 entries in x
mean(x)

# median(x) # comments stop code being executed


######################################################
### Question 2 - Analysis of Iris Data
######################################################

library(datasets)
help(iris) # find out more information about the iris data frame

# There are 150 rows in the iris data frame.
# There are 5 variables in the iris data frame.

names(iris) # prints titles of columns
head(iris) # prints first 6 rows 
tail(iris) # prints last 6 rows 

attach(iris)

### Summary statistics - Ignoring iris species

# Measures of centrality
# Mean values
mean_SL = mean(Sepal.Length)
mean_SW = mean(Sepal.Width)

# Median values
median_SL = median(Sepal.Length)
median_SW = median(Sepal.Width)

# Measures of variability
# Standard deviation
sd_SL = sd(Sepal.Length)
sd_SW = sd(Sepal.Width)

# IQR
iqr_SL = IQR(Sepal.Length)
iqr_SW = IQR(Sepal.Width)

# Coefficient of variation
CV_SL = sd_SL/mean_SL*100
CV_SW = sd_SW/mean_SW*100

# As the CV of the sepal width is slightly higher than 
# the CV of the sepal length, thus the sepal width 
# demonstrates slightly higher variability.

# Measure of skewness
CS_SL = 3*(mean_SL-median_SL)/sd_SL
CS_SW = 3*(mean_SW-median_SW)/sd_SW

# Both CVs are positive. Thus both data sets are postiviely showed
# As CS of the sepal width is higher than the CV of 
# the sepal length, the sepal width is more skewed.

### Graphical Methods

# Histograms of numerical data in iris data frame
hist(Sepal.Length)
hist(Sepal.Width)
hist(Petal.Length)
hist(Petal.Width)

# The Sepal histograms both look approximately symmetric.
# However, the petal histograms both have two distinct 
# distributions. This ie because we have not allowed
# for the different species of iris.

table(Species) # to see frequencies for categories

# Histograms for each species using options
par(mfrow = c(3, 1)) # Put graphs in 3 rows and 1 column
hist(Petal.Width [Species == "setosa"], xlim = c(0, 3), breaks = 9, main = "Petal Width for Setosa", xlab = "",col = "red")
hist(Petal.Width [Species == "versicolor"], xlim = c(0, 3), breaks = 9, main = "Petal Width for Versicolor", xlab = "", col = "purple") 
hist(Petal.Width [Species == "virginica"],  xlim = c(0, 3), breaks = 9, main = "Petal Width for Virginica", xlab = "", col = "blue")	

# par(mfrow = c(3, 1)) sets up the plot window so that
# there are 3 plots arranged one over the other. In contrast
# par(mfrow = c(1, 3)) sets up the plot window so that
# there are 3 plots arranged beside each other

# xlim = x(0,3) gives the range on the x-axis
# breaks is a a vector giving the breakpoints between 
# histogram cells

# Boxplots for each species using options
par(mfrow = c(1, 3)) # Put graphs in 1 rows and 3 columns
boxplot(Petal.Width [Species == "setosa"],  main = "Petal Width for Setosa", xlab = "",col = "red")
boxplot(Petal.Width [Species == "versicolor"], main = "Petal Width for Versicolor", xlab = "", col = "purple") 
boxplot(Petal.Width [Species == "virginica"], main = "Petal Width for Virginica", xlab = "", col = "blue")	

# The setosa data has two outliers (the two circles
# above the top whisker)

### Summary Statistics - Allowing for flower spcies

### Compute summary stats data frames for sepal 
### length by species category
aggregate(x = Sepal.Length,                # Specify data column
          by = list(Species),              # Specify group indicator
          FUN = mean)                      # Specify function (i.e. mean)

aggregate(x = Sepal.Length,by = list(Species), FUN = median)
aggregate(x = Sepal.Length,by = list(Species), FUN = sd)
aggregate(x = Sepal.Length,by = list(Species), FUN = IQR)

### Assign summary stats data frames for sepal 
### length by species category
mean_Sepal.Length=aggregate(x = Sepal.Length,by = list(Species), FUN = mean)
median_Sepal.Length=aggregate(x = Sepal.Length,by = list(Species), FUN = median)
sd_Sepal.Length=aggregate(x = Sepal.Length,by = list(Species), FUN = sd)

### Assign mean, median and sd value for setosa petal length to variables
mean_Sepal_Length_setosa = mean_Sepal.Length[1,2]
median_Sepal_Length_setosa = median_Sepal.Length[1,2]
sd_Sepal_Length_setosa = sd_Sepal.Length[1,2]

### coefficient of skewness for setosa petal length
3*(mean_Sepal_Length_setosa-median_Sepal_Length_setosa)/sd_Sepal_Length_setosa

# The CV is almost 0. This the data is approximately symmetric.
