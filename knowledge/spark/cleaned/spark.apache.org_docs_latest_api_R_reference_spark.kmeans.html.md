[Skip to contents](https://spark.apache.org/docs/latest/api/R/reference/spark.kmeans.html#main)
[ ![](https://spark.apache.org/images/spark-logo-rev.svg)](https://spark.apache.org/) [SparkR](https://spark.apache.org/docs/latest/api/R/index.html) 4.1.2
  * [Reference](https://spark.apache.org/docs/latest/api/R/reference/index.html)
  * [Articles](https://spark.apache.org/docs/latest/api/R/reference/spark.kmeans.html)
[SparkR - Practical Guide](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html)

  *

![](https://spark.apache.org/docs/latest/api/R/reference/spark.kmeans.html)
# K-Means Clustering Model
`spark.kmeans.Rd`
Fits a k-means clustering model against a SparkDataFrame, similarly to R's kmeans(). Users can call `summary` to print a summary of the fitted model, `predict` to make predictions on new data, and `write.ml`/`read.ml` to save/load fitted models.
## Usage[](https://spark.apache.org/docs/latest/api/R/reference/spark.kmeans.html#ref-usage)

```
spark.kmeans(data, formula, ...)

# S4 method for SparkDataFrame,formula
spark.kmeans(
  data,
  formula,
  k = 2,
  maxIter = 20,
  initMode = c[](https://rdrr.io/r/base/c.html)("k-means||", "random"),
  seed = NULL,
  initSteps = 2,
  tol = 1e-04
)

# S4 method for KMeansModel
summary[](https://spark.apache.org/docs/latest/api/R/reference/summary.html)(object)

# S4 method for KMeansModel
predict[](https://spark.apache.org/docs/latest/api/R/reference/predict.html)(object, newData)

# S4 method for KMeansModel,character
write.ml[](https://spark.apache.org/docs/latest/api/R/reference/write.ml.html)(object, path, overwrite = FALSE)
```

## Arguments[](https://spark.apache.org/docs/latest/api/R/reference/spark.kmeans.html#arguments)

data

a SparkDataFrame for training.

formula

a symbolic description of the model to be fitted. Currently only a few formula operators are supported, including '~', '.', ':', '+', and '-'. Note that the response variable of formula is empty in spark.kmeans.

...

additional argument(s) passed to the method.

k

number of centers.

maxIter

maximum iteration number.

initMode

the initialization algorithm chosen to fit the model.

seed

the random seed for cluster initialization.

initSteps

the number of steps for the k-means|| initialization mode. This is an advanced setting, the default of 2 is almost always enough. Must be > 0.

tol

convergence tolerance of iterations.

object

a fitted k-means model.

newData

a SparkDataFrame for testing.

path

the directory where the model is saved.

overwrite

overwrites or not if the output path already exists. Default is FALSE which means throw exception if the output path exists.
## Value[](https://spark.apache.org/docs/latest/api/R/reference/spark.kmeans.html#value)
`spark.kmeans` returns a fitted k-means model. `summary` returns summary information of the fitted model, which is a list. The list includes the model's `k` (the configured number of cluster centers), `coefficients` (model cluster centers), `size` (number of data points in each cluster), `cluster` (cluster centers of the transformed data), is.loaded (whether the model is loaded from a saved file), and `clusterSize` (the actual number of cluster centers. When using initMode = "random", `clusterSize` may not equal to `k`). `predict` returns the predicted values based on a k-means model.
## Note[](https://spark.apache.org/docs/latest/api/R/reference/spark.kmeans.html#note)
spark.kmeans since 2.0.0
summary(KMeansModel) since 2.0.0
predict(KMeansModel) since 2.0.0
write.ml(KMeansModel, character) since 2.0.0
## See also[](https://spark.apache.org/docs/latest/api/R/reference/spark.kmeans.html#see-also)
[predict](https://spark.apache.org/docs/latest/api/R/reference/predict.html), [read.ml](https://spark.apache.org/docs/latest/api/R/reference/read.ml.html), [write.ml](https://spark.apache.org/docs/latest/api/R/reference/write.ml.html)
## Examples[](https://spark.apache.org/docs/latest/api/R/reference/spark.kmeans.html#ref-examples)

```
if (FALSE) {
sparkR.session[](https://spark.apache.org/docs/latest/api/R/reference/sparkR.session.html)()
t <- as.data.frame[](https://spark.apache.org/docs/latest/api/R/reference/as.data.frame.html)(Titanic)
df <- createDataFrame[](https://spark.apache.org/docs/latest/api/R/reference/createDataFrame.html)(t)
model <- spark.kmeans(df, Class ~ Survived, k = 4, initMode = "random")
summary[](https://spark.apache.org/docs/latest/api/R/reference/summary.html)(model)

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
