[Skip to contents](https://spark.apache.org/docs/latest/api/R/reference/spark.bisectingKmeans.html#main)
[ ![](https://spark.apache.org/images/spark-logo-rev.svg)](https://spark.apache.org/) [SparkR](https://spark.apache.org/docs/latest/api/R/index.html) 4.1.2
  * [Reference](https://spark.apache.org/docs/latest/api/R/reference/index.html)
  * [Articles](https://spark.apache.org/docs/latest/api/R/reference/spark.bisectingKmeans.html)
[SparkR - Practical Guide](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html)

  *

![](https://spark.apache.org/docs/latest/api/R/reference/spark.bisectingKmeans.html)
# Bisecting K-Means Clustering Model
`spark.bisectingKmeans.Rd`
Fits a bisecting k-means clustering model against a SparkDataFrame. Users can call `summary` to print a summary of the fitted model, `predict` to make predictions on new data, and `write.ml`/`read.ml` to save/load fitted models.
Get fitted result from a bisecting k-means model. Note: A saved-loaded model does not support this method.
## Usage[](https://spark.apache.org/docs/latest/api/R/reference/spark.bisectingKmeans.html#ref-usage)

```
spark.bisectingKmeans(data, formula, ...)

# S4 method for SparkDataFrame,formula
spark.bisectingKmeans(
  data,
  formula,
  k = 4,
  maxIter = 20,
  seed = NULL,
  minDivisibleClusterSize = 1
)

# S4 method for BisectingKMeansModel
summary[](https://spark.apache.org/docs/latest/api/R/reference/summary.html)(object)

# S4 method for BisectingKMeansModel
predict[](https://spark.apache.org/docs/latest/api/R/reference/predict.html)(object, newData)

# S4 method for BisectingKMeansModel
fitted[](https://spark.apache.org/docs/latest/api/R/reference/fitted.html)(object, method = c[](https://rdrr.io/r/base/c.html)("centers", "classes"))

# S4 method for BisectingKMeansModel,character
write.ml[](https://spark.apache.org/docs/latest/api/R/reference/write.ml.html)(object, path, overwrite = FALSE)
```

## Arguments[](https://spark.apache.org/docs/latest/api/R/reference/spark.bisectingKmeans.html#arguments)

data

a SparkDataFrame for training.

formula

a symbolic description of the model to be fitted. Currently only a few formula operators are supported, including '~', '.', ':', '+', '-', '*', and '^'. Note that the response variable of formula is empty in spark.bisectingKmeans.

...

additional argument(s) passed to the method.

k

the desired number of leaf clusters. Must be > 1. The actual number could be smaller if there are no divisible leaf clusters.

maxIter

maximum iteration number.

seed

the random seed.

minDivisibleClusterSize

The minimum number of points (if greater than or equal to 1.0) or the minimum proportion of points (if less than 1.0) of a divisible cluster. Note that it is an expert parameter. The default value should be good enough for most cases.

object

a fitted bisecting k-means model.

newData

a SparkDataFrame for testing.

method

type of fitted results, `"centers"` for cluster centers or `"classes"` for assigned classes.

path

the directory where the model is saved.

overwrite

overwrites or not if the output path already exists. Default is FALSE which means throw exception if the output path exists.
## Value[](https://spark.apache.org/docs/latest/api/R/reference/spark.bisectingKmeans.html#value)
`spark.bisectingKmeans` returns a fitted bisecting k-means model. `summary` returns summary information of the fitted model, which is a list. The list includes the model's `k` (number of cluster centers), `coefficients` (model cluster centers), `size` (number of data points in each cluster), `cluster` (cluster centers of the transformed data; cluster is NULL if is.loaded is TRUE), and `is.loaded` (whether the model is loaded from a saved file). `predict` returns the predicted values based on a bisecting k-means model. `fitted` returns a SparkDataFrame containing fitted values.
## Note[](https://spark.apache.org/docs/latest/api/R/reference/spark.bisectingKmeans.html#note)
spark.bisectingKmeans since 2.2.0
summary(BisectingKMeansModel) since 2.2.0
predict(BisectingKMeansModel) since 2.2.0
fitted since 2.2.0
write.ml(BisectingKMeansModel, character) since 2.2.0
## See also[](https://spark.apache.org/docs/latest/api/R/reference/spark.bisectingKmeans.html#see-also)
[predict](https://spark.apache.org/docs/latest/api/R/reference/predict.html), [read.ml](https://spark.apache.org/docs/latest/api/R/reference/read.ml.html), [write.ml](https://spark.apache.org/docs/latest/api/R/reference/write.ml.html)
## Examples[](https://spark.apache.org/docs/latest/api/R/reference/spark.bisectingKmeans.html#ref-examples)

```
if (FALSE) {
sparkR.session[](https://spark.apache.org/docs/latest/api/R/reference/sparkR.session.html)()
t <- as.data.frame[](https://spark.apache.org/docs/latest/api/R/reference/as.data.frame.html)(Titanic)
df <- createDataFrame[](https://spark.apache.org/docs/latest/api/R/reference/createDataFrame.html)(t)
model <- spark.bisectingKmeans(df, Class ~ Survived, k = 4)
summary[](https://spark.apache.org/docs/latest/api/R/reference/summary.html)(model)

# get fitted result from a bisecting k-means model
fitted.model <- fitted[](https://spark.apache.org/docs/latest/api/R/reference/fitted.html)(model, "centers")
showDF[](https://spark.apache.org/docs/latest/api/R/reference/showDF.html)(fitted.model)

# fitted values on training data
fitted <- predict[](https://spark.apache.org/docs/latest/api/R/reference/predict.html)(model, df)
head[](https://spark.apache.org/docs/latest/api/R/reference/head.html)(select[](https://spark.apache.org/docs/latest/api/R/reference/select.html)(fitted, "Class", "prediction"))

# save fitted model to input path
path <- "path/to/model"
write.ml[](https://spark.apache.org/docs/latest/api/R/reference/write.ml.html)(model, path)

# can also read back the saved model and print
savedModel <- read.ml[](https://spark.apache.org/docs/latest/api/R/reference/read.ml.html)(path)
summary[](https://spark.apache.org/docs/latest/api/R/reference/summary.html)(savedModel)
}

```

## On this page
Developed by [ The Apache Software Foundation](https://www.apache.org/).
Site built with [pkgdown](https://pkgdown.r-lib.org/) 2.0.1.
Using [preferably](https://preferably.amirmasoudabdol.name/?source=footer) template.
