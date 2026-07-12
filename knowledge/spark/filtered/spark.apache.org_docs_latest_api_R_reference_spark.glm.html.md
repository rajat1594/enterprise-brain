[Skip to contents](https://spark.apache.org/docs/latest/api/R/reference/spark.glm.html#main)
[ ![](https://spark.apache.org/images/spark-logo-rev.svg)](https://spark.apache.org/) [SparkR](https://spark.apache.org/docs/latest/api/R/index.html) 4.1.2
  * [Reference](https://spark.apache.org/docs/latest/api/R/reference/index.html)
  * [Articles](https://spark.apache.org/docs/latest/api/R/reference/spark.glm.html)
[SparkR - Practical Guide](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html)


  * 

![](https://spark.apache.org/docs/latest/api/R/reference/spark.glm.html)
# Generalized Linear Models
`spark.glm.Rd`
Fits generalized linear model against a SparkDataFrame. Users can call `summary` to print a summary of the fitted model, `predict` to make predictions on new data, and `write.ml`/`read.ml` to save/load fitted models.
## Usage[](https://spark.apache.org/docs/latest/api/R/reference/spark.glm.html#ref-usage)

```
spark.glm(data, formula, ...)

# S4 method for SparkDataFrame,formula
spark.glm(
  data,
  formula,
  family = gaussian,
  tol = 1e-06,
  maxIter = 25,
  weightCol = NULL,
  regParam = 0,
  var.power = 0,
  link.power = 1 - var.power,
  stringIndexerOrderType = c[](https://rdrr.io/r/base/c.html)("frequencyDesc", "frequencyAsc", "alphabetDesc",
    "alphabetAsc"),
  offsetCol = NULL
)

# S4 method for GeneralizedLinearRegressionModel
summary[](https://spark.apache.org/docs/latest/api/R/reference/summary.html)(object)

# S3 method for summary.GeneralizedLinearRegressionModel
print[](https://rdrr.io/r/base/print.html)(x, ...)

# S4 method for GeneralizedLinearRegressionModel
predict[](https://spark.apache.org/docs/latest/api/R/reference/predict.html)(object, newData)

# S4 method for GeneralizedLinearRegressionModel,character
write.ml[](https://spark.apache.org/docs/latest/api/R/reference/write.ml.html)(object, path, overwrite = FALSE)
```

## Arguments[](https://spark.apache.org/docs/latest/api/R/reference/spark.glm.html#arguments) 

data
    
a SparkDataFrame for training. 

formula
    
a symbolic description of the model to be fitted. Currently only a few formula operators are supported, including '~', '.', ':', '+', '-', '*', and '^'. 

...
    
additional arguments passed to the method. 

family
    
a description of the error distribution and link function to be used in the model. This can be a character string naming a family function, a family function or the result of a call to a family function. Refer R family at <https://stat.ethz.ch/R-manual/R-devel/library/stats/html/family.html>. Currently these families are supported: `binomial`, `gaussian`, `Gamma`, `poisson` and `tweedie`.
Note that there are two ways to specify the tweedie family.
  * Set `family = "tweedie"` and specify the var.power and link.power;
  * When package `statmod` is loaded, the tweedie family is specified using the family definition therein, i.e., `tweedie(var.power, link.power)`.



tol
    
positive convergence tolerance of iterations. 

maxIter
    
integer giving the maximal number of IRLS iterations. 

weightCol
    
the weight column name. If this is not set or `NULL`, we treat all instance weights as 1.0. 

regParam
    
regularization parameter for L2 regularization. 

var.power
    
the power in the variance function of the Tweedie distribution which provides the relationship between the variance and mean of the distribution. Only applicable to the Tweedie family. 

link.power
    
the index in the power link function. Only applicable to the Tweedie family. 

stringIndexerOrderType
    
how to order categories of a string feature column. This is used to decide the base level of a string feature as the last category after ordering is dropped when encoding strings. Supported options are "frequencyDesc", "frequencyAsc", "alphabetDesc", and "alphabetAsc". The default value is "frequencyDesc". When the ordering is set to "alphabetDesc", this drops the same category as R when encoding strings. 

offsetCol
    
the offset column name. If this is not set or empty, we treat all instance offsets as 0.0. The feature specified as offset has a constant coefficient of 1.0. 

object
    
a fitted generalized linear model. 

x
    
summary object of fitted generalized linear model returned by `summary` function. 

newData
    
a SparkDataFrame for testing. 

path
    
the directory where the model is saved. 

overwrite
    
overwrites or not if the output path already exists. Default is FALSE which means throw exception if the output path exists.
## Value[](https://spark.apache.org/docs/latest/api/R/reference/spark.glm.html#value)
`spark.glm` returns a fitted generalized linear model. `summary` returns summary information of the fitted model, which is a list. The list of components includes at least the `coefficients` (coefficients matrix, which includes coefficients, standard error of coefficients, t value and p value), `null.deviance` (null/residual degrees of freedom), `aic` (AIC) and `iter` (number of iterations IRLS takes). If there are collinear columns in the data, the coefficients matrix only provides coefficients. `predict` returns a SparkDataFrame containing predicted labels in a column named "prediction".
## Note[](https://spark.apache.org/docs/latest/api/R/reference/spark.glm.html#note)
spark.glm since 2.0.0
summary(GeneralizedLinearRegressionModel) since 2.0.0
print.summary.GeneralizedLinearRegressionModel since 2.0.0
predict(GeneralizedLinearRegressionModel) since 1.5.0
write.ml(GeneralizedLinearRegressionModel, character) since 2.0.0
## See also[](https://spark.apache.org/docs/latest/api/R/reference/spark.glm.html#see-also)
[glm](https://spark.apache.org/docs/latest/api/R/reference/glm.html), [read.ml](https://spark.apache.org/docs/latest/api/R/reference/read.ml.html)
## Examples[](https://spark.apache.org/docs/latest/api/R/reference/spark.glm.html#ref-examples)

```
if (FALSE) {
sparkR.session[](https://spark.apache.org/docs/latest/api/R/reference/sparkR.session.html)()
t <- as.data.frame[](https://spark.apache.org/docs/latest/api/R/reference/as.data.frame.html)(Titanic, stringsAsFactors = FALSE)
df <- createDataFrame[](https://spark.apache.org/docs/latest/api/R/reference/createDataFrame.html)(t)
model <- spark.glm(df, Freq ~ Sex + Age, family = "gaussian")
summary[](https://spark.apache.org/docs/latest/api/R/reference/summary.html)(model)

# fitted values on training data
fitted <- predict[](https://spark.apache.org/docs/latest/api/R/reference/predict.html)(model, df)
head[](https://spark.apache.org/docs/latest/api/R/reference/head.html)(select[](https://spark.apache.org/docs/latest/api/R/reference/select.html)(fitted, "Freq", "prediction"))

# save fitted model to input path
path <- "path/to/model"
write.ml[](https://spark.apache.org/docs/latest/api/R/reference/write.ml.html)(model, path)

# can also read back the saved model and print
savedModel <- read.ml[](https://spark.apache.org/docs/latest/api/R/reference/read.ml.html)(path)
summary[](https://spark.apache.org/docs/latest/api/R/reference/summary.html)(savedModel)

# note that the default string encoding is different from R's glm
model2 <- glm[](https://spark.apache.org/docs/latest/api/R/reference/glm.html)(Freq ~ Sex + Age, family = "gaussian", data = t)
summary[](https://spark.apache.org/docs/latest/api/R/reference/summary.html)(model2)
# use stringIndexerOrderType = "alphabetDesc" to force string encoding
# to be consistent with R
model3 <- spark.glm(df, Freq ~ Sex + Age, family = "gaussian",
                   stringIndexerOrderType = "alphabetDesc")
summary[](https://spark.apache.org/docs/latest/api/R/reference/summary.html)(model3)

# fit tweedie model
model <- spark.glm(df, Freq ~ Sex + Age, family = "tweedie",
                   var.power = 1.2, link.power = 0)
summary[](https://spark.apache.org/docs/latest/api/R/reference/summary.html)(model)

# use the tweedie family from statmod
library[](https://rdrr.io/r/base/library.html)(statmod)
model <- spark.glm(df, Freq ~ Sex + Age, family = tweedie[](https://rdrr.io/pkg/statmod/man/tweedie.html)(1.2, 0))
summary[](https://spark.apache.org/docs/latest/api/R/reference/summary.html)(model)
}

```

## On this page
Developed by [ The Apache Software Foundation](https://www.apache.org/).
Site built with [pkgdown](https://pkgdown.r-lib.org/) 2.0.1.
Using [preferably](https://preferably.amirmasoudabdol.name/?source=footer) template.
