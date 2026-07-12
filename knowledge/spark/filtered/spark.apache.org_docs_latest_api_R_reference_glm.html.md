[Skip to contents](https://spark.apache.org/docs/latest/api/R/reference/glm.html#main)
[ ![](https://spark.apache.org/images/spark-logo-rev.svg)](https://spark.apache.org/) [SparkR](https://spark.apache.org/docs/latest/api/R/index.html) 4.1.2
  * [Reference](https://spark.apache.org/docs/latest/api/R/reference/index.html)
  * [Articles](https://spark.apache.org/docs/latest/api/R/reference/glm.html)
[SparkR - Practical Guide](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html)


  * 

![](https://spark.apache.org/docs/latest/api/R/reference/glm.html)
# Generalized Linear Models (R-compliant)
`glm.Rd`
Fits a generalized linear model, similarly to R's glm().
## Usage[](https://spark.apache.org/docs/latest/api/R/reference/glm.html#ref-usage)

```
# S4 method for formula,ANY,SparkDataFrame
glm(
  formula,
  family = gaussian,
  data,
  epsilon = 1e-06,
  maxit = 25,
  weightCol = NULL,
  var.power = 0,
  link.power = 1 - var.power,
  stringIndexerOrderType = c[](https://rdrr.io/r/base/c.html)("frequencyDesc", "frequencyAsc", "alphabetDesc",
    "alphabetAsc"),
  offsetCol = NULL
)
```

## Arguments[](https://spark.apache.org/docs/latest/api/R/reference/glm.html#arguments) 

formula
    
a symbolic description of the model to be fitted. Currently only a few formula operators are supported, including '~', '.', ':', '+', and '-'. 

family
    
a description of the error distribution and link function to be used in the model. This can be a character string naming a family function, a family function or the result of a call to a family function. Refer R family at <https://stat.ethz.ch/R-manual/R-devel/library/stats/html/family.html>. Currently these families are supported: `binomial`, `gaussian`, `poisson`, `Gamma`, and `tweedie`. 

data
    
a SparkDataFrame or R's glm data for training. 

epsilon
    
positive convergence tolerance of iterations. 

maxit
    
integer giving the maximal number of IRLS iterations. 

weightCol
    
the weight column name. If this is not set or `NULL`, we treat all instance weights as 1.0. 

var.power
    
the index of the power variance function in the Tweedie family. 

link.power
    
the index of the power link function in the Tweedie family. 

stringIndexerOrderType
    
how to order categories of a string feature column. This is used to decide the base level of a string feature as the last category after ordering is dropped when encoding strings. Supported options are "frequencyDesc", "frequencyAsc", "alphabetDesc", and "alphabetAsc". The default value is "frequencyDesc". When the ordering is set to "alphabetDesc", this drops the same category as R when encoding strings. 

offsetCol
    
the offset column name. If this is not set or empty, we treat all instance offsets as 0.0. The feature specified as offset has a constant coefficient of 1.0.
## Value[](https://spark.apache.org/docs/latest/api/R/reference/glm.html#value)
`glm` returns a fitted generalized linear model.
## Note[](https://spark.apache.org/docs/latest/api/R/reference/glm.html#note)
glm since 1.5.0
## See also[](https://spark.apache.org/docs/latest/api/R/reference/glm.html#see-also)
[spark.glm](https://spark.apache.org/docs/latest/api/R/reference/spark.glm.html)
## Examples[](https://spark.apache.org/docs/latest/api/R/reference/glm.html#ref-examples)

```
if (FALSE) {
sparkR.session[](https://spark.apache.org/docs/latest/api/R/reference/sparkR.session.html)()
t <- as.data.frame[](https://spark.apache.org/docs/latest/api/R/reference/as.data.frame.html)(Titanic)
df <- createDataFrame[](https://spark.apache.org/docs/latest/api/R/reference/createDataFrame.html)(t)
model <- glm(Freq ~ Sex + Age, df, family = "gaussian")
summary[](https://spark.apache.org/docs/latest/api/R/reference/summary.html)(model)
}

```

## On this page
Developed by [ The Apache Software Foundation](https://www.apache.org/).
Site built with [pkgdown](https://pkgdown.r-lib.org/) 2.0.1.
Using [preferably](https://preferably.amirmasoudabdol.name/?source=footer) template.
