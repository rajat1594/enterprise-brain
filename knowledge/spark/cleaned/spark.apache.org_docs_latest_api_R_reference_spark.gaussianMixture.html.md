[Skip to contents](https://spark.apache.org/docs/latest/api/R/reference/spark.gaussianMixture.html#main)
[ ![](https://spark.apache.org/images/spark-logo-rev.svg)](https://spark.apache.org/) [SparkR](https://spark.apache.org/docs/latest/api/R/index.html) 4.1.2
  * [Reference](https://spark.apache.org/docs/latest/api/R/reference/index.html)
  * [Articles](https://spark.apache.org/docs/latest/api/R/reference/spark.gaussianMixture.html)
[SparkR - Practical Guide](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html)

  *

![](https://spark.apache.org/docs/latest/api/R/reference/spark.gaussianMixture.html)
# Multivariate Gaussian Mixture Model (GMM)
`spark.gaussianMixture.Rd`
Fits multivariate gaussian mixture model against a SparkDataFrame, similarly to R's mvnormalmixEM(). Users can call `summary` to print a summary of the fitted model, `predict` to make predictions on new data, and `write.ml`/`read.ml` to save/load fitted models.
## Usage[](https://spark.apache.org/docs/latest/api/R/reference/spark.gaussianMixture.html#ref-usage)

```
spark.gaussianMixture(data, formula, ...)

# S4 method for SparkDataFrame,formula
spark.gaussianMixture(data, formula, k = 2, maxIter = 100, tol = 0.01)

# S4 method for GaussianMixtureModel
summary[](https://spark.apache.org/docs/latest/api/R/reference/summary.html)(object)

# S4 method for GaussianMixtureModel
predict[](https://spark.apache.org/docs/latest/api/R/reference/predict.html)(object, newData)

# S4 method for GaussianMixtureModel,character
write.ml[](https://spark.apache.org/docs/latest/api/R/reference/write.ml.html)(object, path, overwrite = FALSE)
```

## Arguments[](https://spark.apache.org/docs/latest/api/R/reference/spark.gaussianMixture.html#arguments)

data

a SparkDataFrame for training.

formula

a symbolic description of the model to be fitted. Currently only a few formula operators are supported, including '~', '.', ':', '+', and '-'. Note that the response variable of formula is empty in spark.gaussianMixture.

...

additional arguments passed to the method.

k

number of independent Gaussians in the mixture model.

maxIter

maximum iteration number.

tol

the convergence tolerance.

object

a fitted gaussian mixture model.

newData

a SparkDataFrame for testing.

path

the directory where the model is saved.

overwrite

overwrites or not if the output path already exists. Default is FALSE which means throw exception if the output path exists.
## Value[](https://spark.apache.org/docs/latest/api/R/reference/spark.gaussianMixture.html#value)
`spark.gaussianMixture` returns a fitted multivariate gaussian mixture model. `summary` returns summary of the fitted model, which is a list. The list includes the model's `lambda` (lambda), `mu` (mu), `sigma` (sigma), `loglik` (loglik), and `posterior` (posterior). `predict` returns a SparkDataFrame containing predicted labels in a column named "prediction".
## Note[](https://spark.apache.org/docs/latest/api/R/reference/spark.gaussianMixture.html#note)
spark.gaussianMixture since 2.1.0
summary(GaussianMixtureModel) since 2.1.0
predict(GaussianMixtureModel) since 2.1.0
write.ml(GaussianMixtureModel, character) since 2.1.0
## See also[](https://spark.apache.org/docs/latest/api/R/reference/spark.gaussianMixture.html#see-also)
mixtools: <https://cran.r-project.org/package=mixtools>
[predict](https://spark.apache.org/docs/latest/api/R/reference/predict.html), [read.ml](https://spark.apache.org/docs/latest/api/R/reference/read.ml.html), [write.ml](https://spark.apache.org/docs/latest/api/R/reference/write.ml.html)
## Examples[](https://spark.apache.org/docs/latest/api/R/reference/spark.gaussianMixture.html#ref-examples)

```
if (FALSE) {
sparkR.session[](https://spark.apache.org/docs/latest/api/R/reference/sparkR.session.html)()
library[](https://rdrr.io/r/base/library.html)(mvtnorm[](http://mvtnorm.R-forge.R-project.org))
set.seed[](https://rdrr.io/r/base/Random.html)(100)
a <- rmvnorm[](https://rdrr.io/pkg/mvtnorm/man/Mvnorm.html)(4, c[](https://rdrr.io/r/base/c.html)(0, 0))
b <- rmvnorm[](https://rdrr.io/pkg/mvtnorm/man/Mvnorm.html)(6, c[](https://rdrr.io/r/base/c.html)(3, 4))
data <- rbind[](https://spark.apache.org/docs/latest/api/R/reference/rbind.html)(a, b)
df <- createDataFrame[](https://spark.apache.org/docs/latest/api/R/reference/createDataFrame.html)(as.data.frame[](https://spark.apache.org/docs/latest/api/R/reference/as.data.frame.html)(data))
model <- spark.gaussianMixture(df, ~ V1 + V2, k = 2)
summary[](https://spark.apache.org/docs/latest/api/R/reference/summary.html)(model)

# fitted values on training data
fitted <- predict[](https://spark.apache.org/docs/latest/api/R/reference/predict.html)(model, df)
head[](https://spark.apache.org/docs/latest/api/R/reference/head.html)(select[](https://spark.apache.org/docs/latest/api/R/reference/select.html)(fitted, "V1", "prediction"))

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
