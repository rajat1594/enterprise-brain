[Skip to contents](https://spark.apache.org/docs/latest/api/R/reference/spark.fmRegressor.html#main)
[ ![](https://spark.apache.org/images/spark-logo-rev.svg)](https://spark.apache.org/) [SparkR](https://spark.apache.org/docs/latest/api/R/index.html) 4.1.2
  * [Reference](https://spark.apache.org/docs/latest/api/R/reference/index.html)
  * [Articles](https://spark.apache.org/docs/latest/api/R/reference/spark.fmRegressor.html)
[SparkR - Practical Guide](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html)

  *

![](https://spark.apache.org/docs/latest/api/R/reference/spark.fmRegressor.html)
# Factorization Machines Regression Model
`spark.fmRegressor.Rd`
`spark.fmRegressor` fits a factorization regression model against a SparkDataFrame. Users can call `summary` to print a summary of the fitted model, `predict` to make predictions on new data, and `write.ml`/`read.ml` to save/load fitted models.
## Usage[](https://spark.apache.org/docs/latest/api/R/reference/spark.fmRegressor.html#ref-usage)

```
spark.fmRegressor(data, formula, ...)

# S4 method for SparkDataFrame,formula
spark.fmRegressor(
  data,
  formula,
  factorSize = 8,
  fitLinear = TRUE,
  regParam = 0,
  miniBatchFraction = 1,
  initStd = 0.01,
  maxIter = 100,
  stepSize = 1,
  tol = 1e-06,
  solver = c[](https://rdrr.io/r/base/c.html)("adamW", "gd"),
  seed = NULL,
  stringIndexerOrderType = c[](https://rdrr.io/r/base/c.html)("frequencyDesc", "frequencyAsc", "alphabetDesc",
    "alphabetAsc")
)

# S4 method for FMRegressionModel
summary[](https://spark.apache.org/docs/latest/api/R/reference/summary.html)(object)

# S4 method for FMRegressionModel
predict[](https://spark.apache.org/docs/latest/api/R/reference/predict.html)(object, newData)

# S4 method for FMRegressionModel,character
write.ml[](https://spark.apache.org/docs/latest/api/R/reference/write.ml.html)(object, path, overwrite = FALSE)
```

## Arguments[](https://spark.apache.org/docs/latest/api/R/reference/spark.fmRegressor.html#arguments)

data

a `SparkDataFrame` of observations and labels for model fitting.

formula

a symbolic description of the model to be fitted. Currently only a few formula operators are supported, including '~', '.', ':', '+', and '-'.

...

additional arguments passed to the method.

factorSize

dimensionality of the factors.

fitLinear

whether to fit linear term. # TODO Can we express this with formula?

regParam

the regularization parameter.

miniBatchFraction

the mini-batch fraction parameter.

initStd

the standard deviation of initial coefficients.

maxIter

maximum iteration number.

stepSize

stepSize parameter.

tol

convergence tolerance of iterations.

solver

solver parameter, supported options: "gd" (minibatch gradient descent) or "adamW".

seed

seed parameter for weights initialization.

stringIndexerOrderType

how to order categories of a string feature column. This is used to decide the base level of a string feature as the last category after ordering is dropped when encoding strings. Supported options are "frequencyDesc", "frequencyAsc", "alphabetDesc", and "alphabetAsc". The default value is "frequencyDesc". When the ordering is set to "alphabetDesc", this drops the same category as R when encoding strings.

object

a FM Regression Model model fitted by `spark.fmRegressor`.

newData

a SparkDataFrame for testing.

path

The directory where the model is saved.

overwrite

Overwrites or not if the output path already exists. Default is FALSE which means throw exception if the output path exists.
## Value[](https://spark.apache.org/docs/latest/api/R/reference/spark.fmRegressor.html#value)
`spark.fmRegressor` returns a fitted Factorization Machines Regression Model. `summary` returns summary information of the fitted model, which is a list. `predict` returns the predicted values based on an FMRegressionModel.
## Note[](https://spark.apache.org/docs/latest/api/R/reference/spark.fmRegressor.html#note)
spark.fmRegressor since 3.1.0
summary(FMRegressionModel) since 3.1.0
predict(FMRegressionModel) since 3.1.0
write.ml(FMRegressionModel, character) since 3.1.0
## See also[](https://spark.apache.org/docs/latest/api/R/reference/spark.fmRegressor.html#see-also)
[read.ml](https://spark.apache.org/docs/latest/api/R/reference/read.ml.html)
## Examples[](https://spark.apache.org/docs/latest/api/R/reference/spark.fmRegressor.html#ref-examples)

```
if (FALSE) {
df <- read.df[](https://spark.apache.org/docs/latest/api/R/reference/read.df.html)("data/mllib/sample_linear_regression_data.txt", source = "libsvm")

# fit Factorization Machines Regression Model
model <- spark.fmRegressor(
  df, label ~ features,
  regParam = 0.01, maxIter = 10, fitLinear = TRUE
)

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
