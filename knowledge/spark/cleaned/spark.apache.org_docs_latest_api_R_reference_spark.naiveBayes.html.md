[Skip to contents](https://spark.apache.org/docs/latest/api/R/reference/spark.naiveBayes.html#main)
[ ![](https://spark.apache.org/images/spark-logo-rev.svg)](https://spark.apache.org/) [SparkR](https://spark.apache.org/docs/latest/api/R/index.html) 4.1.2
  * [Reference](https://spark.apache.org/docs/latest/api/R/reference/index.html)
  * [Articles](https://spark.apache.org/docs/latest/api/R/reference/spark.naiveBayes.html)
[SparkR - Practical Guide](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html)

  *

![](https://spark.apache.org/docs/latest/api/R/reference/spark.naiveBayes.html)
# Naive Bayes Models
`spark.naiveBayes.Rd`
`spark.naiveBayes` fits a Bernoulli naive Bayes model against a SparkDataFrame. Users can call `summary` to print a summary of the fitted model, `predict` to make predictions on new data, and `write.ml`/`read.ml` to save/load fitted models. Only categorical data is supported.
## Usage[](https://spark.apache.org/docs/latest/api/R/reference/spark.naiveBayes.html#ref-usage)

```
spark.naiveBayes(data, formula, ...)

# S4 method for SparkDataFrame,formula
spark.naiveBayes(
  data,
  formula,
  smoothing = 1,
  handleInvalid = c[](https://rdrr.io/r/base/c.html)("error", "keep", "skip")
)

# S4 method for NaiveBayesModel
summary[](https://spark.apache.org/docs/latest/api/R/reference/summary.html)(object)

# S4 method for NaiveBayesModel
predict[](https://spark.apache.org/docs/latest/api/R/reference/predict.html)(object, newData)

# S4 method for NaiveBayesModel,character
write.ml[](https://spark.apache.org/docs/latest/api/R/reference/write.ml.html)(object, path, overwrite = FALSE)
```

## Arguments[](https://spark.apache.org/docs/latest/api/R/reference/spark.naiveBayes.html#arguments)

data

a `SparkDataFrame` of observations and labels for model fitting.

formula

a symbolic description of the model to be fitted. Currently only a few formula operators are supported, including '~', '.', ':', '+', and '-'.

...

additional argument(s) passed to the method. Currently only `smoothing`.

smoothing

smoothing parameter.

handleInvalid

How to handle invalid data (unseen labels or NULL values) in features and label column of string type. Supported options: "skip" (filter out rows with invalid data), "error" (throw an error), "keep" (put invalid data in a special additional bucket, at index numLabels). Default is "error".

object

a naive Bayes model fitted by `spark.naiveBayes`.

newData

a SparkDataFrame for testing.

path

the directory where the model is saved.

overwrite

overwrites or not if the output path already exists. Default is FALSE which means throw exception if the output path exists.
## Value[](https://spark.apache.org/docs/latest/api/R/reference/spark.naiveBayes.html#value)
`spark.naiveBayes` returns a fitted naive Bayes model. `summary` returns summary information of the fitted model, which is a list. The list includes `apriori` (the label distribution) and `tables` (conditional probabilities given the target label). `predict` returns a SparkDataFrame containing predicted labeled in a column named "prediction".
## Note[](https://spark.apache.org/docs/latest/api/R/reference/spark.naiveBayes.html#note)
spark.naiveBayes since 2.0.0
summary(NaiveBayesModel) since 2.0.0
predict(NaiveBayesModel) since 2.0.0
write.ml(NaiveBayesModel, character) since 2.0.0
## See also[](https://spark.apache.org/docs/latest/api/R/reference/spark.naiveBayes.html#see-also)
e1071: <https://cran.r-project.org/package=e1071>
[write.ml](https://spark.apache.org/docs/latest/api/R/reference/write.ml.html)
## Examples[](https://spark.apache.org/docs/latest/api/R/reference/spark.naiveBayes.html#ref-examples)

```
if (FALSE) {
data <- as.data.frame[](https://spark.apache.org/docs/latest/api/R/reference/as.data.frame.html)(UCBAdmissions)
df <- createDataFrame[](https://spark.apache.org/docs/latest/api/R/reference/createDataFrame.html)(data)

# fit a Bernoulli naive Bayes model
model <- spark.naiveBayes(df, Admit ~ Gender + Dept, smoothing = 0)

# get the summary of the model
summary[](https://spark.apache.org/docs/latest/api/R/reference/summary.html)(model)

# make predictions
predictions <- predict[](https://spark.apache.org/docs/latest/api/R/reference/predict.html)(model, df)

# save and load the model
path <- "path/to/model"
write.ml[](https://spark.apache.org/docs/latest/api/R/reference/write.ml.html)(model, path)
savedModel <- read.ml[](https://spark.apache.org/docs/latest/api/R/reference/read.ml.html)(path)
summary[](https://spark.apache.org/docs/latest/api/R/reference/summary.html)(savedModel)
}

```

## On this page
Developed by [ The Apache Software Foundation](https://www.apache.org/).
Site built with [pkgdown](https://pkgdown.r-lib.org/) 2.0.1.
Using [preferably](https://preferably.amirmasoudabdol.name/?source=footer) template.
