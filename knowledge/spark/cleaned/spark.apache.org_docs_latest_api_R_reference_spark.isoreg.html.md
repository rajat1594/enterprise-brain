[Skip to contents](https://spark.apache.org/docs/latest/api/R/reference/spark.isoreg.html#main)
[ ![](https://spark.apache.org/images/spark-logo-rev.svg)](https://spark.apache.org/) [SparkR](https://spark.apache.org/docs/latest/api/R/index.html) 4.1.2
  * [Reference](https://spark.apache.org/docs/latest/api/R/reference/index.html)
  * [Articles](https://spark.apache.org/docs/latest/api/R/reference/spark.isoreg.html)
[SparkR - Practical Guide](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html)

  *

![](https://spark.apache.org/docs/latest/api/R/reference/spark.isoreg.html)
# Isotonic Regression Model
`spark.isoreg.Rd`
Fits an Isotonic Regression model against a SparkDataFrame, similarly to R's isoreg(). Users can print, make predictions on the produced model and save the model to the input path.
## Usage[](https://spark.apache.org/docs/latest/api/R/reference/spark.isoreg.html#ref-usage)

```
spark.isoreg(data, formula, ...)

# S4 method for SparkDataFrame,formula
spark.isoreg(
  data,
  formula,
  isotonic = TRUE,
  featureIndex = 0,
  weightCol = NULL
)

# S4 method for IsotonicRegressionModel
summary[](https://spark.apache.org/docs/latest/api/R/reference/summary.html)(object)

# S4 method for IsotonicRegressionModel
predict[](https://spark.apache.org/docs/latest/api/R/reference/predict.html)(object, newData)

# S4 method for IsotonicRegressionModel,character
write.ml[](https://spark.apache.org/docs/latest/api/R/reference/write.ml.html)(object, path, overwrite = FALSE)
```

## Arguments[](https://spark.apache.org/docs/latest/api/R/reference/spark.isoreg.html#arguments)

data

SparkDataFrame for training.

formula

A symbolic description of the model to be fitted. Currently only a few formula operators are supported, including '~', '.', ':', '+', and '-'.

...

additional arguments passed to the method.

isotonic

Whether the output sequence should be isotonic/increasing (TRUE) or antitonic/decreasing (FALSE).

featureIndex

The index of the feature if `featuresCol` is a vector column (default: 0), no effect otherwise.

weightCol

The weight column name.

object

a fitted IsotonicRegressionModel.

newData

SparkDataFrame for testing.

path

The directory where the model is saved.

overwrite

Overwrites or not if the output path already exists. Default is FALSE which means throw exception if the output path exists.
## Value[](https://spark.apache.org/docs/latest/api/R/reference/spark.isoreg.html#value)
`spark.isoreg` returns a fitted Isotonic Regression model. `summary` returns summary information of the fitted model, which is a list. The list includes model's `boundaries` (boundaries in increasing order) and `predictions` (predictions associated with the boundaries at the same index). `predict` returns a SparkDataFrame containing predicted values.
## Note[](https://spark.apache.org/docs/latest/api/R/reference/spark.isoreg.html#note)
spark.isoreg since 2.1.0
summary(IsotonicRegressionModel) since 2.1.0
predict(IsotonicRegressionModel) since 2.1.0
write.ml(IsotonicRegression, character) since 2.1.0
## Examples[](https://spark.apache.org/docs/latest/api/R/reference/spark.isoreg.html#ref-examples)

```
if (FALSE) {
sparkR.session[](https://spark.apache.org/docs/latest/api/R/reference/sparkR.session.html)()
data <- list[](https://rdrr.io/r/base/list.html)(list[](https://rdrr.io/r/base/list.html)(7.0, 0.0), list[](https://rdrr.io/r/base/list.html)(5.0, 1.0), list[](https://rdrr.io/r/base/list.html)(3.0, 2.0),
        list[](https://rdrr.io/r/base/list.html)(5.0, 3.0), list[](https://rdrr.io/r/base/list.html)(1.0, 4.0))
df <- createDataFrame[](https://spark.apache.org/docs/latest/api/R/reference/createDataFrame.html)(data, c[](https://rdrr.io/r/base/c.html)("label", "feature"))
model <- spark.isoreg(df, label ~ feature, isotonic = FALSE)
# return model boundaries and prediction as lists
result <- summary[](https://spark.apache.org/docs/latest/api/R/reference/summary.html)(model, df)
# prediction based on fitted model
predict_data <- list[](https://rdrr.io/r/base/list.html)(list[](https://rdrr.io/r/base/list.html)(-2.0), list[](https://rdrr.io/r/base/list.html)(-1.0), list[](https://rdrr.io/r/base/list.html)(0.5),
                list[](https://rdrr.io/r/base/list.html)(0.75), list[](https://rdrr.io/r/base/list.html)(1.0), list[](https://rdrr.io/r/base/list.html)(2.0), list[](https://rdrr.io/r/base/list.html)(9.0))
predict_df <- createDataFrame[](https://spark.apache.org/docs/latest/api/R/reference/createDataFrame.html)(predict_data, c[](https://rdrr.io/r/base/c.html)("feature"))
# get prediction column
predict_result <- collect[](https://spark.apache.org/docs/latest/api/R/reference/collect.html)(select[](https://spark.apache.org/docs/latest/api/R/reference/select.html)(predict[](https://spark.apache.org/docs/latest/api/R/reference/predict.html)(model, predict_df), "prediction"))

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
